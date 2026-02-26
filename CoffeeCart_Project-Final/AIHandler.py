import ollama

class AIHandler:
    @staticmethod
    def analyze_order(customer_name, items):
        order_details = ", ".join([item.name for item in items])
        
        # עדכון ה-Prompt כדי שיכלול כותרת ברורה לעוגיית המזל
        prompt = (
            f"The customer's name is {customer_name}. They ordered: {order_details}. "
            f"Please write a short, personal response in English. "
            f"1) Briefly summarize their order and address them by name. "
            f"2) Provide a clear 'Fortune Cookie' message on a new line, starting with the header: "
            f"'--- 🥠 FORTUNE COOKIE MESSAGE ---'"
        )
        
        try:
            # שליחת הבקשה למכולה 'dore' שרצה ב-Docker
            response = ollama.chat(model='phi3', messages=[
                {'role': 'user', 'content': prompt},
            ])
            return response['message']['content']
        except Exception as e:
            # טיפול בשגיאות למקרה שה-Docker כבוי
            print(f"Error connecting to AI: {e}")
            return "Your fortune is brewing... (AI connection pending)"
