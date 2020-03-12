from datetime import datetime


def half_birthday():
    your_birthday = datetime.strptime(input('Input your birthday: '), '%m/%d/%Y')
    print(your_birthday)


if __name__ == '__main__':
    half_birthday()
