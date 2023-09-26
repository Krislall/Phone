def phone_number(x):
    result = ''
    for number in x:
        if number.isdigit():
            result += number
    if len(result) < 10 or len(result) > 11:
        print('Try again')
    if len(result) == 10:
        print(result)
    if len(result) == 11:
        print(result[1:])



