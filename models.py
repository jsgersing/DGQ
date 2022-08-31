from typing import Optional, Union, Any

from flask import render_template, request

from mongo_interface_component import MongoDB
from bson import ObjectId

from question_class import QuestionFactory

db = MongoDB("gmat_data")


def route_unpacking(question: Optional[Any], q_number: int) -> Optional[str]:
    test_data = {"correct": question.correct,
                 "stem": question.question_stem, "a": question.ac_list[0],
                 "b": question.ac_list[1], "c": question.ac_list[2],
                 "d": question.ac_list[3], "e": question.ac_list[4]}
    if request.method == 'GET':
        db.create("questions", test_data)
        created = db.read("questions", test_data)
        _id = created[0].get("_id")
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem, a=question.ac_list[0],
            b=question.ac_list[1], c=question.ac_list[2], d=question.ac_list[3],
            e=question.ac_list[4], _id=_id, q_number=q_number)
    if request.method == 'POST':
        answer = request.values.get('Answer').upper()
        token = request.values.get('_id')
        token = ObjectId(token)
        db_answer = db.read("questions", {"_id": token})
        if answer != db_answer[0].get("correct"):
            response = "Incorrect"
            return render_template(
                "generic_incorrect.html", disabled=False, stem=db_answer[0].get("stem"), a=db_answer[0].get("a"),
                b=db_answer[0].get("b"), c=db_answer[0].get("c"), d=db_answer[0].get("d"),
                e=db_answer[0].get("e"), response=response, db_answer=db_answer[0].get("correct"), q_number=q_number)
        else:
            response = "CORRECT!"
            db.create("questions", test_data)
            created = db.read("questions", test_data)
            _id = created[0].get("_id")
            return render_template("generic_question.html", disabled=False, stem=question.question_stem,
                                   a=question.ac_list[0],
                                   b=question.ac_list[1],
                                   c=question.ac_list[2],
                                   d=question.ac_list[3],
                                   e=question.ac_list[4], response=response, _id=_id, q_number=q_number)


def route_unpacking_commas(question: QuestionFactory.sum_of_first_n_numbers(), q_number: int) -> Optional[str]:
    test_data = {"correct": question.correct,
                 "stem": question.question_stem, "a": question.ac_list[0],
                 "b": question.ac_list[1], "c": question.ac_list[2],
                 "d": question.ac_list[3], "e": question.ac_list[4]}
    if request.method == 'GET':
        db.create("questions", test_data)
        created = db.read("questions", test_data)
        _id = created[0].get("_id")
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem,
            a="{:,}".format(question.ac_list[0]),
            b="{:,}".format(question.ac_list[1]),
            c="{:,}".format(question.ac_list[2]), d="{:,}".format(question.ac_list[3]),
            e="{:,}".format(question.ac_list[4]), _id=_id, q_number=q_number)
    if request.method == 'POST':
        answer = request.values.get('Answer').upper()
        token = request.values.get('_id')
        token = ObjectId(token)
        db_answer = db.read("questions", {"_id": token})
        if answer != db_answer[0].get("correct"):
            response = "Incorrect"
            return render_template(
                "generic_incorrect.html", disabled=False, stem=db_answer[0].get('stem'),
                a="{:,}".format(int(db_answer[0].get('a'))),
                b="{:,}".format(int(db_answer[0].get('b'))),
                c="{:,}".format(int(db_answer[0].get('c'))),
                d="{:,}".format(int(db_answer[0].get('d'))),
                e="{:,}".format(int(db_answer[0].get('e'))),
                response=response, db_answer=db_answer[0].get("correct"), q_number=q_number)
        else:
            response = "CORRECT!"
            db.create("questions", test_data)
            created = db.read("questions", test_data)
            _id = created[0].get("_id")
            return render_template("generic_question.html", disabled=False, stem=question.question_stem,
                                   a="{:,}".format(question.ac_list[0]),
                                   b="{:,}".format(question.ac_list[1]), c="{:,}".format(question.ac_list[2]),
                                   d="{:,}".format(question.ac_list[3]), e="{:,}".format(question.ac_list[4]),
                                   response=response, _id=_id, q_number=q_number)


