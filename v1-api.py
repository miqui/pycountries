from flask import Flask, Response
import os
import json

app = Flask(__name__)
port = int(os.getenv("PORT",'8000'))

@app.route('/')
def root():
    data = {
        'About':'REST API about countries (python version)',
        'ver': '1.0.0',
        'get all countries': '/rest/v1/all',
        'swagger': '/rest/v1/swagger.json'
    }
    js = json.dumps(data)
    return Response(js, status=200, mimetype='application/json')

@app.route('/rest/v1/swagger.json',  methods = ['GET'])
def get_api_spec():
    try:
        spec_data = json.loads(open('./swagger.json').read())
        js = json.dumps(spec_data)
        return Response(js, status=200, mimetype='application/json')

    except IOError as err:
        msg = json.dumps({'msg': err})
        Response(msg, status=500, mimetype='application/json')

@app.route('/rest/v1/all', methods = ['GET'])
def get_all():
    try:
        data = json.loads(open('./countriesV1.json').read())
        js = json.dumps(data)

        return Response(js, status=200, mimetype='application/json')

    except IOError as err:
        #logger.warn(arg)
        msg = json.dumps({'msg': err})
        Response(msg, status=500, mimetype='application/json')
    except Exception as ex:
        msg = json.dumps({'msg': ex})
        Response(msg, status=500, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
