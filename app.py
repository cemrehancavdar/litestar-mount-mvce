from litestar import Litestar, get, asgi
from second import app2


@get("/")
async def hello_world() -> str:
    return "Hello, world!"


app = Litestar([hello_world], debug=True)
app.register(asgi("second", name="second", is_mount=True)(app2))
