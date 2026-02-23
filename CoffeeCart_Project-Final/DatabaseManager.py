import sqlite3

class DatabaseManager:
    def __init__(self, db_name="coffee_cart.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """יצירת טבלה שבה כל שורה היא הזמנה שלמה (Order)"""
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            products_info TEXT,
                            customer_name TEXT,
                            total_price REAL,
                            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()

    def save_order(self, products_info, customer_name, total_price):
        """שמירת פרטי המוצרים והלקוח כשורה אחת"""
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO orders (products_info, customer_name, total_price) VALUES (?, ?, ?)",
                       (products_info, customer_name, total_price))
        self.conn.commit()

    def get_all_orders(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM orders ORDER BY order_date DESC")
        return cursor.fetchall()

    def get_orders_by_customer(self, customer_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE customer_name LIKE ? ORDER BY order_date DESC", 
                       ('%' + customer_name + '%',))
        return cursor.fetchall()

    def get_most_sold_product(self):
        """
        ניתוח נתונים: מציאת המוצר הנמכר ביותר מתוך מחרוזות הטקסט ב-DB.
        פונקציה זו מדגימה שימוש בנתונים קיימים להפקת המלצות (סעיף 15, 28).
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT products_info FROM orders")
        all_rows = cursor.fetchall()
        
        if not all_rows:
            return None
            
        product_counts = {}
        for row in all_rows:
            # פירוק המחרוזת (למשל: "[1] Cappuccino, [3] Croissant") לפריטים נפרדים
            items = row[0].split(", ")
            for item in items:
                # ניקוי רווחים מיותרים וספירה
                item = item.strip()
                product_counts[item] = product_counts.get(item, 0) + 1
        
        if not product_counts:
            return None
            
        # מציאת המפתח (שם המוצר) עם הערך (כמות) הגבוה ביותר
        most_sold = max(product_counts, key=product_counts.get)
        return most_sold, product_counts[most_sold]