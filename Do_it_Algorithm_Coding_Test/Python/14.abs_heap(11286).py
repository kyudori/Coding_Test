# https://www.daleseo.com/python-priority-queue/
# https://coding-nurse.tistory.com/14
# https://coding-nurse.tistory.com/8
from queue import PriorityQueue
import sys

print = sys.stdout.write #줄바꿈 없이 바로 출력
input = sys.stdin.readline #한번 입럭, 하나하나 한줄씩 출력

N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1]))+'\n')
    else:
        myQueue.put((abs(request), request))