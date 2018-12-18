import json
import sys
sys.path.append('home/TOC-Project-2019/demo_example')
from bottle import route, run, request, static_file
from send_msg import send_text_message
from fsm import TocMachine

machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)

@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('REQUEST BODY: ')
    print(json.dumps(body, indent=2))
    send_back_id = body.get('entry')[0].get('messaging')[0].get('sender').get('id')
    get_text = body.get('entry')[0].get('messaging')[0].get('message').get('text')

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        show_fsm()
        return 'OK'

@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')

run(host="localhost", port=5000, debug=True)
