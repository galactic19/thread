import concurrent.futures
import time

def process_item(item):
    """각 항목을 처리하는 함수"""
    print(f"처리 중: {item}")
    time.sleep(2)  # 작업을 시뮬레이션하기 위한 대기
    return f"결과: {item * 2}"

def process_items_with_thread_pool(items, max_workers=3):
    """스레드 풀을 사용하여 여러 항목을 병렬로 처리"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 모든 항목에 대해 작업 제출
        future_to_item = {executor.submit(process_item, item): item for item in items}
        
        # 완료된 작업 결과 처리
        for future in concurrent.futures.as_completed(future_to_item):
            item = future_to_item[future]
            try:
                result = future.result()
                print(f"항목 {item}의 {result}")
            except Exception as e:
                print(f"항목 {item} 처리 중 에러 발생: {e}")

def main():
    items = range(1, 11)  # 처리할 항목들
    
    start_time = time.time()
    
    process_items_with_thread_pool(items)
    
    end_time = time.time()
    print(f"총 실행 시간: {end_time - start_time:.2f} 초")

if __name__ == "__main__":
    main()