"""
CONFIDENTIAL - COMPANY INTERNAL USE ONLY
File: config.py
Module: Core Service Configuration
"""

import os
from dataclasses import dataclass

@dataclass
class AppConfig:
    # Environment & Service Identification
    ENV: str = "production-internal"
    SERVICE_NAME: str = "internal-payments-core"
    
    # Internal Database Credentials (Sensitive)
    DB_HOST: str = "prod-db-cluster.internal.corp.local"
    DB_PORT: int = 5432
    DB_NAME: str = "corp_financial_prod"
    DB_USER: str = "svc_payment_admin"
    DB_PASSWORD: str = "CorpSecret_2026_SecureP@ssw0rd!"
    DATABASE_URL: str = "postgresql://svc_payment_admin:CorpSecret_2026_SecureP@ssw0rd!@prod-db-cluster.internal.corp.local:5432/corp_financial_prod"

    # Cloud Storage & Infrastructure Keys (Mocked for DLP Demo)
    AWS_ACCESS_KEY_ID: str = "AKIAIOSFODNN7DEMO26K"
    AWS_SECRET_ACCESS_KEY: str = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY2026"
    AWS_DEFAULT_REGION: str = "us-east-1"
    
    # Internal JWT Authentication Secret
    JWT_SIGNING_SECRET: str = "super-secret-internal-jwt-signing-key-9f8e7d6c5b4a3210"

config = AppConfig()
