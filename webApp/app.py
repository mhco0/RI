from flask import Flask, render_template, session, request, redirect, url_for
from mutual_information import MutualInformation
from utils import Utils
from time import process_time
import random
from ranking import Ranker

app = Flask(__name__)
app.secret_key = 'a1Aw04f3iLlu3Fgfw238Fli32lgD42pRo'

results_dict = Utils.readJsonFile('./results.json')
ranker = Ranker()


@app.route('/')
def home():
    return render_template('home.html', searches=session)


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        t1_start = process_time()
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

        # ranking = [random.randint(0, 199) for x in range(10)]
        ranking = ranker.score_tfidf(user_search)

        results = []
        for id in ranking[0:5]:
            results.append(results_dict[str(id)])

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

        t1_stop = process_time()
        total_time = t1_stop-t1_start
        print("Elapsed time to process results in seconds:", total_time)
        return render_template('results.html', recommendations=recommendations, results=results, qtd=len(ranking), time=total_time)
    else:
        return redirect(url_for('home'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
