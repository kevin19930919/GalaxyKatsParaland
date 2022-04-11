import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from concurrent.futures import ThreadPoolExecutor, as_completed,ProcessPoolExecutor
import asyncio


# ==== global parameter ====
url = 'https://parazenwebtwitterranking.azurewebsites.net/api/AddScore?code=W//7zIIgHBv0/LfsxSyCJz7ITZGggxgmyY9uurEPRz7Os12vWlPwaw=='
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
  'Referer': 'https://www.paraland.world/',
  'Origin': 'https://www.paraland.world'
}

data = {
  'name': 'GalaXY Kats',
  'Group': 'Animal'
}

async def async_post(loop):
    await loop.run_in_executor(None,post_api)

def post_api():
    response = requests.post(url, headers = headers, data=json.dumps(data))
    if response.status_code == requests.codes.ok:
        print(f"success request api")
    else:
        print(response.status_code)

async def main():
    loop = asyncio.get_event_loop()
    tasks = []
    total_count = 0
    while True:
      for i in range(1000):
          tasks.append(loop.create_task(async_post(loop)))
      result = await asyncio.gather(*tasks)
      total_count+=1000
      print(f"total count:{total_count}")

if __name__ =="__main__":
  asyncio.run(main())
