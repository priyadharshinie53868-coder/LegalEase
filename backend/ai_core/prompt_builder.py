"""
Adaptive Legal Document Prompt Builder for LegalEase.
Enforces strict hierarchical structure, de-clustered spacing, professional legal phrasing,
and clean signature formatting.
"""

DOCUMENT_SPECIFIC_INSTRUCTIONS = {
    "Freelance Work Contract": """
STRUCTURE REQUIREMENTS:
1. TITLE: Centered bold title "FREELANCE SERVICES AGREEMENT".
2. PREAMBLE & RECITALS: Formal identification of Client and Independent Contractor, effective date, and "WHEREAS" background statements.
3. SECTION 1 - SCOPE OF WORK & DELIVERABLES: Clear description of services, project milestones, deadlines, and delivery acceptance criteria.
4. SECTION 2 - COMPENSATION & PAYMENT TERMS: Total fee, installment breakdown, invoicing schedule, payment due window, and late fees.
5. SECTION 3 - INTELLECTUAL PROPERTY RIGHTS: Clear assignment of work product upon full payment.
6. SECTION 4 - INDEPENDENT CONTRACTOR STATUS: Explicit confirmation of non-employee status, tax responsibility.
7. SECTION 5 - CONFIDENTIALITY: Mutual protection of proprietary business information and client materials.
8. SECTION 6 - TERM & TERMINATION: Term duration, mutual written notice period.
9. SECTION 7 - WARRANTIES & LIMITATION OF LIABILITY.
10. SECTION 8 - GOVERNING LAW & DISPUTE RESOLUTION.
11. SIGNATURE BLOCKS: Formal execution blocks with Name, Title, Signature Line, and Date.
""",
    "Freelance Contract": """
STRUCTURE REQUIREMENTS:
1. TITLE: Centered bold title "FREELANCE SERVICES AGREEMENT".
2. PREAMBLE & RECITALS: Formal identification of Client and Independent Contractor, effective date, and "WHEREAS" background statements.
3. SECTION 1 - SCOPE OF WORK & DELIVERABLES: Clear description of services, project milestones, deadlines, and delivery acceptance criteria.
4. SECTION 2 - COMPENSATION & PAYMENT TERMS: Total fee, installment breakdown, invoicing schedule, payment due window, and late fees.
5. SECTION 3 - INTELLECTUAL PROPERTY RIGHTS: Clear assignment of work product upon full payment.
6. SECTION 4 - INDEPENDENT CONTRACTOR STATUS: Explicit confirmation of non-employee status.
7. SECTION 5 - CONFIDENTIALITY: Mutual protection of proprietary business information and client materials.
8. SECTION 6 - TERM & TERMINATION: Term duration, mutual written notice period.
9. SECTION 7 - WARRANTIES & LIMITATION OF LIABILITY.
10. SECTION 8 - GOVERNING LAW & DISPUTE RESOLUTION.
11. SIGNATURE BLOCKS: Formal execution blocks with Name, Title, Signature Line, and Date.
""",
    "Employment Contract": """
STRUCTURE REQUIREMENTS:
1. TITLE: Centered bold title "EMPLOYMENT AGREEMENT".
2. PREAMBLE: Effective date, full Employer entity details, and Employee legal name and residency.
3. SECTION 1 - APPOINTMENT & DESIGNATION: Job title, reporting manager, primary work location, and standard working hours.
4. SECTION 2 - PROBATION & PERFORMANCE: Probationary period duration and evaluation criteria.
5. SECTION 3 - COMPENSATION, BENEFITS, AND REMUNERATION: Base salary, allowances, annual CTC breakdown, payment frequency, and statutory benefits.
6. SECTION 4 - LEAVE & HOLIDAYS: Paid annual leave, sick leave, and standard company holidays.
7. SECTION 5 - EMPLOYEE DUTIES & CODE OF CONDUCT: Standard diligence, non-disclosure, and compliance rules.
8. SECTION 6 - INTELLECTUAL PROPERTY ASSIGNMENT: Employer ownership of all works, patents, software, and inventions created during employment.
9. SECTION 7 - NON-COMPETE & NON-SOLICITATION: Reasonable post-employment non-solicitation of clients and staff.
10. SECTION 8 - TERMINATION & NOTICE PERIOD: Notice period requirement for both parties, severance, and summary dismissal for cause.
11. SECTION 9 - GOVERNING LAW & JURISDICTION.
12. SIGNATURE BLOCKS: Dual execution blocks for Authorized Employer Signatory and Employee.
""",
    "NDA": """
STRUCTURE REQUIREMENTS:
1. TITLE: Centered bold title "MUTUAL NON-DISCLOSURE AND CONFIDENTIALITY AGREEMENT".
2. PREAMBLE: Date of agreement and clear identification of both Disclosing Party and Receiving Party.
3. SECTION 1 - PURPOSE: Explicit stated business purpose for exchanging proprietary information.
4. SECTION 2 - DEFINITION OF CONFIDENTIAL INFORMATION: Broad yet precise definition covering technical, commercial, financial, and operational data.
5. SECTION 3 - EXCLUSIONS FROM CONFIDENTIALITY: Standard exclusions (publicly known, previously known, independently developed, lawfully obtained).
6. SECTION 4 - OBLIGATIONS & STANDARD OF CARE: Strict duty of confidentiality, restriction to need-to-know representatives.
7. SECTION 5 - COMPELLED DISCLOSURE: Protocol in the event of judicial or regulatory subpoena.
8. SECTION 6 - TERM & SURVIVAL: Duration of agreement and survival period of confidentiality obligations.
9. SECTION 7 - RETURN OR DESTRUCTION OF INFORMATION: Obligation to return or destroy data within a specified window upon written demand.
10. SECTION 8 - REMEDIES & INJUNCTIVE RELIEF: Acknowledgment that monetary damages may be inadequate.
11. SECTION 9 - GOVERNING LAW & JURISDICTION.
12. SIGNATURE BLOCKS: Formal signature blocks for both entities.
""",
    "Non-Disclosure Agreement (NDA)": """
STRUCTURE REQUIREMENTS:
1. TITLE: Centered bold title "MUTUAL NON-DISCLOSURE AND CONFIDENTIALITY AGREEMENT".
2. PREAMBLE: Date of agreement and clear identification of both Disclosing Party and Receiving Party.
3. SECTION 1 - PURPOSE: Explicit stated business purpose for exchanging proprietary information.
4. SECTION 2 - DEFINITION OF CONFIDENTIAL INFORMATION: Broad yet precise definition covering technical, commercial, financial, and operational data.
5. SECTION 3 - EXCLUSIONS FROM CONFIDENTIALITY: Standard exclusions (publicly known, previously known, independently developed, lawfully obtained).
6. SECTION 4 - OBLIGATIONS & STANDARD OF CARE: Strict duty of confidentiality, restriction to need-to-know representatives.
7. SECTION 5 - COMPELLED DISCLOSURE: Protocol in the event of judicial or regulatory subpoena.
8. SECTION 6 - TERM & SURVIVAL: Duration of agreement and survival period of confidentiality obligations.
9. SECTION 7 - RETURN OR DESTRUCTION OF INFORMATION: Obligation to return or destroy data within a specified window upon written demand.
10. SECTION 8 - REMEDIES & INJUNCTIVE RELIEF: Acknowledgment that monetary damages may be inadequate.
11. SECTION 9 - GOVERNING LAW & JURISDICTION.
12. SIGNATURE BLOCKS: Formal signature blocks for both entities.
""",
    "Lease Agreement": """
STRUCTURE REQUIREMENTS:
1. TITLE: Centered bold title "RESIDENTIAL LEASE AGREEMENT".
2. PREAMBLE: Effective date, Landlord details, and Tenant details.
3. SECTION 1 - DEMISED PREMISES: Complete property address, fixtures, and permitted residential use.
4. SECTION 2 - LEASE TERM & COMMENCEMENT: Fixed lease period, commencement date, and renewal procedure.
5. SECTION 3 - RENT & PAYMENT SCHEDULE: Monthly rental amount, monthly due date, payment mode, and late penalty charges.
6. SECTION 4 - SECURITY DEPOSIT: Refundable security deposit amount, deductions terms, and refund timeline after handover.
7. SECTION 5 - UTILITIES & MAINTENANCE: Allocation of electricity, water, society maintenance, and minor repair expenses.
8. SECTION 6 - RESTRICTIONS & PROHIBITIONS: Subletting ban, illegal activities, and structural alterations.
9. SECTION 7 - TERMINATION & NOTICE: Lock-in period, notice requirements for early vacation, and default handling.
10. SECTION 8 - GOVERNING LAW & DISPUTE RESOLUTION.
11. SIGNATURE BLOCKS: Signatures of Landlord, Tenant, and two Witnesses.
""",
    "Service Agreement": """
STRUCTURE REQUIREMENTS:
1. TITLE: Centered bold title "MASTER SERVICES AGREEMENT".
2. PREAMBLE & RECITALS: Client, Service Provider, and background context.
3. SECTION 1 - SERVICES & STATEMENTS OF WORK (SOW).
4. SECTION 2 - PERFORMANCE STANDARDS & DELIVERABLES.
5. SECTION 3 - PRICING, INVOICING, AND PAYMENT TERMS.
6. SECTION 4 - INTELLECTUAL PROPERTY RIGHTS.
7. SECTION 5 - CONFIDENTIALITY & DATA PROTECTION.
8. SECTION 6 - INDEMNIFICATION & LIMITATION OF LIABILITY.
9. SECTION 7 - TERM AND TERMINATION.
10. SECTION 8 - GOVERNING LAW & JURISDICTION.
11. SIGNATURE BLOCKS: Signatures for Authorized Representatives.
""",
    "Offer Letter": """
STRUCTURE REQUIREMENTS:
1. FORMAL LETTERHEAD & DATE.
2. CANDIDATE ADDRESS & FORMAL SALUTATION.
3. POSITION OFFERED, DEPARTMENT, AND REPORTING STRUCTURE.
4. COMMENCEMENT DATE & WORK LOCATION.
5. COMPENSATION BREAKDOWN (Base, Allowances, Performance Bonus, Total CTC).
6. BENEFITS, MEDICAL COVERAGE, AND VACATION POLICY.
7. CONTINGENCIES (Background check, reference verification, documentation).
8. ACCEPTANCE DEADLINE & SIGNING INSTRUCTIONS.
9. COMPANY SIGN-OFF AND CANDIDATE ACCEPTANCE COUNTERSIGNATURE BLOCK.
""",
    "General Agreement": """
STRUCTURE REQUIREMENTS:
1. TITLE: Centered bold title of agreement.
2. PREAMBLE & RECITALS.
3. SECTION 1 - PURPOSE & SCOPE.
4. SECTION 2 - RIGHTS & MUTUAL OBLIGATIONS.
5. SECTION 3 - CONSIDERATION & FINANCIAL TERMS (IF APPLICABLE).
6. SECTION 4 - REPRESENTATIONS & WARRANTIES.
7. SECTION 5 - TERM & TERMINATION.
8. SECTION 6 - GENERAL PROVISIONS (Severability, Entire Agreement, Amendments, Force Majeure).
9. SECTION 7 - GOVERNING LAW & JURISDICTION.
10. SIGNATURE BLOCKS: Dual execution blocks.
""",
}


