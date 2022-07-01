from random import randint, randrange
from fractions import Fraction


class Question:

    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f"Question number: {self.number}"

    def No_of_Primes(self):
        a = randint(5, 10)
        b = randint(20, 50)

        def primeCheck(n):
            # 0, 1, even numbers greater than 2 are NOT PRIME
            if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
                return "Not prime"
            else:
                '''Not prime if divisable by another number less than
                or equal to the square root of itself.
                n**(1/2) returns square root of n'''
                for i in range(3, int(n ** (1 / 2)) + 1, 2):
                    if n % i == 0:
                        return "Not prime"
                return "Prime"

        def totalPrimes(a, b):
            arr = range(a + 1, b)
            wrongs = []
            correct = 0
            stem = f"How many prime numbers are less than {b} and greater than {a}?"
            print(stem)
            for num in arr:
                if primeCheck(num) == "Prime":
                    correct += 1
            while len(wrongs) < 4:
                wrong = correct + randint(-5, 5)
                if wrong not in wrongs and wrong > 0 and wrong != correct:
                    wrongs.append(wrong)
            # print(f"The correct answer is {correct}, and the wrong answers are {wrongs}")
            wrongs.append(correct)
            asc_desc = randint(0, 1)
            if asc_desc == 0:
                answer_choices = sorted(wrongs)
            else:
                answer_choices = (sorted(wrongs))[::-1]

            choices = ['A', 'B', 'C', 'D', 'E']
            i = 0
            while i < len(answer_choices):
                print(f"{choices[i]}) {answer_choices[i]}")
                i += 1
            # return f"all choices: {answer_choices}"

        return totalPrimes(a, b)

    def sum_of_first_n_numbers(self):

        n1 = randint(1, 10) * 25
        n2 = n1 * randint(2, 5)

        def gaussian_theorem_consecutive(n):
            return int((n + 1) * (n) / 2)

        def first_second(n1, n2):
            answer_choices = []
            first = gaussian_theorem_consecutive(n1)
            second = gaussian_theorem_consecutive(n2)
            print(
                f'The sum of the first {n1} positive intergers is {first}. What is the sum of the first {n2} postive integers')
            correct = second
            answer_choices.append(correct)
            while len(answer_choices) < 5:
                wrongs = correct + (randint(-5, 5)) * 25
                if wrongs not in answer_choices and wrongs > 0 and wrongs != correct:
                    answer_choices.append(wrongs)
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

        return first_second(n1, n2)

    def mf_rat_ratio(self):

        n1 = randint(4, 6) * 10
        n2 = randint(2, 4) * 10

        def rat_ratio(n1, n2):

            answer_choices = []
            stem = f"""{n1} percent of the rats included in an experiment were male rats. If some of the rats 
died during the experiment and {n2} percent of the rats that died were male rats, 
what was the ratio of death rate among the male rats to the death rate among the female rats?"""
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

        return rat_ratio(n1, n2)

    def age_diff(self):

        def Al_age():
            factor_dict = {2: 'twice', 3: 'three times', 4: 'four times', 5: 'five times', 6: 'six times',
                           7: 'seven times'}
            randomizer1 = randrange(3, 7, 2)
            randomizer2 = randint(2, randomizer1 - 1)
            in_years = randrange(3, 15, 2)
            less_years = randrange(1, 5, 2)
            stem = f"""Today Al is {factor_dict[randomizer1]} as old as Pat. In {in_years} year(s),
Al will be {less_years} year(s) less than {factor_dict[randomizer2]} as old as Pat will be then. 
How many years old is Al today?"""
            correct = int((randomizer2 * in_years - less_years - in_years) / (1 - (randomizer2 / randomizer1)))
            answer_choices = []
            if correct == 0:
                Al_age()
            else:
                print(stem)
                answer_choices.append(correct)
            while len(answer_choices) < 5:
                wrongs = correct + randint(-20, 20)
                if wrongs not in answer_choices and wrongs > 0 and wrongs != correct:
                    answer_choices.append(wrongs)
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

        return Al_age()