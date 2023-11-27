import sqlite3
from sqlite3 import Cursor


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.connection_cursor = self.connection.cursor()
        self.cursor = self.connection_cursor

    def all_users(self):
        with self.connection:
            result = self.cursor.execute("SELECT user_id FROM users").fetchall()
            return len(result)

    def user_exists(self, user_id):
        result = self.cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,)).fetchall()
        return bool(len(result))

    def add_user(self, user_id, referrer_id=None):
        with self.connection:
            if referrer_id is None:
                self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
            else:
                self.cursor.execute("INSERT INTO 'users' ('user_id', 'referrer_id') VALUES (?, ?)",
                                    (user_id, referrer_id,))

    def get_user(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id FROM users").fetchall()

    def get_referral(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT user_id FROM users WHERE referrer_id = ?", (user_id,)).fetchall()
            return len(result)

    def add_task(self, user_id):
        with self.connection:
            count_task = self.cursor.execute("SELECT tasks FROM users WHERE user_id = ?", (user_id,)).fetchall()
            count_task = int(count_task[0][0]) + 1
            self.cursor.execute("UPDATE users SET tasks = ? WHERE user_id = ?", (count_task, user_id,))

    def delete_task(self, user_id):
        with self.connection:
            count_task = self.cursor.execute("SELECT tasks FROM users WHERE user_id = ?", (user_id,)).fetchall()
            if count_task[0][0] == 0:
                pass
            else:
                count_task = int(count_task[0][0]) - 1
                self.cursor.execute("UPDATE users SET tasks = ? WHERE user_id = ?", (count_task, user_id,))

    def get_friends_tasks(self, user_id):
        tasks = 0
        with self.connection:
            friends_id = self.cursor.execute("SELECT user_id FROM users WHERE referrer_id = ?", (user_id,)).fetchall()
            for row in friends_id:
                result = self.cursor.execute("SELECT tasks FROM users WHERE user_id = ?", (row[0],)).fetchall()
                if result[0][0] >= 10:
                    count = 10
                else:
                    count = result[0][0]
                tasks += count
            balance_for_friends = tasks * 200
            return balance_for_friends

    def get_task_user(self, user_id):
        with self.connection:
            tasks = self.cursor.execute("SELECT tasks FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return tasks[0][0]

    def set_user_name(self, user_name, user_id):
        with self.connection:
            self.cursor.execute("UPDATE users SET user_name = ? WHERE user_id = ?", (user_name, user_id,))

    def get_user_name(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT user_name FROM users WHERE user_id = ?", (user_id,)).fetchall()[0][0]

    def get_all_task_user(self):
        with self.connection:
            user = self.cursor.execute("SELECT tasks, user_id, user_name FROM users").fetchall()
            return user
