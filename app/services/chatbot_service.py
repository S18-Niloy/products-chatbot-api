from app.services.product_service import ProductService
from app.utils.groq_client import GroqClient

product_service = ProductService()
groq = GroqClient()

def generate_chat_response(user_message: str):
    # 1️⃣ Extract product name from user message
    product_name = product_service.extract_product_name(user_message)
    if not product_name:
        return "Sorry, I couldn't find a product in your message."

    # 2️⃣ Fetch product details
    product = product_service.get_product_by_name(product_name)
    if not product:
        return f"Sorry, we don't have information about {product_name}."

    # 3️⃣ Prepare context for Groq
    prompt = f"""
    You are a helpful assistant for an e-commerce website.
    Product info: {product}
    Answer this customer question naturally: "{user_message}"
    """

    # 4️⃣ Call Groq model
    return groq.chat([{"role": "user", "content": prompt}])
