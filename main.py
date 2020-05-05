from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from sim import get_response

app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():
    print(request)
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(get_response(incoming_msg))
    return str(resp)


if __name__ == "__main__":
    app.run()
