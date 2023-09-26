def check_phone_number(x: str) -> str:
    result = ''.join([number for number in x if number.isdigit()])
    if len(result) in {10, 11}:
        print(((result[::-1])[:10])[::-1])
    else:
        raise ValueError('Number entered incorrectly')


