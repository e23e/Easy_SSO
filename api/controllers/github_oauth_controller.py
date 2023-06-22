from threading import Thread

from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from api.helpers.github_oauth_helper import Github_Helper
from lib.constants import OAUTH_GITHUB_CLIENT_ID

github_router = APIRouter()


@github_router.get("/github/login")
async def github_login(scope: str = None):
    if scope is None:
        raise HTTPException(status_code=400, detail="scope param is missing, please read README.md for more info")
    url = f"https://github.com/login/oauth/authorize?client_id={OAUTH_GITHUB_CLIENT_ID}&scope={scope}"
    return RedirectResponse(url=url, status_code=302)

@github_router.get("/github/callback")
def github_callback(code: str):
    if code is None:
        raise HTTPException(status_code=400, detail="Code param is empty")
    print(code)
    t_thread = Thread(target=Github_Helper.process_credentials, args=(code,))
    t_thread.start()
    return {"msg" : "Success!"}






