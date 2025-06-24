import uuid
import logging
import pdb

from fastapi import APIRouter, status, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse

from app.process_document.services.process_document_interfaces import (
  ProcessDocumentInterface, 
  SearchVectorDataBaseInterface, 
  QueryQAChainInterface,
  QueryRerankChainInterface
) 
from app.process_document.models.process_document_request import (
  SearchVectorDataBaseRequest, ProcessDocumentRequest
)

router = APIRouter()

@router.post("/api/v1/upload", status_code=200)
async def process_document(
  request: ProcessDocumentRequest
):
  try:
    query_id = str(uuid.uuid4())
    process_document_interface = ProcessDocumentInterface(
      query_id=query_id,
      input_data=request
    )
    result_process = process_document_interface.process_document()
    return JSONResponse(
      status_code=status.HTTP_200_OK,
      content={
        "query_id": query_id,
        "status": result_process
      }
    )
  except Exception as e:
    error_message = (
      f"Error consulta: {type(e).__name__} -"
      f"Mensaje: {str(e)}"
    )
    logging.error(error_message)
    raise HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail={"type": type(e).__name__, "message": str(e)}
    )

@router.post("/api/v1/ask", status_code=200)
async def query_reranked_chain(
  request: SearchVectorDataBaseRequest
):
  try:
    query_rerank_chain_interface = QueryRerankChainInterface(
      input_data=request
    )
    query_rerank_chain_interface.query_rerank_chain()
    return JSONResponse(
      status_code=status.HTTP_200_OK,
      content=query_rerank_chain_interface.query_rerank_chain_response
    )
  except Exception as e:
    error_message = (
      f"Error consulta: {type(e).__name__} -"
      f"Mensaje: {str(e)}"
    )
    logging.error(error_message)
    raise HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail={"type": type(e).__name__, "message": str(e)}
    )
  
@router.post("/api/v1/busqueda_bdv", status_code=200)
async def search_vdb(
  request: SearchVectorDataBaseRequest
):
  try:
    search_vdb_interface = SearchVectorDataBaseInterface(
      input_data=request
    )
    search_vdb_interface.search_vdb()
    return JSONResponse(
      status_code=status.HTTP_200_OK,
      content=search_vdb_interface.query_vdb_response
    )
  except Exception as e:
    error_message = (
      f"Error consulta: {type(e).__name__} -"
      f"Mensaje: {str(e)}"
    )
    logging.error(error_message)
    raise HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail={"type": type(e).__name__, "message": str(e)}
    )