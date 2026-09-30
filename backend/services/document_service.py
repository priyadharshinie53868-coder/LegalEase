import logging
from backend.schemas import DocumentRequest, DocumentResponse
from backend.ai_core.prompt_builder import build_legal_prompt
from backend.ai_core.gemini_generator import generate_legal_document
from backend.utils.validators import validate_document_request
from backend.utils.history_manager import save_document_to_history
from backend.utils.summary_utils import extract_executive_summary

logger = logging.getLogger("legalease.service")


def process_document_generation(request: DocumentRequest) -> DocumentResponse:
    """
    Coordinates validation, prompt generation, AI invocation, history archiving, and summary formatting.
    """
    # 1. Validate
    is_valid, err_msg = validate_document_request(request)
    if not is_valid:
        return DocumentResponse(
            success=False,
            document_type=request.document_type,
            content="",
            error=err_msg
        )

    # 2. Build Prompt
    eff_date = request.effective_date or request.dates or "Effective Immediately upon Execution"
    prompt = build_legal_prompt(
        document_type=request.document_type,
        parties=request.parties,
        terms=request.terms,
        effective_date=eff_date,
        additional_details=request.additional_details or ""
    )

    # 3. Call AI
    try:
        generated_content = generate_legal_document(prompt)
        if not generated_content or not generated_content.strip():
            return DocumentResponse(
                success=False,
                document_type=request.document_type,
                content="",
                error="The AI model generated an empty document. Please try again with more specific terms."
            )

        # 4. Auto-save to History
        try:
            save_document_to_history(
                document_type=request.document_type,
                parties=request.parties,
                terms=request.terms,
                dates=eff_date,
                content=generated_content,
                additional_details=request.additional_details
            )
        except Exception as hist_err:
            logger.warning(f"Failed to auto-save to history: {hist_err}")

        return DocumentResponse(
            success=True,
            document_type=request.document_type,
            content=generated_content,
            error=None
        )
    except ValueError as ve:
        logger.warning(f"Configuration error: {ve}")
        return DocumentResponse(
            success=False,
            document_type=request.document_type,
            content="",
            error=str(ve)
        )
    except Exception as e:
        logger.error(f"Generation error: {e}", exc_info=True)
        return DocumentResponse(
            success=False,
            document_type=request.document_type,
            content="",
            error=f"Unable to generate document: {str(e)}"
        )
