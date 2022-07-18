from random import randint, randrange
from fractions import Fraction
import uuid
import names


def arrange_answer_choices(answer_choices, correct):
    asc_desc = randint(0, 1)
    if asc_desc == 0:
        answer_choices = sorted(answer_choices)
    else:
        answer_choices = (sorted(answer_choices))[::-1]

    choices = ['A', 'B', 'C', 'D', 'E']
    i = 0
    while i < len(answer_choices):
        print(f"{choices[i]}) {answer_choices[i]}")
        i += 1
    if answer_choices[0] == correct:
        correct_letter = 'A'
    elif answer_choices[1] == correct:
        correct_letter = 'B'
    elif answer_choices[2] == correct:
        correct_letter = 'C'
    elif answer_choices[3] == correct:
        correct_letter = 'D'
    else:
        correct_letter = 'E'
    print(correct_letter)
    return answer_choices, correct_letter


class QuestionFactory:

    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f"Question number: {self.number}"

    @staticmethod
    def no_of_primes():
        a = randint(5, 10)
        b = randint(20, 50)

        def prime_check(n):
            # 0, 1, even numbers greater than 2 are NOT PRIME
            if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
                return "Not prime"
            else:
                '''Not prime if divisible by another number less than
                or equal to the square root of itself.
                n**(1/2) returns square root of n'''
                for i in range(3, int(n ** (1 / 2)) + 1, 2):
                    if n % i == 0:
                        return "Not prime"
                return "Prime"

        def total_primes(a, b):
            q_id = uuid.uuid4()
            arr = range(a + 1, b)
            wrongs = []
            correct = 0
            stem = f"How many prime numbers are less than {b} and greater than {a}?"
            print(stem)
            for num in arr:
                if prime_check(num) == "Prime":
                    correct += 1
            while len(wrongs) < 4:
                wrong = correct + randint(-5, 10)
                if wrong not in wrongs and wrong > 0 and wrong != correct:
                    wrongs.append(wrong)
            wrongs.append(correct)
            choices_and_correct = arrange_answer_choices(answer_choices=wrongs, correct=correct)

            return QuestionElements(
                question_stem=stem, ac_list=choices_and_correct[0], correct=choices_and_correct[1], uuid=q_id)

        return total_primes(a, b)

    @staticmethod
    def sum_of_first_n_numbers():

        n1 = randint(1, 10) * 25
        n2 = n1 * randint(2, 5)

        def gaussian_theorem_consecutive(n):
            return int((n + 1) * n / 2)

        def first_second(n1, n2):
            q_id = uuid.uuid4()
            answer_choices = []
            first = "{:,}".format(gaussian_theorem_consecutive(n1))
            second = gaussian_theorem_consecutive(n2)
            stem = f'''The sum of the first {n1} positive integers is {first}. 
What is the sum of the first {n2} positive integers?'''
            print(
                f'''The sum of the first {n1} positive integers is {first}. 
What is the sum of the first {n2} positive integers?''')
            correct = second
            answer_choices.append(correct)
            while len(answer_choices) < 5:
                wrongs = correct + (randint(-5, 10)) * 25
                if wrongs not in answer_choices and wrongs > 0 and wrongs != correct:
                    answer_choices.append(wrongs)
            choices_and_correct = arrange_answer_choices(answer_choices=answer_choices, correct=correct)

            return QuestionElements(
                question_stem=stem, ac_list=choices_and_correct[0], correct=choices_and_correct[1], uuid=q_id)

        return first_second(n1, n2)

    @staticmethod
    def mf_rat_ratio():

        n1 = randint(4, 6) * 10
        n2 = randint(2, 4) * 10

        def rat_ratio(n1, n2):
            q_id = uuid.uuid4()
            answer_choices = []
            stem = f"""{n1} percent of the mice included in an experiment were male mice. If some of the mice 
died during the experiment and {n2} percent of the mice that died were male mice, 
what was the ratio of death rate among the male mice to the death rate among the female mice?"""
            print(stem)
            num_of_num = int((n2 / 100) * 50)
            denom_of_num = n1
            num_of_denom = int(50 - num_of_num)
            denom_of_denom = 100 - n1
            numerator = Fraction(num_of_num / denom_of_num)
            denominator = Fraction(num_of_denom / denom_of_denom)
            correct = (numerator / denominator).limit_denominator()
            answer_choices.append(correct)
            while len(answer_choices) < 5:
                wrongs = Fraction(randint(1, 9) / randint(1, 9)).limit_denominator()
                if wrongs not in answer_choices and wrongs > 0 and wrongs != correct:
                    answer_choices.append(wrongs)
            choices_and_correct = arrange_answer_choices(answer_choices=answer_choices, correct=correct)
            return QuestionElements(
                question_stem=stem, ac_list=choices_and_correct[0], correct=choices_and_correct[1], uuid=q_id)

        return rat_ratio(n1, n2)

    @staticmethod
    def age_diff():

        def al_age():
            q_id = uuid.uuid4()
            factor_dict = {2: 'twice', 3: 'three times', 4: 'four times', 5: 'five times', 6: 'six times',
                           7: 'seven times'}
            randomizer1 = randrange(3, 7, 2)
            randomizer2 = randint(2, randomizer1 - 1)
            in_years = randrange(3, 15, 2)
            less_years = randrange(1, 5, 2)
            name_1 = names.get_first_name(gender='male')
            name_2 = names.get_first_name(gender='female')
            stem = f"""Today {name_1} is {factor_dict[randomizer1]} as old as {name_2}. In {in_years} year(s),
{name_1} will be {less_years} year(s) less than {factor_dict[randomizer2]} as old as {name_2} will be then. 
How many years old is {name_1} today?"""
            correct = int((randomizer2 * in_years - less_years - in_years) / (1 - (randomizer2 / randomizer1)))
            answer_choices = []
            if correct == 0:
                al_age()
            else:
                print(stem)
                answer_choices.append(correct)
            while len(answer_choices) < 5:
                wrongs = correct + randint(-10, 20)
                if wrongs not in answer_choices and wrongs > 0 and wrongs != correct:
                    answer_choices.append(wrongs)
            choices_and_correct = arrange_answer_choices(answer_choices=answer_choices, correct=correct)
            return QuestionElements(
                question_stem=stem, ac_list=choices_and_correct[0], correct=choices_and_correct[1], uuid=q_id)
        return al_age()

    @staticmethod
    def jacket_profit():
        q_id = uuid.uuid4()
        mark_up = randint(1, 3) / 4
        if mark_up == 1 / 4:
            discount = 1 / 5
        else:
            discount = randint(1, 2) / 5
        purchase_price = int((20 * randint(3, 6)))
        sale_price = purchase_price / (1 - mark_up)
        discounted_price = sale_price * (1 - discount)
        correct = discounted_price - purchase_price
        stem = f"""A merchant purchased a jacket for ${purchase_price} and
then determined a selling price that equalled the purchase price of
the jacket plus a markup that was {int(mark_up * 100)} percent of the selling
price. During a sale, the merchant discounted the selling price by
{int(discount * 100)} percent and sold the jacket. What was the merchant's 
gross profit on the sale?"""
        answer_choices = []
        print(stem)
        answer_choices.append(correct)
        while len(answer_choices) < 5:
            wrongs = correct + randint(-10, 20)
            if wrongs not in answer_choices and wrongs > 0 and wrongs != correct:
                answer_choices.append(wrongs)
        choices_and_correct = arrange_answer_choices(answer_choices=answer_choices, correct=correct)

        return QuestionElements(
            question_stem=stem, ac_list=choices_and_correct[0], correct=choices_and_correct[1], uuid=q_id)


class QuestionElements:

    def __init__(self, question_stem, ac_list, correct, uuid):
        self.question_stem = question_stem
        self.ac_list = ac_list
        self.correct = correct
        self.uuid = uuid

    def __repr__(self):
        return f"Question:"

    # def unpack_question(self, ac_list):
    #     a = ac_list[0]
    #     b = ac_list[1]
    #     c = ac_list[2]
    #     d = ac_list[3]
    #     e = ac_list[4]
    #     return a, b, c, d, e
