from fastapi import APIRouter, HTTPException, status
from backend.schemas import DocumentRequest, DocumentResponse, HealthResponse
from backend.services.document_service import process_document_generation
from backend.utils.history_manager import (
    get_all_history,
    get_history_by_id,
    delete_history_by_id,
    clear_all_history
)

router = APIRouter()


@router.get("/", tags=["Root"])
def root_endpoint():
    return {
        "app": "LegalEase API",
        "description": "AI-Powered Legal Document Generator Backend",
        "docs": "/docs",
        "health": "/health",
        "history": "/history"
    }


@router.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check():
    return HealthResponse(
        status="ok",
        message="LegalEase API backend is healthy and operational."
    )


@router.post("/generate", response_model=DocumentResponse, tags=["Document Generation"])
def generate_document(request: DocumentRequest):
    try:
        response = process_document_generation(request)
        if not response.success and response.error and "is required" in response.error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=response.error
            )
        return response
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected internal server error occurred while processing your document request."
        )


@router.get("/history", tags=["History"])
def get_document_history():
    """Returns list of past generated legal document records."""
    return get_all_history()


@router.get("/history/{doc_id}", tags=["History"])
def get_single_document_history(doc_id: str):
    """Retrieves a single past document by ID."""
    doc = get_history_by_id(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document draft not found.")
    return doc


@router.delete("/history/{doc_id}", tags=["History"])
def delete_single_document(doc_id: str):
    """Deletes a document from history."""
    success = delete_history_by_id(doc_id)
    if not success:
        raise HTTPException(status_code=404, detail="Document not found.")
    return {"status": "success", "message": f"Document {doc_id} deleted."}


@router.delete("/history", tags=["History"])
def clear_history():
    """Clears all document history."""
    clear_all_history()
    return {"status": "success", "message": "All history cleared."}
