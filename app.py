from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/produkt/<int:id>')
def vis_produkt(id):
    return f'Du ser på produkt nummer {id}'

if __name__ == '__main__':
    app.run(debug=True)