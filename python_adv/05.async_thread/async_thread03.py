from time import time
import asyncio


async def find_user_async(n: int):
    for i in range(1, n + 1):
        print(f"{n}명중 {i}번쨰 회원의 데이터 조회중...")
        await asyncio.sleep(1)

    print(f"{n}명의 데이터 조회 완료..")


async def async_process():
    start_time = time()
    tast1 = asyncio.create_task(find_user_async(3))
    tast2 = asyncio.create_task(find_user_async(2))
    tast3 = asyncio.create_task(find_user_async(1))
    await tast1()
    await tast2()
    await tast3()
    end_time = time()

    print(f'>>> 비 동기 처리 총 소요 시간 : {end_time - start_time}')


asyncio.run(async_process())