"""
하노이의 탑 출력 모듈입니다.
n이 20보다 클경우 과정은 출력하지 않는다.
"""

def hanoiInOut ():
    n = int(input('1~100까지의 숫자를 입력 하여 주세요.'))
    if (1 <= n <= 100 ):
        print(2**n - 1)
        hanoi(n, 1, 2, 3)
    else:
        print("1~100까지의 숫자만 입력 하여 주세요.")


def hanoi (n, tray1, tray2, tray3):
    """
    :param n: 입력 받은 원판의 갯수 n
    :param tray1: 현재 밟고 있는 발판 tray1
    :param tray2: 임시 저장 발판 tray2
    :param tray3: 이동할 위치의 발판 tray3
    :return:
    """
    if (n == 1):
        print(tray1, tray3)

    elif (1 < n <= 20) :
        hanoi(n - 1, tray1, tray3, tray2)
        print(tray1, tray3)
        hanoi(n - 1, tray2, tray1, tray3)

if __name__ == '__main__':
    hanoiInOut()