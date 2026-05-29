from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/produkt/<int:id>')
def vis_produkt(id):
    return f'Du ser på produkt nummer {id}'

@app.route('/login')
def login_side():
    return render_template_string('''
        <form action="/login" method="POST">
            <input type="text"     name="username" placeholder="Brukernavn">
            <input type="password" name="password" placeholder="Passord">
            <button type="submit">Logg inn</button>
        </form>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form.get('password')
    
    return f"Logging in {username}..."

if __name__ == '__main__':
    app.run(debug=True)