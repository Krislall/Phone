def check_phone_number(x: str) -> str:
    result = ''.join([i for i in x if i.isdigit()])
    if len(result) in {10, 11}:
        return result[-10:]
    raise ValueError('Number entered incorrectly')




