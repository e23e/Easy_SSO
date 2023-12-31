import os

OAUTH_GITHUB_CLIENT_ID = os.getenv("OAUTH_GITHUB_CLIENT_ID")
OAUTH_GITHUB_CLIENT_SECRET = os.getenv("OAUTH_GITHUB_CLIENT_SECRET")
OAUTH_GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"

OAUTH_SERVICE_PORT = os.getenv("OAUTH_SERVICE_PORT", 8080)
