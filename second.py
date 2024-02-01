from litestar import Litestar, get, Request
from litestar.template.base import url_for


@get("/", name="second index")
async def hello_world(request: Request) -> str:
    print(request.url_for("second index"))
    return str(request.url_for("second index"))


app2 = Litestar([hello_world], debug=True)
