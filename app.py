from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/portfolio')
def index():
    return render_template('home.html')

@app.route('/contacts')
def contacts():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8000)