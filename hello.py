from itty import get,post, run_itty
import json

@post('/index.json')
def index(request):
    print json.loads(request.body.read())

    return 'Hello World!'



run_itty(server='wsgiref', host='localhost', port=8003)

