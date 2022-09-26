from flask import Flask, request
from flask_api import status
import json
from Study import add,same
app = Flask(__name__)

@app.route('/')
def greeting():
    return "This is Test API !"


@app.route('/add', methods=['POST']) # 실제 호출할 API 주소  ex - 127.0.0.1:5000/add
def get_add():
    # POST일 때, 아래 함수 호출
    if request.method == 'POST':
        # add 함수는 input 값이 두개를 받아야 함
        a = request.json["a"]
        b = request.json["b"] # 주고받기 편하게 a,b는 json형태로 데이터를 받음
        c = add(a,b) # add함수를 통해서 나온 값을
        result = json.dumps(c) # 다시 json.dumps로 만들어 return

    return result, status.HTTP_200_OK, {"Content-Type": "application/json; charset=utf-8", "Access-Control-Allow-Origin": "*"}
    # API가 제대로 응답하면 200 코드와 함께 result값이 Return

@app.route('/same',methods=['POST'])
def get_same():
    if request.method == 'POST':
        a = request.json["a"]
        b = request.json["b"]
        c = same(a,b)
        result = json.dumps(c)
    return result, status.HTTP_200_OK, {"Content-Type": "application/json; charset=utf-8", "Access-Control-Allow-Origin": "*"}
