"""
입력받은 숫자에따라 별을 출력하는 모듈입니다.
"""


def answer():
    """
    정답을 출력 하는 함수입니다.
    :return: null
    """
    num = int(input('숫자를 입력 하여 주세요.'))

    if 1 < num < 200:
        print_star(num)
    else:
        print("2 ~ 199 사이의 숫자만 입력 하여 주세요.")


def print_star(num):
    """
    입력받은 값에 대한 별을 출력합니다.
    :param num:
    :return: null
    """
    for line in range(num):
        for _ in range(line):
            print(' ', end="")
        for _ in range(2 * (num - line) - 1):
            print('*', end="")
        print('')

    for line in range(1, num):
        for _ in range(num - line - 1):
            print(' ', end="")
        for _ in range(2 * line + 1):
            print('*', end="")
        print('')


if __name__ == '__main__':
    answer()
