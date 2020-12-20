from input_utils import *
import operator

def solve_1(data):
    return sum(map(solve_equation_left_precedence, data))
    
def solve_equation_left_precedence(equation):    
    equation = equation.replace(' ', '')
    op = None
    answer = 0
    number_buffer = ''
    equation_pointer = 0

    def update_answer():
        nonlocal op
        nonlocal answer
        nonlocal number_buffer
        if (op != None):
            answer = op(answer, int(number_buffer))
        else:
            answer = int(number_buffer)
        number_buffer = ''

    while (equation_pointer < len(equation)):
        target = equation[equation_pointer]
        if (target == '+'):
            update_answer()
            op = operator.add
            equation_pointer += 1
        elif (target == '*'):
            update_answer()
            op = operator.mul
            equation_pointer += 1
        elif (target == '('):
            forwarded_count = 1
            equation_pointer += 1
            start_of_bracket_eq = equation_pointer
            while(forwarded_count != 0):
                brack_target = equation[equation_pointer]
                if (brack_target == '('):
                    forwarded_count += 1
                elif (brack_target == ')'):
                    forwarded_count -= 1
                equation_pointer += 1
            end_of_bracket_eq = equation_pointer - 1
            number_buffer = solve_equation_left_precedence(equation[start_of_bracket_eq:end_of_bracket_eq])
        else:
            number_buffer += target
            equation_pointer += 1
    update_answer()
    return answer

def solve_2(data):
    return sum(map(solve_equation_plus_precedence, data))
    
def solve_equation_plus_precedence(equation):    
    equation = equation.replace(' ', '')
    equation = resolve_brackets(equation)
    equation = resolve_plus(equation)
    return evaluate_mults(equation)

def resolve_brackets(equation):
    new_equation = ''
    equation_pointer = 0
    while (equation_pointer < len(equation)):
        target = equation[equation_pointer]
        if (target == '('):
            forwarded_count = 1
            equation_pointer += 1
            start_of_bracket_eq = equation_pointer
            while(forwarded_count != 0):
                brack_target = equation[equation_pointer]
                if (brack_target == '('):
                    forwarded_count += 1
                elif (brack_target == ')'):
                    forwarded_count -= 1
                equation_pointer += 1
            end_of_bracket_eq = equation_pointer - 1
            new_equation += str(solve_equation_plus_precedence(equation[start_of_bracket_eq:end_of_bracket_eq]))
        else:
            new_equation += target
            equation_pointer += 1
    return new_equation

def resolve_plus(equation):
    new_equation = ''
    equation_pointer = 0
    number_buffer = ''
    plus_lst = []
    while (equation_pointer < len(equation)):
        target = equation[equation_pointer]
        if (target == '+'):
            plus_lst.append(int(number_buffer))
            number_buffer = ''
        elif (target == '*'):
            plus_lst.append(int(number_buffer))
            new_equation += str(sum(plus_lst))
            plus_lst = []
            new_equation += '*'
            number_buffer = ''
        else:
            number_buffer += target
        equation_pointer += 1
    plus_lst.append(int(number_buffer))
    new_equation += str(sum(plus_lst))
    return new_equation

def evaluate_mults(equation):
    values = equation.split('*')
    return functools.reduce(lambda a, b: a * int(b), values, 1)

print('Part 1')
print(f"Answer: {solve_1(get_input_as_list(1))}")

print('Part 2')
print(f"Answer: {solve_2(get_input_as_list(1))}")