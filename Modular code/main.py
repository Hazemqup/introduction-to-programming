from input import receve_input
from operation import calculator
from output import the_answer_opera

def main():

    number1, number2, operater = receve_input()
    answer = calculator(number1, number2, operater)

    the_answer_operater(answer)


if __name__=="__main__":
    main()
