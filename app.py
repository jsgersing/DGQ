from flask import Flask, render_template
from helper_class import Question

APP = Flask(__name__)


@APP.route('/')
def home():
    return render_template("home.html", disabled=False)


@APP.route("/about")
def about():
    return render_template("about.html", disabled=False)


@APP.route("/question1", methods=['POST', 'GET'])
def question1():
    question = Question(1)
    q1 = question.No_of_Primes()
    return render_template("question1.html", disabled=False, message1=q1)


@APP.route("/question2", methods=['POST', 'GET'])
def question2():
    question = Question(2)
    q2 = question.sum_of_first_n_numbers()
    return render_template("question2.html", disabled=False, message2=q2)


@APP.route("/question3", methods=['POST', 'GET'])
def question3():
    question = Question(3)
    q3 = question.mf_rat_ratio()
    return render_template("question3.html", disabled=False, message3=q3)


@APP.route("/question4", methods=['POST', 'GET'])
def question4():
    question = Question(4)
    q4 = question.age_diff()
    return render_template("question4.html", disabled=False, message4=q4)


@APP.route("/contact")
def contact():
    return render_template("contact.html", disabled=True)


if __name__ == '__main__':
    APP.run(debug=True)
