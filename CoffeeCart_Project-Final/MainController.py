from DatabaseManager import DatabaseManager
from ConsoleView import ConsoleView
from Product import Product
from Coffee import Coffee
from AIHandler import AIHandler

class MainController:
    def __init__(self):
        self.db = DatabaseManager()
        self.view = ConsoleView()
        self.menu = [
            Coffee(1, "Cappuccino", 15),
            Coffee(2, "Latte (Oat)", 15, "Oat"),
            Product(3, "Croissant", 12),
            Product(4, "Cookie", 7)
        ]

    def run(self):
        """לולאת REPL ראשית המנהלת את התפריט (סעיף 17)"""
        while True:
            # תפריט מורחב - אופציה 4 שונתה למוצר מומלץ (Best Seller)
            print("\n1. New Order | 2. Full History | 3. Search by Name | 4. Most Recommended | 5. Exit")
            choice = self.view.get_input("Select option")

            if choice == '1':
                self.process_multi_item_order()
            
            elif choice == '2':
                # שליפת נתונים מהמודל והצגתם דרך ה-View
                orders = self.db.get_all_orders()
                self.view.display_history(orders)
            
            elif choice == '3':
                # חיפוש היסטוריה לפי שם לקוח (דרישה 4)
                name_to_search = self.view.get_input("Enter customer name to search (or 'q' to go back)")
                if name_to_search.lower() != 'q':
                    results = self.db.get_orders_by_customer(name_to_search)
                    self.view.display_history(results)

            elif choice == '4':
                # ניתוח נתונים מה-Database למציאת המוצר הפופולרי ביותר
                recommendation = self.db.get_most_sold_product()
                if recommendation:
                    product_info, count = recommendation
                    self.view.show_message(f"Our Best Seller: {product_info}")
                    self.view.show_message(f"Sold {count} times! Highly recommended.")
                else:
                    self.view.show_message("No sales data available yet for recommendations.")

            elif choice in ['5', 'q', 'exit']:
                self.view.show_message("Exiting system. Goodbye!")
                break

    def process_multi_item_order(self):
        """ניהול הזמנה מרובת פריטים עם שמירה מרוכזת (דרישות 1, 2, 3, 15)"""
        current_cart = []
        self.view.display_menu(self.menu)
        
        name = self.view.get_input("Customer Name (or 'q' to cancel)")
        if name.lower() == 'q':
            self.view.show_message("Order cancelled.")
            return

        while True:
            pid = self.view.get_input("Enter Product ID to add (or 'f' to finish, 'q' to cancel)")
            
            if pid.lower() == 'q':
                self.view.show_message("Order cancelled and items cleared.")
                return 
            
            if pid.lower() == 'f':
                break
            
            # עבודה עם Instances של מחלקות (סעיף 5 בנספח)
            product = next((p for p in self.menu if str(p.product_id) == pid), None)
            
            if product:
                current_cart.append(product)
                self.view.show_message(f"Added {product.name} to cart.")
            else:
                self.view.show_message("Product not found.")

        if current_cart:
            # יצירת טקסט המכיל את כל ה-IDs והשמות של המוצרים בסל
            items_details = ", ".join([f"[{p.product_id}] {p.name}" for p in current_cart])
            # שימוש ב-get_price מדגים פולימורפיזם (סעיף 8 בנספח)
            total_price = sum([item.get_price() for item in current_cart])
            
            # שמירה אחת בלבד למסד הנתונים עבור כל ההזמנה
            self.db.save_order(items_details, name, total_price)

            # הצגת קבלה מסודרת דרך ה-View (דרישה 2)
            self.view.display_order_summary(name, current_cart)
            
            # הפעלת מנוע ה-AI עם ה-Prompt החדש (בונוס)
            self.view.show_message("AI is analyzing the order personality...")
            insight = AIHandler.analyze_order(name, current_cart)
            print(f"\n[AI Insight]: {insight}")
        else:
            self.view.show_message("No items selected.")

if __name__ == "__main__":
    MainController().run()