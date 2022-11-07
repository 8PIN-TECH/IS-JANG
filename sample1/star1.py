
num = int(input('숫자를 입력 하여 주세요.'))

if 1 < num < 200:
    for line in range(num):
        for blank in range(line):
            print(' ', end="")
        for star in range(2 * (num - line) - 1):
            print('*', end="")
        print('')

    for line in range(1, num):
        for blank in range(num - line - 1):
            print(' ', end="")
        for star in range(2 * line + 1):
            print('*', end="")
        print('')
else :
    print("2 ~ 199 사이의 숫자만 입력 하여 주세요.")

