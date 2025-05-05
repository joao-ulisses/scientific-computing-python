def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = ''
    second_line = ''
    dashes_line = ''
    results_line = ''
    for problem in problems:
        numbers = problem.split(' ')
        if not all(map(lambda x: x.isdigit(), numbers[2])) or not all(map(lambda x: x.isdigit(), numbers[0])):
            return "Error: Numbers must only contain digits."
        if '+' not in numbers[1] and '-' not in numbers[1]:
            return "Error: Operator must be '+' or '-'."
        if len(numbers[0]) > 4 or len(numbers[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if len(numbers[0]) > len(numbers[2]):
            maximum_space = len(numbers[0]) + 2
        else:
            maximum_space = len(numbers[2]) + 2
        first_line += (' ' * (maximum_space - len(numbers[0]))) + numbers[0]
        second_line += numbers[1] + (' ' * ((maximum_space - 1)- len(numbers[2]))) + numbers[2]
        dashes_line += '-' * maximum_space 
        if show_answers:
            if numbers[1] == '+':
                result = int(numbers[0]) + int(numbers[2])
            else:
                result = int(numbers[0]) - int(numbers[2])
            results_line += (' ' * (maximum_space - len(str(result)))) + str(result)
        if problems.index(problem) != (len(problems) - 1):
            first_line += ' ' * 4
            second_line += ' ' * 4
            dashes_line += ' ' * 4
            results_line += ' ' * 4 
    fixed_problems = '\n'.join((first_line, second_line, dashes_line, results_line))
    if show_answers:
        fixed_problems = '\n'.join((first_line, second_line, dashes_line, results_line))
    else: 
        fixed_problems = '\n'.join((first_line, second_line, dashes_line))
    return fixed_problems

print(arithmetic_arranger(["98 + 35"]))