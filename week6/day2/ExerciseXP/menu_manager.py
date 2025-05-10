import psycopg2
from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        connection = psycopg2.connect(database="restaurant_db", user="postgres", password="2525")
        cursor = connection.cursor()
        cursor.execute("SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s", (name,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return MenuItem(name=result[0], price=result[1])
        else:
            return None

    @classmethod
    def all_items(cls):
        connection = psycopg2.connect(database="restaurant_db", user="postgres", password="2525")
        cursor = connection.cursor()
        cursor.execute("SELECT item_name, item_price FROM Menu_Items")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return [MenuItem(name=row[0], price=row[1]) for row in rows]