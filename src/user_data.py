"""
====================================================================
CONFIDENTIAL - RESTRICTED CUSTOMER PII DATABASE SAMPLE
CLASSIFICATION: RESTRICTED / GDPR & CCPA REGULATED
DO NOT EXPORT, COPY, OR EXPOSE TO PUBLIC REPOSITORIES
====================================================================
"""

from typing import List, Dict

# Mock Customer records used for testing payment settlement flows.
# These records trigger DLP pattern detectors for SSN, Email, Phone, and Credit Card.
MOCK_CUSTOMER_DATA: List[Dict[str, str]] = [
    {
        "customer_id": "CUST-10029",
        "full_name": "Alice Montgomery",
        "email": "alice.montgomery@example-corp.com",
        "phone": "+1-555-019-2834",
        "national_id_ssn": "123-45-6789",
        "credit_card_pan": "4111-2222-3333-4444",
        "billing_address": "742 Evergreen Terrace, Springfield, OR 97477",
        "account_balance": "$142,500.00"
    },
    {
        "customer_id": "CUST-10030",
        "full_name": "Bob Henderson",
        "email": "bob.henderson@enterprise-client.net",
        "phone": "+1-555-014-9876",
        "national_id_ssn": "987-65-4321",
        "credit_card_pan": "5500-0000-0000-0004",
        "billing_address": "123 Market Street, Suite 400, San Francisco, CA 94105",
        "account_balance": "$85,230.50"
    },
    {
        "customer_id": "CUST-10031",
        "full_name": "Carolyn Vance",
        "email": "carolyn.vance@vance-holdings.org",
        "phone": "+1-555-017-3456",
        "national_id_ssn": "456-78-1234",
        "credit_card_pan": "3782-822463-10005",
        "billing_address": "88 Pine Boulevard, New York, NY 10005",
        "account_balance": "$310,000.00"
    }
]

def get_customer_by_id(customer_id: str) -> Dict[str, str]:
    for cust in MOCK_CUSTOMER_DATA:
        if cust["customer_id"] == customer_id:
            return cust
    raise ValueError(f"Customer {customer_id} not found.")
