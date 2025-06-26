
def clean_input(user_input):
    return user_input.strip()

def process_data(data):
    tmp = []
    for d in data:
        tmp.append(d.upper())
    return tmp
