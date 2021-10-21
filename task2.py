# from types import MethodType
import json
from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    value = {"key":request.json['key']}

    with open('./templates/product.json','r+') as file:
        file_data = json.load(file)
        file_data.append(value)
        file.seek(0)
        json.dump(file_data,file,indent=4)
    return value

# app.run(host='0.0.0.0', port=81)

if __name__=="__main__":
    app.run(debug=True)