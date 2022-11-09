"""
하노이의 탑 출력 stack을 활용한 모듈입니다.
"""
def hanoi ():
    """
    원판의 갯수를 입력 받고 원판 이동 횟수를 출력함
    :return:
    """
    n = int(input('1~100까지의 숫자를 입력 하여 주세요.'))
    if 1 <= n and n <= 100 :
        print(2**n - 1)
        hanoiStack(n, 1, 2, 3)
    else:
        print("1~100까지의 숫자만 입력 하여 주세요.")

def hanoiStack(num, tray_first, tray_Second, tray_third):
    """
    :param n: 입력 받은 원판의 갯수 n
    :param tray1: 현재 밟고 있는 발판 tray1
    :param tray2: 임시 저장 발판 tray2
    :param tray3: 이동할 위치의 발판 tray3
    :return:
    """
    stack = []
    stack.append((num, tray_first, tray_third, False))

    while len(stack) > 0:
        num, tray_start, tray_end, move = stack.pop()
        if move:
            print(tray_start, tray_end)
        elif 0 < num and num <= 20 :
            stack.append((num - 1, tray_Second, tray_end, False))
            stack.append((num, tray_start, tray_end, True))
            stack.append((num - 1, tray_start, tray_Second, False))

if __name__ == '__main__':
    hanoi()