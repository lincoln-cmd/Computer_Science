'''
 Flask

 파이썬으로 작성된 웹 프레임워크

 ex)
 from flask import Flask
 app = Flask(__name__)
 
 @app.route("/")
 def hello():
     return "Hello World!"
 
 if __name__ == "__main__":
     app.run()
'''


from flask import Flask
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def hello():
    return "Hello PyWorld!!"

if __name__ == "__main__":
    app.run(debug = True)


'''
 실행법: 앱을 띄워놓은 상태에서 누군가가 앱에 접속시 http를 통해 호출.
즉, 앱을 띄워놓은 상태에서 누군가 URI를 통해 접속해서 get메서드를 사용하면 함수를 호출하여 return값을 반환.

 cmd나 prompt를 통해서 실행 가능.
'''
















