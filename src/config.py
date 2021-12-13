import os
from dataclasses import dataclass


@dataclass
class Config:
    AWS_ID = os.getenv("aws_access_key_id")
    AWS_KEY = os.getenv("aws_secret_access_key")
    SYSTEM_EMAIL_USER = os.getenv("SYSTEM_EMAIL_USER")  # put in aws secrets
    SYSTEM_EMAIL_PASSWD = os.getenv("SYSTEM_EMAIL_PASSWD")  # put in aws secrets
    REGION_NAME = os.getenv("REGION_NAME", "us-east-1")
    CONN_STR = "host='{0}' dbname='{1}' user='{2}' password='{3}' port='{4}' sslmode='disable'"
    DB_COLS = ["person_name", "person_email"]
