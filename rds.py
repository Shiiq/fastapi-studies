import asyncio

from redis.asyncio.client import Redis

r = Redis(host="localhost", port=6379)

data_st = [f"{i}_d" for i in range(1, 21)]


async def run_set():
    # res1 = await r.sadd("bikes:racing:france", "bike:123")
    # print(res1)
    # res2 = await r.sadd("bikes:racing:france", "bike:2", "bike:3")
    # print(res2)
    # await r.srem("bikes:racing:france", "bike:4", "bike:5", "bike:6")
    # res3 = await r.sadd("bikes:racing:france", "bike:4", "bike:5", "bike:6")
    # print(res3)
    # items = await r.smembers("bikes:racing:france")
    # print(items)
    # ia = await r.smembers("bikes:racing")
    # print(ia)
    pass


async def run_list():
    # await r.rpush("movie:data", *data_st)
    # res2 = await r.lrange("movie:data", 0, -1)
    # print(res2)
    # x = await r.rpop("movie:data")
    # print(x)
    # print(*data_st[0:5])
    res3 = await r.lrange("movie:data", 19, 45)
    print(res3)
    # res4 = await r.lrange("movie:data", 10, 14)
    # print(res4)
    # res5 = await r.lrange("movie:data", 15, 20)
    # print(res5)
    # await r.ltrim("movie:data", 1, 0)

    # ex = await r.llen("data:list")
    # print(ex)
    # xe = await r.llen("movie:comedyactionadventureanimationchildren20062007")
    # print(xe)
    # x = await r.exists("data:movies:1", "data:movies:2")
    # print(x, type(x))

    pass


asyncio.run(run_list())
