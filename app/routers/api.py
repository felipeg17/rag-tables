from fastapi import APIRouter
from app.process_document.controller.process_document_controller import \
  router as process_document_router

router = APIRouter(
  prefix="/rag-tables",
  tags=["Procesar documentos"]
)

router.include_router(process_document_router)
