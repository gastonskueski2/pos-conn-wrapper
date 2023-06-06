import hashlib
import hmac


# Function to generate checksum
def get(key, message):
    # convert to bytes
    bkey = bytes(key, 'utf-8')
    bmsg = bytes(message, 'utf-8')

    # create a new HMAC object
    hash = hmac.new(bkey, bmsg, hashlib.sha256)

    # to lowercase hexits
    return hash.hexdigest()
