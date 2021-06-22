import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def add(self, new):
        try:
            self.__cur.execute("INSERT INTO suppliers VALUES (NULL, ?,  ?, ?, ?, ?, ?, ?)", (new['organisation']
                                                                                             , new['until'],
                                                                                             new['category'],
                                                                                             new['load_date'],
                                                                                             new['unload_date'],
                                                                                             new['responsible'],
                                                                                             new['comment']))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления" + str(e))
            return False

        return True

    def get_suppliers_list(self):
        try:
            self.__cur.execute("SELECT id, organisation, until, category, load_date, unload_date, responsible, "
                               "comment FROM suppliers")
            res = self.__cur.fetchall()
            if res:
                result = []
                for f in res:
                    result.append({
                        'id': f[0],
                        'organisation': f[1],
                        'until': f[2],
                        'category': f[3],
                        'load_date': f[4],
                        'unload_date': f[5],
                        'responsible': f[6],
                        'comment': f[7],
                    })
                return result
        except sqlite3.Error as e:
            print("Ошибка получения списка " + str(e))
            return []

    def delete(self, supplier_id):
        try:
            self.__cur.execute(f"DELETE FROM suppliers WHERE id={supplier_id}")
            self.__db.commit()
        except sqlite3.Error as e:
            return 400

        return 'success'

    def change(self, supplier_id, supplier_data):
        print(supplier_data)
        try:
            query = """UPDATE suppliers SET organisation=?, until=?, category=?, load_date=?, unload_date=?, 
            responsible=?, comment=? WHERE id=? """
            data = (supplier_data['organisation'],
                    supplier_data['until'],
                    supplier_data['category'],
                    supplier_data['load_date'],
                    supplier_data['unload_date'],
                    supplier_data['responsible'],
                    supplier_data['comment'],
                    supplier_id
                    )
            self.__cur.execute(query, data)
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка изменения " + str(e))
            return False

        return True

    def add_user(self, user_name, password, role='user'):
        try:
            query = """INSERT INTO users VALUES (NULL, ?, ?, ?)"""
            data = (user_name, password, role)
            self.__cur.execute(query, data)
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления пользователя в db " + str(e))
            return False
        return {'user_name': user_name, 'role': role}

    def get_users(self):
        try:
            query = """SELECT user_name FROM users"""
            self.__cur.execute(query)
            res = self.__cur.fetchall()
            result = []
            for r in res:
                for re in r:
                    result.append(re)
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка " + str(e))
            return False
        return result

    def get_user_data(self, user_name):
        try:
            query = """SELECT id, user_name, password, role FROM users WHERE user_name=?"""
            data = (user_name,)
            self.__cur.execute(query, data)
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения из db " + str(e))

    def find(self, find_data):
        # print(find_data.keys)
        table_headers= {
            '№': 'id',
            'организация': 'organisation',
            'контракт до': 'until',
            'категория товара': 'category',
            'дата погрузки': 'load_date',
            'дата разгрузки': 'unload_date',
            'отв. лицо': 'responsible',
            'комментарий': 'comment'
        }
        all_find_criteria = ''
        for key in list(find_data.keys()):
            # print(key)
            current_find_criteria = f'{table_headers[key]} in ( '
            # print(len(find_data[key])-1)
            for value in find_data[key]:
                # print(value)
                # print(len(find_data[key])-1)
                if find_data[key].index(value) != len(find_data[key])-1:
                    current_find_criteria += f'\'{value}\', '
                else:
                    current_find_criteria += f'\'{value}\' )'
            if list(find_data.keys()).index(key) != len(find_data)-1:
                all_find_criteria += f"{current_find_criteria} AND "
            else:
                all_find_criteria += f"{current_find_criteria}"
        # print(all_find_criteria)
        try:
            query = f'SELECT id, organisation, until, category, load_date, unload_date, responsible, comment ' \
                    f'FROM suppliers WHERE {all_find_criteria}'
            print(query)
            self.__cur.execute(query)
            res = self.__cur.fetchall()
            if res:
                result = []
                for f in res:
                    result.append({
                        'id': f[0],
                        'organisation': f[1],
                        'until': f[2],
                        'category': f[3],
                        'load_date': f[4],
                        'unload_date': f[5],
                        'responsible': f[6],
                        'comment': f[7],
                    })
                return result
        except sqlite3.Error as e:
            print("Ошибка поиска " + str(e))
