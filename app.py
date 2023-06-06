# Description: Main file for the POS Wrapper
from flask import Flask, request, Response
import json
import posconn

# Error messages
ERROR_INVALID_REQUEST_BODY = {'status': 'failure', 'message': 'POS wrapper: invalid request body', 'code': '100-INVALID_BODY'}
ERROR_CALL_POS_CONN = {'status': 'failure', 'message': 'POS wrapper: error calling POS connector', 'code': '100-INTERNAL_ERROR'}

# Flask app
app = Flask(__name__)

# Set Routes
# Healthcheck
@app.route("/")
def healthcheck():
    return "OK"


# Post payment
@app.route("/pos-conn-wrapper/payment", methods=["POST"])
def post_payment():
    # Get request body
    try:
        reqbdy = request.get_json()
    except:
        # return error
        app.logger.error(json.dumps(ERROR_INVALID_REQUEST_BODY))
        return Response(json.dumps(ERROR_INVALID_REQUEST_BODY), status=500, mimetype="application/json")

    # Call POS Connector
    try:
        resp = posconn.call_payment(reqbdy)
        if resp is None:
            raise Exception(ERROR_CALL_POS_CONN)
    except:
        app.logger.error(json.dumps(ERROR_CALL_POS_CONN))
        return Response(json.dumps(ERROR_CALL_POS_CONN), status=500, mimetype="application/json")

    # Return response
    return resp.json()


# Post payment status
@app.route("/pos-conn-wrapper/payment/status", methods=["POST"])
def post_payment_status():
    # Get request body
    try:
        reqbdy = request.get_json()
    except:
        # return error
        app.logger.error(json.dumps(ERROR_INVALID_REQUEST_BODY))
        return Response(json.dumps(ERROR_INVALID_REQUEST_BODY), status=500, mimetype="application/json")

    # Call POS Connector
    try:
        resp = posconn.call_payment_status(reqbdy)
        if resp is None:
            raise Exception(ERROR_CALL_POS_CONN)
    except:
        app.logger.error(json.dumps(ERROR_CALL_POS_CONN))
        return Response(json.dumps(ERROR_CALL_POS_CONN), status=500, mimetype="application/json")

    # Return response
    return resp.json()


# Post payment refund
@app.route("/pos-conn-wrapper/payment/refund", methods=["POST"])
def post_payment_refund():
    # Get request body
    try:
        reqbdy = request.get_json()
    except:
        # return error
        app.logger.error(json.dumps(ERROR_INVALID_REQUEST_BODY))
        return Response(json.dumps(ERROR_INVALID_REQUEST_BODY), status=500, mimetype="application/json")

    # Call POS Connector
    try:
        resp = posconn.call_payment(reqbdy)
        if resp is None:
            raise Exception(ERROR_CALL_POS_CONN)
    except:
        app.logger.error(json.dumps(ERROR_CALL_POS_CONN))
        return Response(json.dumps(ERROR_CALL_POS_CONN), status=500, mimetype="application/json")

    # Return response
    return resp.json()


# Run flask app
app.run()


