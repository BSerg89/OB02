# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на
# обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять
# пользователя из системы.
#
# Требования:
#
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных
# сотрудников).
#
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы `add_user` и `remove_user`, которые
# позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров `User`).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь
# доступ к необходимым атрибутам через методы (например, get и set методы).


class User():
    # access_l = ['user', 'admin']
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._access_l = 'user'

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def __str__(self):
        return f'(ID: {self.get_id()}, Имя: {self.get_name()}, Уровень доступа: {self._access_l})'

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._access_l = 'admin'

    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f'Пользователь {user.get_name()} успешно добавлен.')
        else:
            print('Ошибка при добавлении.')

    def remove_user(self, user_list, id):
        for user in user_list:
            if user.get_id() == id:
                user_list.remove(user)
                print(f'Пользователь {user.get_name()} успешно удален.')
                return
        else:
            print('Ошибка при удалении.')

    def __str__(self):
        return super().__str__()

users = []

admin = Admin(1, 'Admin One')
new_user = User(2, 'User One')
admin.add_user(users, admin)
admin.add_user(users, new_user)
admin.remove_user(users, 1)
for user in users:
    print(user)
