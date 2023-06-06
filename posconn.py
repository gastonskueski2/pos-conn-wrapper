import requests
import checksum

# Constants
API_KEY = "12fc8617-2545-48b2-97bf-06642816795e"
MERCHANT_ID = 1234567890
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
GUEST_ORIGIN = "POS-CONNECTOR-WRAPPER / 1.0 python"
POS_CONN_URL = "https://kh36t6agy9.execute-api.us-east-1.amazonaws.com/staging"
PAYMENT_URL = "/pos-connector/payment"
PAYMENT_STATUS_URL = "/pos-connector/payment/status"
PAYMENT_REFUND_URL = "/pos-connector/payment/refund"

def call_post_payment(reqbdy):
    # Calculate checksum
    checksum_str = checksum.get(API_KEY, reqbdy.__str__())

    # Build request
    url = POS_CONN_URL + PAYMENT_URL
    headers = {
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT,
        "Key": API_KEY,
        "Guest-Origin": GUEST_ORIGIN,
        "Checksum": checksum_str
    }
    resp = requests.post(url, headers=headers, data=reqbdy)
    return resp
