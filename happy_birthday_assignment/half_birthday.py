from datetime import datetime


def half_birthday():
    your_birthday = datetime.strptime(input('Input your birthday: '), '%m/%d/%Y')
    six_months_later = your_birthday - 182
    print(six_months_later)


if __name__ == '__main__':
    half_birthday()
