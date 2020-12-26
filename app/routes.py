from views import *

def setup_routes(app):
    app.add_routes([
        web.get('/', index),
        web.get('/{post_id}', detail),
    ])