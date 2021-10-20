from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Task 1.</h2>'

@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('product.json')
app.run(host='0.0.0.0', port=81)

if __name__=="__main__":
    app.run(debug=True)