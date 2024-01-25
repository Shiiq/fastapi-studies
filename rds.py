import asyncio

import redis.asyncio as redis
from redis.asyncio.client import Redis

r = redis.Redis(host="localhost", port=6379)

data_st = ["data1", "data2", "data3", "data4"]

async def run():
    # res1 = await r.sadd("bikes:racing:france", "bike:123")
    # print(res1)
    # res2 = await r.sadd("bikes:racing:france", "bike:2", "bike:3")
    # print(res2)
    # await r.srem("bikes:racing:france", "bike:4", "bike:5", "bike:6")
    # res3 = await r.sadd("bikes:racing:france", "bike:4", "bike:5", "bike:6")
    # print(res3)
    items = await r.smembers("bikes:racing:france")
    print(items)
    ia = await r.smembers("bikes:racing")
    print(ia)


asyncio.run(run())
