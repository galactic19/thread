# 간단한 멀티스레드 프로그램 작성하기
# 1부터 100까지의 숫자 중 짝수와 홀수를 각각 다른 스레드에서 출력하는 프로그램을 작성.

import threading
import time

class MultiThread:
    def __init__(self):
        self.lock = threading.Lock()
    
    def print_odd(self): # odd_number
        for i in range(1,101, 1):
            # with self.lock:
                print(i)
                time.sleep(0.1)
                
    def print_even(self):
        for i in range(1, 101, 2):
            # with self.lock:
                print(i)
                time.sleep(0.1)
                
                
if __name__ == "__main__":
    import threading 
    import time
    
    mt = MultiThread()
    
    start_time = time.time()
    
    odd = threading.Thread(target=mt.print_odd)
    even = threading.Thread(target=mt.print_even)
    
    odd.start()
    even.start()
    
    odd.join()
    even.join()
    
    end_time = time.time()
    print(f'실행시간 : {end_time - start_time} 초')
    
    
    
