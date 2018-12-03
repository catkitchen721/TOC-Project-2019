import json
import sys
sys.path.append('home/TOC-Project-2019/demo_example')
from bottle import route, run, request
from send_msg import send_text_message

@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('REQUEST BODY: ')
    print(json.dumps(body, indent=2))
    send_back_id = body.get('entry')[0].get('messaging')[0].get('sender').get('id')
    get_text = body.get('entry')[0].get('messaging')[0].get('message').get('text')

    if(get_text == 'help'):
        send_text_message(send_back_id, "->help: \nYou can input some command.")
    else:
        send_text_message(send_back_id, get_text)

run(host="localhost", port=5000, debug=True)
