# Description: POS Connector calls
import requests, json
import hashlib, hmac, base64

# Constants
API_KEY = "3ceb0d78-f175-4616-a4b2-e7fd23419262"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
GUEST_ORIGIN = "POS-CONNECTOR / 1.0 python"
URL_POS_CONN = "https://kh36t6agy9.execute-api.us-east-1.amazonaws.com/staging"
URL_PAYMENT = "/pos-connector/payment"
URL_PAYMENT_STATUS = "/pos-connector/payment/status"
URL_PAYMENT_REFUND = "/pos-connector/payment/refund"
ENV_STAGING = "staging"
ENV_PRODUCTION = "production"
CHECKSUM = "pass"


# Function to set headers
def get_checksum(bdy):
    data = bytes(bdy, 'utf-8')
    secret = bytes(API_KEY, 'utf-8')

    hash = hmac.new(secret, data, hashlib.sha256)

    # to lowercase hexits
    return hash.hexdigest()



# Function to set headers
def set_headers(bdy):
    checksum = get_checksum(bdy)

    # build headers
    headers = {
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT,
        "Key": API_KEY,
        "Guest-Origin": GUEST_ORIGIN,
        "Checksum": checksum,
        "Environment": ENV_STAGING
    }

    # return headers
    return headers


# Function to call POS Connector payment endpoint
def call_payment(reqbdy):
    # Convert request body to json
    try:
        bdy = json.dumps(reqbdy)
    except:
        return None

    # Set headers
    headers = set_headers(bdy)

    # Call endpoint
    url = URL_POS_CONN + URL_PAYMENT
    try:
        resp = requests.post(url, headers=headers, data=bdy)
    except:
        return None

    # return endpoint response
    return resp


# Function to call POS Connector payment status endpoint
def call_payment_status(reqbdy):
    # Convert request body to json
    try:
        bdy = json.dumps(reqbdy)
    except:
        return None

    # Set headers
    headers = set_headers(bdy)

    # Call endpoint
    url = URL_POS_CONN + URL_PAYMENT_STATUS
    try:
        resp = requests.post(url, headers=headers, data=bdy)
    except:
        return None

    # return endpoint response
    return resp


# Function to call POS Connector payment refund endpoint
def call_payment_refund(reqbdy):
    # Convert request body to json
    try:
        bdy = json.dumps(reqbdy)
    except:
        return None

    # Set headers
    headers = set_headers(bdy)

    # Call endpoint
    url = URL_POS_CONN + URL_PAYMENT_REFUND
    try:
        resp = requests.post(url, headers=headers, data=bdy)
    except:
        return None

    # return endpoint response
    return resp
