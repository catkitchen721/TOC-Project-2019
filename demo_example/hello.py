from bottle import route, run


@route('/message')
def hello():
    return ("\n"
            "    <!DOCTYPE HTML>\n"
            "    <head>\n"
            "	    <title>Test Page</title>\n"
            "    </head>\n"
            "    <body>\n"
            "	    <p>sample page</p>\n"
            "    </body>\n"
            "    ")

run(host='localhost', port=8080, debug=True)
