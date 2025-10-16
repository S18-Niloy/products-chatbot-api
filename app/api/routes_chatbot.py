from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chatbot_service import generate_chat_response
from app.services.product_service import ProductService
router = APIRouter(prefix="/api", tags=["chatbot"])
prod_svc = ProductService()
@router.get("/products")
def get_products(): return {"products": prod_svc.fetch_all_products()}
@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest): return {"response": generate_chat_response(req.message)}
