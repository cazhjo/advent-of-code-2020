import input
import re
data = input.get_data("18")

def get_sub_expression(first_parenthesis, expression):
    parenthesis_count = 0
    for index in range(first_parenthesis + 1, len(expression)):
        if expression[index] == "(":
            parenthesis_count += 1
        elif expression[index] == ")":
            parenthesis_count -= 1

        if parenthesis_count == -1:
            return expression[first_parenthesis + 1:index]


def handle_calc(root, operator, operand):
    if operator == "*":
        return root * operand
    elif operator == "+":
        return root + operand


def calc(expression, precedence=""):
    if "(" in expression:
        first_parenthesis = expression.index("(")
        sub_expression = get_sub_expression(first_parenthesis, expression)
        expression = expression[:first_parenthesis] + calc(sub_expression, precedence) + expression[first_parenthesis + len(sub_expression) + 2:]
        return calc(expression, precedence)
    else:
        temp = re.split("(\W)", expression)
        operator = ""
        i = 0
        while len(temp) > 1:
            try:
                int(temp[i])
            except ValueError:
                operator = temp[i]
                i += 1
                continue

            if operator != "":
                if precedence != "" and precedence in temp:
                    if operator != precedence:
                        operator = ""
                        i += 1
                        continue
                result = handle_calc(int(temp[i - 2]), operator, int(temp[i]))
                temp = temp[: i - 2] + [str(result)] + temp[i + 1:] 
                i = 0
                operator = ""
                continue
            i += 1
            
        return temp[0]
            

def sum_of_expressions(expressions, precedence=""):
    total_sum = 0
    for expression in expressions:
        total_sum += int(calc(expression.replace(" ", ""), precedence))

    return total_sum

print("Part1:", sum_of_expressions(data))
print("Part2:", sum_of_expressions(data, "+"))