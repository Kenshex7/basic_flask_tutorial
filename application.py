from flask import Flask, request, jsonify
import json
app = Flask(__name__)

un_arreglo = ['Cosa0', 'Cosa1', 'Cosa2', 'Cosa3']

@app.route('/')
def hello_world():
   return 'Hello world'

@app.route('/', methods=['POST'])
def un_post():
    try:
        res = json.loads(request.get_data())
        print(res)
        res['un_campo'] = "Soy un nuevo campo"
        return jsonify(res)
    except Exception as e:
        print(e)

@app.route('/<una_variable>', methods=['GET'])
def un_get_con_variable(una_variable):
    return jsonify({'un_elemento': un_arreglo[int(una_variable)]})

if __name__ == '__main__':
   app.run()