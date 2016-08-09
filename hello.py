from itty import get,post, run_itty
import json

@post('/index.json')
def index(request):
    print json.loads(request.body.read())
    #print sd

    return 'Hello World!'

    #for key in res:
        
      # mess = res["salut"]
    

run_itty(server='wsgiref', host='localhost', port=8003)

cxxcv
