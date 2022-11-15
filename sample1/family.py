"""
촌수를 계산하는 모듈입니다.
"""

def family (n, s, e, num):

    injub = [[0 for i in range(n+1)] for j in range(n+1)]
    result = [0 for j in range(n+1)]
    queue = [0 for j in range(n*(n-1))]
    queueCost = [0 for j in range(n*(n-1))]

    # 시작노드와 종료노드가 같으면 자기자신이므로 0촌 프로그램 종료
    if s == e :
        print("0")

    # 인접행렬 생성, 부모와 자식은 양방향노드 True
    for i in range(num):
        x, y = map(int, input().split(' '))  # 부모와 자식의 번호
        injub[x][y] = True
        injub[y][x] = True

    # dfs에 사용할 queue 초기화
    head = 0
    tail = 1
    queue[0] = s
    queueCost[0] = 0

    while head<tail :
        for i in range(n) :
            if injub[queue[head]][i] == True : #자식탐색
                # 자식발견시 추가
                queue[tail] = i
                # queue.append(tail, 1)
                queueCost[tail] = queueCost[head]+1
                # 촌수 중복계산 방지를위해 인접행렬에서 표기한 기존 연결을 끊어줌
                injub[queue[head]][i] = False
                injub[i][queue[head]] = False

                tail += 1
        # 기존에 탐색한 노드 결과배열에 저장 (pop)
        result[queue[head]] = queueCost[head];
        head += 1

    # 도달할 수 없는 경우 초기화값인 0으로 되어있을테니 -1으로 바꿔서 출력
    if result[e] == 0 :
        print('-1')
    else :
        print(result[e])

if __name__ == '__main__':
    n = int(input())  # 전체 사람 수
    s, e = map(int, input().split(' '))  # 두 사람의 촌수를 구할것
    num = int(input())  # 관계 수
    family(n, s, e, num)