import ollama

class AIHandler:
    @staticmethod
    def analyze_order(customer_name, items):
        """Generates order summary + Fortune Cookie message in English"""
        order_details = ", ".join([item.name for item in items])
        
        # ההנחיה החדשה ל-AI
        prompt = (
            f"Customer {customer_name} ordered: {order_details}. "
            f"Please write a short response in English: "
            f"1) Briefly summarize the items ordered. "
            f"2) Add a funny or inspiring 'Fortune Cookie' message based on these items."
        )
        
        try:
            # שימוש במודל llama3 שהורדת בהצלחה
            response = ollama.chat(model='llama3', messages=[
                {'role': 'user', 'content': prompt},
            ])
            return response['message']['content']
        except Exception:
            return "Your fortune is brewing... try again later!"