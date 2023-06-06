# Description: Main file for the Kueski POS Wrapper
import posconn
from flask import Flask, request, jsonify, Response


# Flask app
app = Flask(__name__)

# Routes
# Healthcheck
@app.route("/")
def healthcheck():
    return "OK"

# Post payment
@app.route("/kueski-pos-wrapper/payment", methods=["POST"])
def post_payment():
    # Get request body
    reqbdy = request.get_json()
    # Check request body
    if reqbdy == None:
        app.logger.error("Invalid request body")
        return Response("Invalid request body", status=500, mimetype="application/json")

    # Call POS Connector
    resp = posconn.call_post_payment(reqbdy)

    # Check response
    if resp == None:
        app.logger.error("Error in post_payment with order_id: " + reqbdy["order_id"])
        return Response(status=500)

    return Response(resp.data, status=resp.status_code, mimetype=resp.mime_type, headers=resp.headers)

# Post payment status
@app.route("/kueski-pos-wrapper/payment/status", methods=["POST"])
def post_payment_status():
    return jsonify({"hello": "world"})

# Post payment refund
@app.route("/kueski-pos-wrapper/payment/refund", methods=["POST"])
def post_payment_refund():
    return jsonify({"hello": "world"})

# Run flask app
app.run()


