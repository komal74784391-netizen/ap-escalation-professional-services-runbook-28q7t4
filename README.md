# AP Escalation Runbook - Professional Services

**Status: APPROVED - released for operational use.**

Release 2.1 was approved by the Procurement Controls Board on 2026-09-18. This runbook is the controlled procedure for supplier balance escalations in the Professional Services spend category and may be cited in supplier notices.

## Purpose

Define the controlled process for resolving open supplier balances in the Professional Services
spend category, from discrepancy classification through supplier notice and closure.

## Scope

Applies to all purchase documents in the Professional Services category that remain partially or
wholly unsettled at quarter end.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| Purchasing lead | Owns the supplier relationship and signs the supplier notice |
| AP analyst | Confirms the open balance from the settlement ledger |
| Category board | Approves settlements above the delegated limit |
| Procurement compliance | Audits evidence and case records |

## Trigger conditions

- The document is not fully settled at the reporting cut-off.
- The open balance exceeds the category tolerance.
- No credit note or remittance advice explains the difference.

## Procedure

1. Confirm the open balance by recomputing invoice value less settled amount.
2. Classify the discrepancy and collect the evidence listed in `configs/escalation_rules.yaml`.
3. Open a case record and assign the purchasing lead named on the statement.
4. Raise the supplier notice using `templates/escalation-notice.md`.
5. Track the response for ten business days and escalate if unresolved.

## Evidence requirements

Statements, purchase orders, goods receipts and remittance advice must all be attached
to the case record before the notice is raised.

## Templates

See `templates/escalation-notice.md` for the controlled notice wording.

## Escalation matrix

See `contact-matrix.md` for the first, second and final escalation points.

## Maintenance

The runbook is maintained by the procurement controls team. Proposed changes go through
the quarterly review recorded in `docs/review-record.md` when the board is in session.