def route_unpacking_dollars(question: QuestionFactory.jacket_profit(), q_number: int) -> Optional[str]:
    test_data = {"correct": question.correct,
                 "stem": question.question_stem, "a": question.ac_list[0],
                 "b": question.ac_list[1], "c": question.ac_list[2],
                 "d": question.ac_list[3], "e": question.ac_list[4]}
    if request.method == 'GET':
        db.create("questions", test_data)
        created = db.read("questions", test_data)
        _id = created[0].get("_id")
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem,
            a="${:,.2f}".format(question.ac_list[0]),
            b="${:,.2f}".format(question.ac_list[1]), c="${:,.2f}".format(question.ac_list[2]),
            d="${:,.2f}".format(question.ac_list[3]),
            e="${:,.2f}".format(question.ac_list[4]), _id=_id, q_number=q_number)
    if request.method == 'POST':
        answer = request.values.get('Answer').upper()
        token = request.values.get('_id')
        token = ObjectId(token)
        db_answer = db.read("questions", {"_id": token})
        if answer != db_answer[0].get("correct"):
            response = "Incorrect"
            return render_template(
                "generic_incorrect.html", disabled=False, stem=db_answer[0].get('stem'),
                a="${:,.2f}".format(float(db_answer[0].get('a'))),
                b="${:,.2f}".format(float(db_answer[0].get('b'))),
                c="${:,.2f}".format(float(db_answer[0].get('c'))),
                d="${:,.2f}".format(float(db_answer[0].get('d'))),
                e="${:,.2f}".format(float(db_answer[0].get('e'))),
                response=response, db_answer=db_answer[0].get("correct"), q_number=q_number)
        else:
            response = "CORRECT!"
            db.create("questions", test_data)
            created = db.read("questions", test_data)
            _id = created[0].get("_id")
            return render_template("generic_question.html", disabled=False, stem=question.question_stem,
                                   a="${:,.2f}".format(question.ac_list[0]),
                                   b="${:,.2f}".format(question.ac_list[1]),
                                   c="${:,.2f}".format(question.ac_list[2]),
                                   d="${:,.2f}".format(question.ac_list[3]),
                                   e="${:,.2f}".format(question.ac_list[4]),
                                   repsonse=response, _id=_id, q_number=q_number)


def route_unpacking_fractions(question: QuestionFactory.mf_rat_ratio(), q_number: int) -> Optional[str]:
    test_data = {"correct": question.correct,
                 "stem": str(question.question_stem), "a": str(question.ac_list[0]),
                 "b": str(question.ac_list[1]), "c": str(question.ac_list[2]),
                 "d": str(question.ac_list[3]), "e": str(question.ac_list[4])}
    if request.method == 'GET':
        db.create("questions", test_data)
        created = db.read("questions", test_data)
        _id = created[0].get("_id")
        return render_template(
            "generic_question.html", disabled=False, stem=question.question_stem, a=question.ac_list[0],
            b=question.ac_list[1], c=question.ac_list[2], d=question.ac_list[3],
            e=question.ac_list[4], _id=_id, q_number=q_number)
    if request.method == 'POST':
        answer = request.values.get('Answer').upper()
        token = request.values.get('_id')
        token = ObjectId(token)
        db_answer = db.read("questions", {"_id": token})
        if answer != db_answer[0].get("correct"):
            response = "Incorrect"
            return render_template(
                "generic_incorrect.html", disabled=False, stem=db_answer[0].get('stem'), a=db_answer[0].get('a'),
                b=db_answer[0].get('b'), c=db_answer[0].get('c'), d=db_answer[0].get('d'),
                e=db_answer[0].get('e'), response=response, db_answer=db_answer[0].get("correct"), q_number=q_number)
        else:
            response = "CORRECT!"
            db.create("questions", test_data)
            created = db.read("questions", test_data)
            _id = created[0].get("_id")
            return render_template("generic_question.html", disabled=False, stem=question.question_stem,
                                   a=question.ac_list[0],
                                   b=question.ac_list[1],
                                   c=question.ac_list[2],
                                   d=question.ac_list[3],
                                   e=question.ac_list[4],
                                   response=response, _id=_id, q_number=q_number)
