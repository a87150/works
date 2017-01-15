import aiohttp
import asyncio
import time
import requests
from concurrent.futures import ThreadPoolExecutor

NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'
def fetch(a):
    r = requests.get(URL.format(a))
    return r.json()['args']['a']
start = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    for num, result in zip(NUMBERS, executor.map(fetch, NUMBERS)):
        print('fetch({}) = {}'.format(num, result))
print('Use requests+ThreadPoolExecutor cost: {}'.format(time.time() - start))


async def fetch_async(a):
    async with aiohttp.request('GET', URL.format(a)) as r:
        data = await r.json()
    return data['args']['a']

start = time.time()
event_loop = asyncio.get_event_loop()
tasks = [fetch_async(num) for num in NUMBERS]
results = event_loop.run_until_complete(asyncio.gather(*tasks))
for num, result in zip(NUMBERS, results):
    print('fetch({}) = {}'.format(num, result))
print('Use requests+ThreadPoolExecutor cost: {}'.format(time.time() - start))
