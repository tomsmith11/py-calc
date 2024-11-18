result_prev = 0
operator = ''

print('result_prev:', result_prev)

firstNum = input('Enter your first number')
result_prev = int(firstNum)
print('result_prev:', result_prev)

while True:
    operatorInput = input("Enter an operator (+, -, *, /) or press 'q' to quit")

    if operatorInput == 'q': 
        break

    operator = operatorInput

    num = int(input('Enter a number'))
    currentNum = int(num)

    if operator == '+':
        result_prev += currentNum
    elif operator == '-':
        result_prev -= currentNum
    elif operator == '*':
        result_prev *= currentNum
    elif operator == '/':
        result_prev /= currentNum
    else: 
        print('invalid operator')
    print('result_prev:', result_prev)

print('Final result:', result_prev)