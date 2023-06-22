import uvicorn

from lib.constants import OAUTH_SERVICE_PORT

if __name__=="__main__":
    uvicorn.run("api.base:app", host="0.0.0.0", port=int(OAUTH_SERVICE_PORT), reload=True)
