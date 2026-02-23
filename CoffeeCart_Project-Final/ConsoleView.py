class ConsoleView:
    @staticmethod
    def display_menu(products):
        print("\n" + "="*45)
        print(f"{'ID':<4} | {'Product':<20} | {'Price':<10}")
        print("-" * 45)
        for p in products:
            print(f"{p.product_id:<4} | {p.name:<20} | ₪{p.get_price():<10}")
        print("="*45)

    @staticmethod
    def display_history(orders):
        """הצגת היסטוריית הזמנות בפורמט מורחב (דרישה 2, 15)"""
        if not orders:
            print("\n>>> No order history found.")
            return
        
        # הגדלנו את הרוחב ל-90 תווים כדי שרשימת המוצרים תיכנס יפה
        print("\n" + "="*95)
        print(f"{'ID':<4} | {'Customer':<12} | {'Products (ID & Name)':<35} | {'Total':<8} | {'Date'}")
        print("-" * 95)
        for row in orders:
            # row[1] הוא ה-products_info שמכיל את כל רשימת המוצרים
            print(f"{row[0]:<4} | {row[2]:<12} | {row[1]:<35} | ₪{row[3]:<7} | {row[4]}")
        print("="*95)

    @staticmethod
    def get_input(prompt):
        return input(f">>> {prompt}: ")

    @staticmethod
    def show_message(msg):
        print(f"\n[*] {msg}")

    @staticmethod
    def display_order_summary(customer_name, items):
        print("\n" + "*"*40)
        print(f" RECEIPT FOR: {customer_name}")
        print("*"*40)
        total = 0
        for item in items:
            print(f"- {item}") 
            total += item.get_price()
        print("-" * 40)
        print(f"TOTAL AMOUNT: ₪{total}")
        print("*"*40)