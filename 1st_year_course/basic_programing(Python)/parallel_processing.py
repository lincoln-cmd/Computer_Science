'''
 - 병렬처리(프로세스와 쓰레드)

 파이썬은 인터프리터 언어로서 기본적으로 싱글 쓰레드에서 ㅅ순차적으로 동작.
따라서 병렬처리를 위해선 별도의 모듈을 사용하여 수행해야 한다.
'''

from threading import Thread
import time

def work(work_id, start, end, result):
    start_time = time.time()
    total = 0
    for i in range(start, end):
        total += 1
    result.append(total)
    
    print(time.time() - start_time)
    
if __name__ == "__main__":
    result = []
    th1 = Thread(target = work, args = (1, 0, 10000, result))
    th2 = Thread(target = work, args = (2, 10001, 20000, result))
    
    th1.start()
    th2.start()
    th1.join() # join() 메소드는 파이썬에게 프로세스가 종료 될 때까지 대기하도록 지시
    th2.join() # 불완전한 종료를 방지하기 위해 join() 메소드 사용.
    
    print(result)

'''
 파이선에서 멀티 쓰레드를 쓴 것과 싱글 쓰레드를 쓴 것은 실행시간이 거의 차이가 없다.
이것은 파이썬의 GIL(Global Interpreter Lock) 정책 때문이다.
단, 이 GIL 정책은 cpu 작업에서만 적용되므로 I/O(파일 읽고 쓰기, 하드디스크 속도를 사용) 작업이 많은 병렬처리 작업에서는 멀티
쓰레드가 효과적일 수 있다.
'''


######################################################################


'''
 멀티 프로세싱(POOL)
 
'''

from multiprocessing import Pool
import time
import os

def f(x):
    print(os.getpid())
    return x * x

print(__name__)

if __name__ == '__main__':
    p = Pool(4)
    result = p.map(f, [1, 2, 3, 4])
    p.close() # 사용 후 프로세스를 죽임. 안그러면 프로세스가 계속 남아서 메모리 성능이 떨어짐.
    print(result)

# 과도하게 많은 프로세스를 만들 경우 프로세스를 띄우는데 걸리는 시간과 cpu의 제한 때문에 효율이 떨어짐.
# 보통 pc의 코어의 개수만큼 프로세스를 띄워서 사용함.


'''
 멀티 프로세싱(Process)
'''

import os
from multiprocessing import Process

def f2(x):
    print(x*x)
    
if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    proc1 = Process(target = f2, args = (numbers[0],))
    proc1.start()
    proc2 = Process(target = f2, args = (numbers[1],))
    proc2.start()
    proc3 = Process(target = f2, args = (numbers[2],))
    proc3.start()
    proc4 = Process(target = f2, args = (numbers[3],))
    proc4.start()
    proc1.join()
    proc2.join()
    proc3.join()
    proc4.join()
    
'''
 Pool과 Process 모두 병렬 처리를 위해 사용되지만 차이가 있다. 간단하게 설명하면, Pool은 처리할 일들을 pool에 뿌려 놓고 일아서 병렬 처리를 하게 만드는 것이고,
Process는 각 프로세스별로 할당량을 명시적으로 적어 두고 그걸 처리하게 하는 것이다.

 쓰레드는 가볍지만 파이썬의 GIL 정책으로 인해 I/O 처리를 하는 경우에만 주로 효과적이고 프로세스는 각자가 고유한 메모리 영역을 가지기 때문에 처음 프로세스를 만들 때
시간이 조금 필요히고 더 많은 메모리를 필요로 하지만 병렬적으로 cpu 작업을 할 수 있어서 빠르다.
'''
    
