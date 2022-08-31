from flask import Flask, render_template
from question_class import QuestionFactory
from dotenv import load_dotenv
from models import route_unpacking, route_unpacking_commas, route_unpacking_dollars, route_unpacking_fractions
from mongo_interface_component import MongoDB


load_dotenv()
APP = Flask(__name__)

db = MongoDB("gmat_data")
questions = db.read("questions")


@APP.route('/')
def home():
    return render_template("home.html", disabled=False)


@APP.route("/reset")
def reset():
    # DB.drop_all()
    # DB.create_all()
    db.delete("questions", {})
    return render_template('home.html', title='Reset DB')


@APP.route("/about")
def about():
    return render_template("about.html", disabled=False)


@APP.route("/question1", methods=['POST', 'GET'])
def question1():
    output = route_unpacking(QuestionFactory(1).no_of_primes(), q_number=1)
    return output


@APP.route("/question2", methods=['POST', 'GET'])
def question2():
    output = route_unpacking_commas(QuestionFactory(2).sum_of_first_n_numbers(), q_number=2)
    return output


@APP.route("/question3", methods=['POST', 'GET'])
def question3():
    output = route_unpacking_fractions(QuestionFactory(3).mf_rat_ratio(), q_number=3)
    return output


@APP.route("/question4", methods=['POST', 'GET'])
def question4():
    output = route_unpacking(QuestionFactory(4).age_diff(), q_number=4)
    return output


@APP.route("/question5", methods=['POST', 'GET'])
def question5():
    output = route_unpacking_dollars(QuestionFactory(5).jacket_profit(), q_number=5)
    return output


@APP.route("/question6", methods=['POST', 'GET'])
def question6():
    output = route_unpacking(QuestionFactory(6).work_time(), q_number=6)
    return output


@APP.route("/question7", methods=['POST', 'GET'])
def question7():
    output = route_unpacking(QuestionFactory(7).percent_solution(), q_number=7)
    return output


@APP.route("/question8", methods=['POST', 'GET'])
def question8():
    output = route_unpacking_fractions(QuestionFactory(8).original_solution(), q_number=8)
    return output


@APP.route("/contact")
def contact():
    return render_template("contact.html", disabled=True)


if __name__ == '__main__':
    APP.run(debug=True)
