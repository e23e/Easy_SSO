import requests

from lib.constants import (OAUTH_GITHUB_CLIENT_ID, OAUTH_GITHUB_CLIENT_SECRET,
                           OAUTH_GITHUB_TOKEN_URL)
from lib.oauth import Oauth


class Github_oauth(Oauth):

    def fetch_credentials(self,code: str) -> dict:
        post_data = f"client_id={OAUTH_GITHUB_CLIENT_ID}&client_secret={OAUTH_GITHUB_CLIENT_SECRET}&code={code}"
        header = {"Accept" : "application/json"}
        try:
            r = requests.post(url=OAUTH_GITHUB_TOKEN_URL, data=post_data, headers=header)
        except Exception as e:
            return {"status" : "error", "data" : e}
        if r.status_code != 200:
            error = f"Request {OAUTH_GITHUB_TOKEN_URL} returned with unsupported status code: {r.status_code}, message: {r.text}"
            return {"status" : "error", "data" : error }
        return {"status" : "success", "data" : r.json()}