def build_legal_prompt(
    document_type: str,
    parties: str,
    terms: str,
    effective_date: str,
    additional_details: str = ""
) -> str:
    """
    Constructs a de-clustered, highly readable, structured legal prompt.
    """
    doc_type_guidelines = DOCUMENT_SPECIFIC_INSTRUCTIONS.get(
        document_type,
        "Ensure standard legal contract structure with Preamble, Covenants, Consideration, Term, Termination, Governing Law, and Signatures."
    )

    additional_section = (
        f"\nSPECIAL CLAUSES & USER SPECIFICATIONS:\n{additional_details}\n"
        if additional_details and additional_details.strip()
        else ""
    )

    prompt = f"""You are a senior legal drafting counsel.
Generate a complete, professionally formatted, ready-to-customize draft legal document.

DOCUMENT METADATA:
- DOCUMENT TYPE: {document_type}
- PARTIES: {parties}
- KEY TERMS & COVENANTS: {terms}
- EFFECTIVE DATE: {effective_date}
{additional_section}
{doc_type_guidelines}

STRICT DE-CLUSTERING & FORMATTING RULES:
1. STRICT PROHIBITION ON HTML: Do NOT use ANY HTML tags (such as <b>, <center>, <br>, <p>, <div>, <span>). Use standard markdown headers (# for Title, ## for Section) or clean plain text ONLY.
2. PREVENT CLUSTERED TEXT: Leave double blank lines between every major Article/Section. Use clean paragraph breaks for sub-clauses.
3. HIERARCHICAL HEADINGS:
   - Use uppercase bold headings for main sections (e.g., "## SECTION 1. DEFINITIONS AND INTERPRETATION").
   - Use numbered sub-clauses (e.g., "1.1", "1.2", "(a)", "(b)").
4. RECITALS: Use clear "WHEREAS" clauses to establish context.
5. INTEGRATE ALL USER TERMS: Embed all supplied parties, compensation amounts, durations, notice periods, and covenants into clear legal drafting.
6. NO INVENTED FACTS: Where specific administrative data (such as bank account numbers or corporate registration numbers) is not supplied by the user, use clear brackets like [Insert Registration Number] or [Insert City/State].
7. PROFESSIONAL SIGNATURE GRID: End with a clean, formal execution section with lines for:
   - Entity / Party Name
   - By: ________________________ (Signature)
   - Name: [Authorized Person Name]
   - Title: [Designation/Title]
   - Date: ______________________
8. DIRECT CONTENT ONLY: Return ONLY the final legal document text. Do NOT include conversational commentary (e.g. "Here is your document:").
"""
    return prompt.strip()
