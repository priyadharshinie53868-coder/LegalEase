import os
import sys
import datetime
import requests

# Ensure project root is in sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
from dotenv import load_dotenv

try:
    from frontend.components.document_editor import render_document_editor
    from backend.utils.history_manager import get_all_history, delete_history_by_id, clear_all_history
except ImportError:
    from components.document_editor import render_document_editor
    from utils.history_manager import get_all_history, delete_history_by_id, clear_all_history

# Load environment variables
load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000").rstrip("/")

# Configure Page (Centered layout matching PDF)
st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Clean Modern Styling
st.markdown(
    """
    <style>
    .main-header-title {
        text-align: center;
        font-size: 2.1rem;
        font-weight: 700;
        margin-top: 6px;
        margin-bottom: 2px;
    }
    .stButton>button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        font-weight: 600;
        padding: 0.6rem 1rem;
        border-radius: 6px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Preset Templates for quick testing
PRESET_OPTIONS = {
    "— Select Preset (Optional) —": None,
    "Freelance Work Contract": {
        "doc_type": "Freelance Work Contract",
        "parties": "Jane Doe (Service Provider), TechNova Inc. (Client)",
        "terms": "Work must be delivered by May 15, 2025;\nPayment will be made within 7 days of invoice;\nThe client retains intellectual property rights;\nEither party may terminate with 14 days notice",
        "dates": "April 15, 2025"
    },
    "Employment Contract": {
        "doc_type": "Employment Contract",
        "parties": "Acme Technologies Pvt Ltd (Employer), Rahul Sharma (Employee)",
        "terms": "Role: Senior Software Engineer;\nSalary: ₹18,00,000 CTC per annum;\nNotice Period: 60 Days;\nWorking Hours: 9:30 AM to 6:30 PM (Mon-Fri)",
        "dates": "October 1, 2026"
    },
    "Non-Disclosure Agreement (NDA)": {
        "doc_type": "NDA (Non-Disclosure Agreement)",
        "parties": "Nexus Ventures LLC (Party A), Vertex Software Systems Inc (Party B)",
        "terms": "Purpose: Evaluating strategic technology partnership;\nConfidentiality Duration: 3 Years;\nReturn of confidential information within 14 days upon written demand",
        "dates": "November 1, 2026"
    },
    "Residential Lease Agreement": {
        "doc_type": "Lease Agreement",
        "parties": "Suresh Menon (Landlord), Priya Patel (Tenant)",
        "terms": "Property Address: Flat 402, Green Meadows, Indiranagar, Bengaluru;\nMonthly Rent: ₹35,000 payable by 5th of each month;\nSecurity Deposit: ₹1,50,000 (Refundable upon vacating)",
        "dates": "January 1, 2027"
    }
}


def render_sidebar():
    """
    Renders the clean Sidebar containing generation History and sample presets.
    """
    with st.sidebar:
        st.markdown("### 💡 Quick Presets")
        selected_preset = st.selectbox(
            "Load Sample Contract",
            list(PRESET_OPTIONS.keys()),
            label_visibility="collapsed"
        )
        preset_data = PRESET_OPTIONS.get(selected_preset)

        st.markdown("---")
        st.markdown("### 📜 Generation History")
        
        history = get_all_history()
        if not history:
            st.caption("No past documents yet. Generate a contract to see it archived here.")
        else:
            search = st.text_input("🔍 Search History", placeholder="Filter by type or party...", label_visibility="collapsed")
            filtered = history
            if search and search.strip():
                q = search.strip().lower()
                filtered = [h for h in history if q in h.get("document_type", "").lower() or q in h.get("parties", "").lower()]

            st.caption(f"Showing {len(filtered)} saved drafts:")
            
            for item in filtered:
                doc_id = item.get("id")
                doc_type = item.get("document_type", "Document")
                created_at = item.get("created_at", "").split()[0]
                
                col_btn, col_del = st.columns([4, 1])
                with col_btn:
                    if st.button(f"📄 {doc_type} ({created_at})", key=f"hist_{doc_id}", use_container_width=True):
                        st.session_state.generated_document = item.get("content", "")
                        st.session_state.edited_document = item.get("content", "")
                        st.session_state.document_type = item.get("document_type", "")
                        st.session_state.current_parties = item.get("parties", "")
                        st.session_state.current_terms = item.get("terms", "")
                        st.session_state.current_dates = item.get("dates", "")
                        st.session_state.show_edit = False
                        st.rerun()
                with col_del:
                    if st.button("🗑️", key=f"del_side_{doc_id}", help="Delete"):
                        delete_history_by_id(doc_id)
                        st.rerun()

            if st.button("Clear All History", use_container_width=True):
                clear_all_history()
                st.rerun()

    return preset_data


def main():
    # Render Sidebar with History & Presets
    preset_data = render_sidebar()

    # Centered Logo (Page 13, 18 of PDF)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists("assets/logo.png"):
            st.image("assets/logo.png", use_container_width=True)

    # Sub-title
    st.markdown("<h2 class='main-header-title'>AI Legal Document Generator</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Handle defaults from preset or history selection
    default_doc_type = preset_data.get("doc_type", "") if preset_data else st.session_state.get("current_doc_type", "")
    default_parties = preset_data.get("parties", "") if preset_data else st.session_state.get("current_parties", "")
    default_terms = preset_data.get("terms", "") if preset_data else st.session_state.get("current_terms", "")
    default_dates = preset_data.get("dates", "") if preset_data else st.session_state.get("current_dates", "")

    # Input Fields (Pages 18-19 of PDF)
    document_type = st.text_input(
        "Document Type (Ex: Agreement, Contract, NDA)",
        value=default_doc_type,
        placeholder="Freelance Work Contract"
    )

    parties = st.text_area(
        "Parties Involved",
        value=default_parties,
        placeholder="Jane Doe (Service Provider), TechNova Inc. (Client)",
        height=100
    )

    terms = st.text_area(
        "Terms & Conditions (Use semicolons for bullet points)",
        value=default_terms,
        placeholder="Work must be delivered by May 15, 2025;\nPayment will be made within 7 days of invoice;\nThe client retains intellectual property rights;",
        height=120
    )

    dates = st.text_input(
        "Effective Date",
        value=default_dates,
        placeholder="April 15, 2025"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Action Button
    if st.button("Generate Document"):
        if not document_type.strip():
            st.error("⚠️ Please specify the Document Type.")
            return
        if not parties.strip():
            st.error("⚠️ Please provide the Parties Involved.")
            return
        if not terms.strip():
            st.error("⚠️ Please specify the Terms & Conditions.")
            return
        if not dates.strip():
            st.error("⚠️ Please specify the Effective Date.")
            return

        with st.spinner("⏳ Generating legal draft via Gemini AI..."):
            payload = {
                "document_type": document_type.strip(),
                "parties": parties.strip(),
                "terms": terms.strip(),
                "dates": dates.strip(),
                "effective_date": dates.strip()
            }

            try:
                response = requests.post(f"{BACKEND_URL}/generate", json=payload, timeout=60)
                if response.status_code == 200:
                    data = response.json()
                    if data.get("success"):
                        st.session_state.generated_document = data.get("content", "")
                        st.session_state.edited_document = data.get("content", "")
                        st.session_state.document_type = document_type.strip()
                        st.session_state.current_parties = parties.strip()
                        st.session_state.current_terms = terms.strip()
                        st.session_state.current_dates = dates.strip()
                        st.session_state.show_edit = False
                        st.success("✅ Document Generated Successfully!")
                    else:
                        st.error(f"❌ Generation Failed: {data.get('error')}")
                else:
                    st.error(f"❌ Server Error ({response.status_code}): {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("❌ Could not connect to FastAPI backend. Make sure `uvicorn backend.main:app` is running on port 8000.")
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")

    # Render Preview, Inline Editor & Download Options
    render_document_editor()


if __name__ == "__main__":
    main()
