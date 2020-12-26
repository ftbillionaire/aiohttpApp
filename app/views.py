from aiohttp import web
import aiohttp_jinja2
import db
from db import get_post

@aiohttp_jinja2.template('index.html')
async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.posts.select())
        result = await cursor.fetchall()
        posts = [dict(post) for post in result]
        return {'posts':posts}

@aiohttp_jinja2.template('detail.html')
async def detail(request):
    post_id = request.match_info['post_id']
    async with request.app['db'].acquire() as conn:
        data = await get_post(post_id, conn)
        result = await data.fetchall()
        post = [dict(post) for post in result]
        post_dict = {}
        for p in post:
            post_dict['id'] = p['id']
            post_dict['title'] = p['title']
            post_dict['text'] = p['text']
            post_dict['pub_date'] = p['pub_date']
            post_dict['tagID'] = p['tagID']
        return {'post': post_dict}