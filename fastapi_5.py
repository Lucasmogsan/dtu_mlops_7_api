from fastapi import FastAPI
from http import HTTPStatus
import re
from pydantic import BaseModel




app = FastAPI()

# Check for specific email domains
domains = ['gmail', 'hotmail', 'yahoo', 'outlook', 'icloud', 'mail']

# Create class for the input data
class Email(BaseModel):
    email: str
    domain_match: str


@app.get("/text_model/")
def contains_email(data: Email):
    regex = r'\b[A-Za-z0-9._%+-]+@(' + '|'.join(re.escape(domain) for domain in domains) + r')\.(dk|com|net)\b'
    response = {
        "input": data,
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "acceptable_domain": re.fullmatch(regex, data.email) is not None,
        "email_contains_domain_match": data.domain_match in data.email
    }
    return response


# Tested with:
# http://localhost:8000/docs
# OR:
# curl -X 'GET' \
#   'http://localhost:8000/text_model/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#     "email": "mlops@gmail.com",
#     "domain_match": "gmail"
# }'