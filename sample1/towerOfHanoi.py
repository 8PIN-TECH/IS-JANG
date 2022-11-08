"""
하노이의 탑 출력 모듈입니다.
"""

def hanoi (n, tray1, tray2, tray3):
    """
    :param n: 입력 받은 원판의 갯수 n
    :param tray1: 현재 밟고 있는 발판 tray1
    :param tray2: 임시 저장 발판 tray2
    :param tray3: 이동할 위치의 발판 tray3
    :return:
    """
    if (1 < n < 100):
        hanoi(n - 1, tray1, tray3, tray2)
        print(tray1, tray3)
        hanoi(n - 1, tray3, tray2, tray1)

if __name__ == '__main__':
    n = int(input('숫자를 입력 하여 주세요.'))
    print(n)
    hanoi(n, 1, 2, 3)