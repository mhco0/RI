from flask import Flask, render_template, session, request, redirect, url_for
from mutual_information import MutualInformation

app = Flask(__name__)
app.secret_key = 'a1Aw04f3iLlu3Fgfw238Fli32lgD42pRo'


@app.route('/')
def home():
    return render_template('home.html', searches=session)


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        author = request.form['author'] if ('author' in
                                            request.form) else ''
        publisher = request.form['publisher'] if ('publisher' in
                                                  request.form) else ''
        language = request.form['language'] if ('language' in
                                                request.form) else ''
        isbn = request.form['isbn'] if ('isbn' in
                                        request.form) else ''
        words = request.form['words'] if ('words' in
                                          request.form) else ''
        user_search = [('author', author), ('publisher', publisher),
                       ('language', language), ('isbn', isbn), ('words', words)]

        if('history' in session):
            session['history'] = [
                (author, publisher, language, isbn, words)] + session['history']
        else:
            session['history'] = [(author, publisher, language, isbn, words)]

        recommendations = {
            'author': MutualInformation.calcMutualInformation(author),
            'publisher': MutualInformation.calcMutualInformation(publisher),
            'words': MutualInformation.calcMutualInformation(words)
        }

        return render_template('results.html', recommendations=recommendations)
    else:
        return redirect(url_for('home'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
