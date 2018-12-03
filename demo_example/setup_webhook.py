from bottle import route, run, request
import os


VERIFY_TOKEN = os.environ.get("ACCESS_TOKEN")


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

run(host="localhost", port=5000, debug=True)
