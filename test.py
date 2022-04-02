from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/xyz',methods=['GET','POST'])
def test():
   if request.method == 'POST':
       a = request.json['num1']
       b = request.json['num2']
       result = a+b
       return jsonify(str(result))


@app.route('/abc/sudh',methods=['GET','POST'])
def test1():
    if request.method == 'POST':
       a = request.json['num3']
       b = request.json['num4']
       result = a+b
       return jsonify(str(result))

@app.route('/abc/sudh/kumar',methods=['GET','POST'])
def test2():
    if request.method == 'POST':
       a = request.json['num5']
       b = request.json['num6']
       result = a+b
       return jsonify(str(result))

@app.route('/abc/xyz',methods=['GET','POST'])
def test3():
    if request.method == 'POST':
       a = request.json['num7']
       b = request.json['num8']
       result = a+b
       return jsonify(str(result))

@app.route('/faiz/xyz',methods=['GET','POST'])
def test4():
    if request.method == 'POST':
       a = request.json['num9']
       b = request.json['num10']
       result = a+b
       return jsonify(str(result))

if __name__ == '__main__':
    app.run()
