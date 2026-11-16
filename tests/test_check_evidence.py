from scripts.check_evidence import validate


def test_complete_case():
    case = {
        "document_reference": "T-1",
        "supplier": "Test Supplier",
        "invoice_total": 10.0,
        "settled_amount": 5.0,
        "open_balance": 5.0,
        "purchase_order": "PO-1",
        "assigned_lead": "lead@example.com",
    }
    assert validate(case) == []


def test_missing_evidence():
    assert "purchase_order" in validate({"document_reference": "T-1"})
