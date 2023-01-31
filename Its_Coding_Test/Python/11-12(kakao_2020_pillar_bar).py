Pillar = [[]]
Bar = [[]]

def checkPillar(x, y):
    if y == 0 or Pillar[x][y-1]:
        return True
    if (x > 0 and Bar[x-1][y]) or Bar[x][y]:
        return True
    return False

def checkBar(x, y):
    if Pillar[x][y-1] or Pillar[x+1][y-1]:
        return True
    if x > 0 and Bar[x-1][y] and Bar[x+1][y]:
        return True
    return False
    
def canDelete(x, y):
    for i in range(x-1, x+2):
        for j in range(y, y+2):
            if Pillar[i][j] and checkPillar(i, j) == False:
                return False
            if Bar[i][j] and checkBar(i, j) == False:
                return False
    return True
    
def solution(n, build_frame):
    global Pillar, Bar
    Pillar = [[0 for _ in range(n+2)] for _ in range(n+2)]
    Bar = [[0 for _ in range(n+2)] for _ in range(n+2)]
    
    for x, y, kind, cmd in build_frame:
        if kind == 0:
            if cmd == 1:
                if checkPillar(x, y):
                    Pillar[x][y] = 1
            else:
                Pillar[x][y] = 0
                if not canDelete(x, y):
                    Pillar[x][y] = 1
        
        else:
            if cmd == 1:
                if checkBar(x, y):
                    Bar[x][y] = 1
            else:
                Bar[x][y] = 0
                if not canDelete(x, y):
                    Bar[x][y] = 1

    answer = [[]]
    for x in range(n+1):
        for y in range(n+1):
            if Pillar[x][y]:
                answer.append([x, y, 0])
            if Bar[x][y]:
                answer.append([x, y, 1])

    return answer
