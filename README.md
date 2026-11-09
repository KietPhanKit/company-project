# Internal Financial Core Service (Company Project)

> **CONFIDENTIAL & PROPRIETARY**
> This repository contains internal company code, proprietary business logic, and sensitive test configurations.

---

## DLP Demo Scenarios

This repository can be used to test and demonstrate various Data Loss Prevention (DLP) controls:

1. **Git Push Enforcement (Firewall / Whitelist)**:
   - If your DLP policy allows pushing to `company-project` (authorized internal remote) but blocks pushing to `public-repository` (unauthorized remote).
2. **Clipboard & Copy-Paste Detection**:
   - Copying proprietary source code, secrets, or PII from files in this repository into unauthorized apps (e.g. personal browsers, public chats, external text editors).
3. **Secret Scanning / Token Leaks**:
   - Accidental leak or commit of API keys (AWS keys, Stripe keys, database strings) found in [config.py](file:///Users/kiet.phan/demo/dlp/company-project/config.py) and [.env.secrets.demo](file:///Users/kiet.phan/demo/dlp/company-project/.env.secrets.demo).
4. **Customer PII Exfiltration**:
   - Extracting mock customer data (names, SSNs, credit cards) located in [src/user_data.py](file:///Users/kiet.phan/demo/dlp/company-project/src/user_data.py).

---

## File Overview

- [`config.py`](file:///Users/kiet.phan/demo/dlp/company-project/config.py): Service configuration containing internal API credentials and database connection strings.
- [`.env.secrets.demo`](file:///Users/kiet.phan/demo/dlp/company-project/.env.secrets.demo): Mock environment secrets file formatted for secrets detection.
- [`src/payment_gateway.py`](file:///Users/kiet.phan/demo/dlp/company-project/src/payment_gateway.py): Proprietary payment gateway integration with mock live credentials.
- [`src/user_data.py`](file:///Users/kiet.phan/demo/dlp/company-project/src/user_data.py): Sample customer PII records for data leak testing.
- [`src/risk_engine.py`](file:///Users/kiet.phan/demo/dlp/company-project/src/risk_engine.py): Proprietary fraud risk scoring algorithm.
