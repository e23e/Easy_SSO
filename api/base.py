from fastapi import FastAPI

from api.controllers.github_oauth_controller import github_router
from lib.queue import Queue

app = FastAPI(debug=True)

@app.get("/")
def root():
    return {"msg" : "Please vist /docs page for swagger options and read the README.md file for the detailed info!"}

app.include_router(github_router)

@app.get("/get/access_credentials")
def get_access_credentials():
    data = Queue.get_queue_list()
    return {"data" : data}
