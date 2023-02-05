import re


def arithmetic_arranger(problems, solve=False):
    """

    :type problems: object
    """
    if (len(problems) > 5):
        return "Error: Too many problems."
        first = ""
        second = ""
        lines = ""
        sumx = ""
        string = ""

    for problem in problems:
      if (re.search("[^\s0-9.+-]", problem)):
        if re.search(["/"], problem) or       re.search(["*"], problem):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."

      firstNumber = problem.split(" ")[0]
      operator = problem.split(" ")[1]
      secondNumber = problem.split(" ")[2]

      if (len(firstNumber) >= 5 or len(firstNumber) >= 5):
                return "Error: Numbers cannot be more than four digits."
      sumx = ""
      if (operator == "+"):
        sumx = str(int(firstNumber) + int(secondNumber))
      elif (operator == "-"):
        sumx = str(int(firstNumber) - int(secondNumber))


        length = max(len(firstNumber), len(secondNumber)) + 2
        top = str(firstNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length - 1)
        line = ""
        res = str(sumx).rjust(length)

        for s in range(length):
            line += "-"

      if problem != problems[-1]:
        first += top + ' '
        second += bottom + ' '
        lines = line + '  '
        sumx += res + ' '
      else:
        first += top
        second += bottom
        lines = line
        sumx += res

    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    return string



