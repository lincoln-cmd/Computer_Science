from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/get', methods = ['GET'])
def get_exam():
    name = request.args.get('name')
    age = request.args.get('age')
    
    return name + "-" + age

@app.route('/post', methods = ['POST'])
def post_example():
    data = json.loads(request.data)
    name = data['name']
    age = data['age']
    
    return name + "-" + age

if __name__ == "__main__":
    app.run(debug = True, port = 8000)

