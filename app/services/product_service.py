# product_service.py
import httpx
from app.core.config import settings

class ProductService:
    def __init__(self):
        self.client = httpx.Client(timeout=15.0)

    def fetch_all_products(self):
        url = f"{settings.DUMMYJSON_BASE}/products"
        resp = self.client.get(url)
        resp.raise_for_status()
        return resp.json().get("products", [])

    def get_product_by_name(self, name: str):
        """Return a product dict if the name matches any product title (case-insensitive)"""
        products = self.fetch_all_products()
        for p in products:
            if p["title"].lower() == name.lower():
                return p
        return None

    def extract_product_name(self, message: str):
        """Simple heuristic: find the first product title mentioned in the message"""
        products = self.fetch_all_products()
        message_lower = message.lower()
        for p in products:
            if p["title"].lower() in message_lower:
                return p["title"]
        return None
