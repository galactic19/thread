# 단일 스레드 예제.
import threading
import time


class ThreadStudy:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()
        
    def print_number(self):
        for i in range(1, 6):
            print(f"Number : {i}")
            time.sleep(1)


    def print_letter(self):
        for letter in 'ABCDE':
            print(f'letter : {letter}')
            time.sleep(1)
            
    def increament(self):
        for _ in range(1000000):
            with self.lock:
                self.count += 1


if __name__ == "__main__":
    thread = ThreadStudy()

    # 멀티 스레드 예제
    # 함수는 위 생성한 동일한 함수를 사용하고, 아래와 같은 방식으로 호출 한다.

    start_time = time.time()
    print(f"시작시간 {start_time}")

    thread1 = threading.Thread(target=thread.print_number)
    thread2 = threading.Thread(target=thread.print_letter)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time = time.time()
    print(f'종료시간 : {end_time}')
    print(f'실행시간 : {end_time - start_time} 초')


    print('Done 스레드 동작 완료')
