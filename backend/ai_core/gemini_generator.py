import os
import logging
from dotenv import load_dotenv
from backend.utils.text_utils import sanitize_document_text

load_dotenv()
logger = logging.getLogger("legalease.gemini")

DEFAULT_MODEL = "gemini-2.5-flash"


def get_gemini_config():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    model_name = os.getenv("GEMINI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
    return api_key, model_name


def generate_legal_document(prompt: str) -> str:
    """
    Calls the Google Gemini API to generate the legal document draft.
    Supports google-genai client and legacy google.generativeai fallback.
    """
    api_key, model_name = get_gemini_config()

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not configured. Please set your API key in the .env file."
        )

    # 1. Try modern google-genai SDK
    try:
        from google import genai

        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
        )
        if response and response.text:
            return sanitize_document_text(response.text)
    except ImportError:
        logger.info("google-genai not found, attempting google.generativeai fallback.")
    except Exception as e:
        logger.warning(f"google-genai SDK call failed: {e}. Attempting alternative invocation...")

    # 2. Try google.generativeai fallback
    try:
        import google.generativeai as genai_legacy

        genai_legacy.configure(api_key=api_key)
        model = genai_legacy.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        if response and response.text:
            return sanitize_document_text(response.text)
    except ImportError:
        pass
    except Exception as e:
        logger.error(f"google.generativeai SDK error: {e}")
        raise RuntimeError(f"Error generating document via Gemini API: {str(e)}")

    # 3. Direct REST API fallback if SDK fails
    try:
        import requests

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        res = requests.post(url, json=payload, timeout=60)
        if res.status_code == 200:
            data = res.json()
            candidates = data.get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                if parts:
                    return sanitize_document_text(parts[0].get("text", ""))
        else:
            error_data = res.json().get("error", {})
            error_msg = error_data.get("message", res.text)
            raise RuntimeError(f"Gemini API returned status {res.status_code}: {error_msg}")
    except Exception as rest_err:
        logger.error(f"REST API fallback error: {rest_err}")
        raise RuntimeError(f"Gemini API generation failed: {str(rest_err)}")

    raise RuntimeError("Failed to receive a valid response from Gemini API.")
