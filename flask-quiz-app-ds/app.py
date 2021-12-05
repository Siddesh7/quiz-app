from flask import Flask, render_template, request
from main import *
app = Flask(__name__)


@app.route('/')
def index():
    key = list(s.keys())
    return render_template('index.html', q=key, o=questions)


@app.route('/results', methods=['POST'])
def quiz_answers():
    correct = 0
    wrong = 0
    t = []
    for i in questions.keys():
        answer = request.form[i]
        if answer in ans:
            correct = correct+1
            t.append(answer)
        else:
            wrong = wrong + 1
    return render_template('a.html', res='Correct Answers: '+str(correct), c=correct, w=wrong)


if __name__ == "__main__":
    app.debug = True
    app.run()
