import time

def find_user_sync(id: int, n: int) -> None:

    for i in range(1, (n + 1)):
        print(f"{id}함수 실행 중 : ", end = '')
        print(f"{n}명중 {i}번째 회원 조회중...")
        time.sleep(1)
    print(f"{id}함수의-> {n}명의 데이터 조회 완료..")


def sync_process():
    start = time.time()
    find_user_sync(1000, 3)
    find_user_sync(1001, 2)
    find_user_sync(1002, 1)
    end = time.time()

    print(f">>> 동기 회원 조회 시간: {end - start}")


sync_process()