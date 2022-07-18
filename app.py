from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from helper_class import QuestionFactory
from os import getenv
from dotenv import load_dotenv

load_dotenv()
APP = Flask(__name__)

APP.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy()
DB.init_app(APP)


class Answers(DB.Model):
    uu = DB.Column(DB.String(), primary_key=True)
    correct = DB.Column(DB.String(), nullable=True)
    stem = DB.Column(DB.String(), nullable=True)
    a = DB.Column(DB.String(), nullable=True)
    b = DB.Column(DB.String(), nullable=True)
    c = DB.Column(DB.String(), nullable=True)
    d = DB.Column(DB.String(), nullable=True)
    e = DB.Column(DB.String(), nullable=True)

    def __init__(self, uu, correct, stem, a, b, c, d, e):
        self.uu = uu
        self.correct = correct
        self.stem = stem
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def __repr__(self):
        return f"Correct: {self.correct}"


APP.app_context().push()
DB.session.commit()


@APP.route('/')
def home():
    return render_template("home.html", disabled=False)


@APP.route("/reset")
def reset():
    # Drop our DB tables
    DB.drop_all()
    # Create tables according to the classes in models.py
    DB.create_all()
    return render_template('home.html', title='Reset DB')


@APP.route("/about")
def about():
    return render_template("about.html", disabled=False)


@APP.route("/question1", methods=['POST', 'GET'])
def question1():
    question = QuestionFactory(1).no_of_primes()
    test_data = Answers(uu=str(question.uuid), correct=question.correct,
                        stem=question.question_stem, a=question.ac_list[0],
                        b=question.ac_list[1], c=question.ac_list[2], d=question.ac_list[3],
                        e=question.ac_list[4])
    if request.method == 'GET':
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem, a=question.ac_list[0],
            b=question.ac_list[1], c=question.ac_list[2], d=question.ac_list[3],
            e=question.ac_list[4], uuid=question.uuid, q_number=1)
    if request.method == 'POST':
        answer = request.values.get('Answer').upper()
        token = request.values.get('uuid')
        db_answer = Answers.query.filter(Answers.uu == token).all()[0]
        if answer != db_answer.correct:
            response = "Incorrect"
            return render_template(
                "generic_incorrect.html", disabled=False, stem=db_answer.stem, a=db_answer.a,
                b=db_answer.b, c=db_answer.c, d=db_answer.d,
                e=db_answer.e, response=response, db_answer=db_answer, q_number=1)
        else:
            response = "CORRECT!"
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem, a=question.ac_list[0],
            b=question.ac_list[1], c=question.ac_list[2], d=question.ac_list[3],
            e=question.ac_list[4], response=response, uuid=question.uuid, q_number=1)


@APP.route("/question2", methods=['POST', 'GET'])
def question2():
    question = QuestionFactory(2).sum_of_first_n_numbers()
    test_data = Answers(uu=str(question.uuid), correct=question.correct,
                        stem=question.question_stem, a=question.ac_list[0],
                        b=question.ac_list[1], c=question.ac_list[2], d=question.ac_list[3],
                        e=question.ac_list[4])
    if request.method == 'GET':
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem,
            a="{:,}".format(question.ac_list[0]),
            b="{:,}".format(question.ac_list[1]),
            c="{:,}".format(question.ac_list[2]), d="{:,}".format(question.ac_list[3]),
            e="{:,}".format(question.ac_list[4]), uuid=question.uuid, q_number=2)
    if request.method == 'POST':
        answer = request.values.get('Answer').upper()
        token = request.values.get('uuid')
        db_answer = Answers.query.filter(Answers.uu == token).one()
        if answer != db_answer.correct:
            response = "Incorrect"
            return render_template(
                "generic_incorrect.html", disabled=False, stem=db_answer.stem, a="{:,}".format(int(db_answer.a)),
                b="{:,}".format(int(db_answer.b)), c="{:,}".format(int(db_answer.c)),
                d="{:,}".format(int(db_answer.d)),
                e="{:,}".format(int(db_answer.e)), response=response, db_answer=db_answer, q_number=2)
        else:
            response = "CORRECT!"
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem,
            a="{:,}".format(question.ac_list[0]),
            b="{:,}".format(question.ac_list[1]), c="{:,}".format(question.ac_list[2]),
            d="{:,}".format(question.ac_list[3]),
            e="{:,}".format(question.ac_list[4]), response=response, uuid=question.uuid, q_number=2)


