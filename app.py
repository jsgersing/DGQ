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
    question = Question(1).No_of_Primes()
    q1 = question[0]
    ac_list = question[1]
    a = ac_list[0]
    b = ac_list[1]
    c = ac_list[2]
    d = ac_list[3]
    e = ac_list[4]
    return render_template(
        "question1.html", disabled=False, message1=q1, message2=a, message3=b, message4=c, message5=d, message6=e)


@APP.route("/question2", methods=['POST', 'GET'])
def question2():
    question = Question(2).sum_of_first_n_numbers()
    q2 = question[0]
    ac_list = question[1]
    a = ac_list[0]
    b = ac_list[1]
    c = ac_list[2]
    d = ac_list[3]
    e = ac_list[4]
    return render_template(
        "question2.html", disabled=False, message1=q2, message2=a, message3=b, message4=c, message5=d, message6=e)


@APP.route("/question3", methods=['POST', 'GET'])
def question3():
    question = Question(3).mf_rat_ratio()
    q3 = question[0]
    ac_list = question[1]
    a = ac_list[0]
    b = ac_list[1]
    c = ac_list[2]
    d = ac_list[3]
    e = ac_list[4]
    return render_template(
        "question3.html", disabled=False, message1=q3, message2=a, message3=b, message4=c, message5=d, message6=e)


@APP.route("/question4", methods=['POST', 'GET'])
def question4():
    question = Question(4).age_diff()
    q4 = question[0]
    ac_list = question[1]
    a = ac_list[0]
    b = ac_list[1]
    c = ac_list[2]
    d = ac_list[3]
    e = ac_list[4]
    return render_template(
        "question4.html", disabled=False, message1=q4, message2=a, message3=b, message4=c, message5=d, message6=e)


@APP.route("/contact")
def contact():
    return render_template("contact.html", disabled=True)


if __name__ == '__main__':
    APP.run(debug=True)
