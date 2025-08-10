# ----------------------------------
'''многопоточність'''
from venv import create

'''import threading
threading.current_thread() - поточний потік
threading.Thread(target = що саме запускати, args=аргументи, name=імя потоку)
thread.start() - запуск потоку
змінна  = threading.Lock() - тільки один потік
thread.join()- приєднання до основного потоку'''
# ----------------------------------
'''мультипроцессориц'''
'''import multiprocessing
-для розподілення нагрузки на ядра
multiprocessing.Pool(processes=multiprocessing.cpu_count()) - використання всіх ядер- '''
# ----------------------------------
'''Асинхронність'''
'''import asyncio
async def fucn():
    pass
asyncio.create_task('') - создать асинхрон
await asyncio.gather(...,...) - вместе две асинхронки
asyncio.run() - запустить асинхрон'''

'''import requests
requests.get(url=..., allow-redirect=True|False) - запрос
requests.Response - ответ'''

import httpx
async def get_res(url, client: httpx.AsyncClient):
    res = await client.get(url, follow_redirects=True)
    # приклад асинхронного завантаження
mk