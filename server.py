from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'any string you want'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')

@app.route('/up')
def up():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)