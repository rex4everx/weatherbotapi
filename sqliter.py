import sqlite3


class SQLighter:

    def __init__(self, db):
        # Подключаемся к БД и сохраняем курсор соединения
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    # def get_subscriptions(self, status=True):
    #     # Получаем всех активных подписчиков бота
    #     with self.connection:
    #         return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()

    # def add_subscriber(self, user_id, status=True):
    #     # Добавляем нового подписчика
    #     with self.connection:
    #         return self.cursor.execute("INSERT INTO `subscriptions` (`user_id`, `status`) VALUES(?,?)",
    #                                    (user_id, status))

    def subscriber_exists(self, user_id):
        # Проверяем, есть ли уже юзер в базе#
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM 'users' WHERE users_id = {user_id}").fetchall()
            return bool(len(result))

    def update_subscription(self, user_id, lat, long):
        # Обновляем статус подписки пользователя
        with self.connection:
            return self.cursor.execute(
                f"UPDATE 'users' SET 'latitude' = {lat}, 'longitude' = {long} WHERE 'user_id' = {user_id}")

    def add_locator(self, user_id, lat, long):
        with self.connection:
            return self.cursor.execute(
                f"INSERT INTO 'users' ('users_id', 'latitude', 'longitude') VALUES ({user_id}, {lat}, {long})")

    def take_pos(self, user_id):
        #Берем его координаты
        with self.connection:
            result = self.cursor.execute(
                f"SELECT latitude, longitude FROM 'users' WHERE users_id = {user_id}").fetchone()
            return result

    def close(self):
        # Закрываем соединение с БД
        self.connection.close()