@APP.route("/question3", methods=['POST', 'GET'])
def question3():
    question = QuestionFactory(3).mf_rat_ratio()
    test_data = Answers(uu=str(question.uuid), correct=question.correct,
                        stem=question.question_stem, a=str(question.ac_list[0]),
                        b=str(question.ac_list[1]), c=str(question.ac_list[2]), d=str(question.ac_list[3]),
                        e=str(question.ac_list[4]))
    if request.method == 'GET':
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem, a=question.ac_list[0],
            b=question.ac_list[1], c=question.ac_list[2], d=question.ac_list[3],
            e=question.ac_list[4], uuid=question.uuid, q_number=3)
    if request.method == 'POST':
        answer = request.values.get('Answer').upper()
        token = request.values.get('uuid')
        db_answer = Answers.query.filter(Answers.uu == token).one()
        if answer != db_answer.correct:
            response = "Incorrect"
            return render_template(
                "generic_incorrect.html", disabled=False, stem=db_answer.stem, a=db_answer.a,
                b=db_answer.b, c=db_answer.c, d=db_answer.d,
                e=db_answer.e, response=response, db_answer=db_answer, q_number=3)
        else:
            response = "CORRECT!"
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem, a=question.ac_list[0],
            b=question.ac_list[1], c=question.ac_list[2], d=question.ac_list[3],
            e=question.ac_list[4], response=response, uuid=question.uuid, q_number=3)


@APP.route("/question4", methods=['POST', 'GET'])
def question4():
    question = QuestionFactory(4).age_diff()
    test_data = Answers(uu=str(question.uuid), correct=question.correct,
                        stem=question.question_stem, a=question.ac_list[0],
                        b=question.ac_list[1], c=question.ac_list[2], d=question.ac_list[3],
                        e=question.ac_list[4])
    if request.method == 'GET':
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem, a=question.ac_list[0],
            b=question.ac_list[1], c=question.ac_list[2], d=question.ac_list[3],
            e=question.ac_list[4], uuid=question.uuid, q_number=4)
    if request.method == 'POST':
        answer = request.values.get('Answer').upper()
        token = request.values.get('uuid')
        db_answer = Answers.query.filter(Answers.uu == token).one()
        if answer != db_answer.correct:
            response = "Incorrect"
            return render_template(
                "generic_incorrect.html", disabled=False, stem=db_answer.stem, a=db_answer.a,
                b=db_answer.b, c=db_answer.c, d=db_answer.d,
                e=db_answer.e, response=response, db_answer=db_answer, q_number=4)
        else:
            response = "CORRECT!"
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem, a=question.ac_list[0],
            b=question.ac_list[1], c=question.ac_list[2], d=question.ac_list[3],
            e=question.ac_list[4], response=response, uuid=question.uuid, q_number=4)


@APP.route("/question5", methods=['POST', 'GET'])
def question5():
    question = QuestionFactory(5).jacket_profit()
    test_data = Answers(uu=str(question.uuid), correct=question.correct,
                        stem=question.question_stem, a=question.ac_list[0],
                        b=question.ac_list[1], c=question.ac_list[2], d=question.ac_list[3],
                        e=question.ac_list[4])
    if request.method == 'GET':
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem,
            a="${:,.2f}".format(question.ac_list[0]),
            b="${:,.2f}".format(question.ac_list[1]), c="${:,.2f}".format(question.ac_list[2]),
            d="${:,.2f}".format(question.ac_list[3]),
            e="${:,.2f}".format(question.ac_list[4]), uuid=question.uuid, q_number=5)
    if request.method == 'POST':
        answer = request.values.get('Answer').upper()
        token = request.values.get('uuid')
        db_answer = Answers.query.filter(Answers.uu == token).one()
        if answer != db_answer.correct:
            response = "Incorrect"
            return render_template(
                "generic_incorrect.html", disabled=False, stem=db_answer.stem, a="${:,.2f}".format(float(db_answer.a)),
                b="${:,.2f}".format(float(db_answer.b)), c="${:,.2f}".format(float(db_answer.c)),
                d="${:,.2f}".format(float(db_answer.d)),
                e="${:,.2f}".format(float(db_answer.e)), response=response, db_answer=db_answer, q_number=5)
        else:
            response = "CORRECT!"
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem,
            a="${:,.2f}".format(question.ac_list[0]),
            b="${:,.2f}".format(question.ac_list[1]), c="${:,.2f}".format(question.ac_list[2]),
            d="${:,.2f}".format(question.ac_list[3]),
            e="${:,.2f}".format(question.ac_list[4]), repsonse=response, uuid=question.uuid, q_number=5)


@APP.route("/contact")
def contact():
    return render_template("contact.html", disabled=True)


if __name__ == '__main__':
    APP.run(debug=True)
