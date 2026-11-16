#!/usr/bin/env python3
"""Validate that an escalation case has the evidence the runbook requires."""

REQUIRED_FIELDS = [
    "document_reference",
    "supplier",
    "invoice_total",
    "settled_amount",
    "open_balance",
    "purchase_order",
    "assigned_lead",
]


def validate(case: dict) -> list:
    missing = [field for field in REQUIRED_FIELDS if not case.get(field)]
    return missing


if __name__ == "__main__":
    sample = {
        "document_reference": "EXAMPLE-0001",
        "supplier": "Example Supplier",
        "invoice_total": 1000.0,
        "settled_amount": 250.0,
        "open_balance": 750.0,
        "purchase_order": "PO-00-0001",
        "assigned_lead": "lead@example.com",
    }
    print("missing fields:", validate(sample))
