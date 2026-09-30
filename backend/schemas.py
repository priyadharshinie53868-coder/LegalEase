from pydantic import BaseModel, Field, model_validator
from typing import Optional


class DocumentRequest(BaseModel):
    document_type: str = Field(..., min_length=1, description="Type of legal document")
    parties: str = Field(..., min_length=2, description="Parties involved in the contract/agreement")
    terms: str = Field(..., min_length=5, description="Key terms, conditions, compensation, or obligations")
    dates: Optional[str] = Field(None, description="Effective date or key dates")
    effective_date: Optional[str] = Field(None, description="Effective start date of the agreement")
    additional_details: Optional[str] = Field(None, description="Optional extra clauses or custom context")

    @model_validator(mode="before")
    @classmethod
    def sync_date_fields(cls, data):
        if isinstance(data, dict):
            date_val = data.get("dates") or data.get("effective_date")
            if date_val:
                data["dates"] = date_val
                data["effective_date"] = date_val
        return data


class DocumentResponse(BaseModel):
    success: bool
    document_type: str
    content: str
    error: Optional[str] = None


class HealthResponse(BaseModel):
    status: str
    message: str
    version: str = "1.0.0"
