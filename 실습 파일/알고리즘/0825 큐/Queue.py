# practice 1
Queue = [1, 2, 3]
front = -1
rear = len(Queue)-1

while front < rear:
    print(Queue[front+1])
    front += 1


## 원형큐
front = rear = 0

rear += 1
Q[rear] = item

# enQueue(item)
rear += 1
if rear == N:
    rear = 0
# 위와 같음
rear = (rear+1) % N

# deQueue()
front += 1
if front == N:
    front = 0
# 위와 같음
front = (front+1) % N

def isFull():       # 포화상태
    return (rear+1)%len(cQ) == front