from aiohttp import web
import jinja2
import aiohttp_jinja2

from routes import setup_routes
from settings import config, BASE_DIR
from db import init_pg, close_pg


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR /'app'/'templates')))
setup_routes(app)
app['config'] = config
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)

if __name__ == '__main__':
    web.run_app(app)