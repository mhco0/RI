from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'a1Awef3iLlu3Fgfw238Fli32lgD42pRo'


@app.route('/')
def home():
    return render_template('home.html', searches=session.keys())


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        return request.form['language']
    else:
        return redirect(url_for('home'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
