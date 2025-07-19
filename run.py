import deps
from fasthtml.common import Request

PLUGIN_INFO = {
    "name": "Events",
    "version": "1.0.0",
    "author": "traore Eliezer",
    "Api_prefix": "/app/events",
    "tag_for_identified": ["Plugin", "events"],
    "trigger": 2,
}

router = deps.APIRouter(
    prefix=PLUGIN_INFO["Api_prefix"],
)


class Plugin:

    def __init__(self):
        super().__init__()
        return

    @router("/", methods=["GET"])
    def run(session, request: Request):
        # session["user_id"] = "bc523c62-6d38-49f1-9741-124886"
        return
