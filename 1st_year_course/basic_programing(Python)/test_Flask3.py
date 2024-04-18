import requests
import json

requests.get("http://127.0.0.1:5000/get?name=lincoln&age=20").text

requests.post("http://127.0.0.1:8000/post", data = json.dumps({"name":"Felipe", "age":"22"})).text

# URI가 너무 길어지는 것을 방지하기 위해 post를 사용해서 데이터를 따로 넘겨준다.
