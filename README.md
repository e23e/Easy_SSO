# Easy SSO
An tool to obtain oauth access token. This tool host an web app and make oauth process and give the access token to the user.

## Objective
Github has seperate (high) ratelimit for enterprise cloud account users with some conditions like if the request is made from an github app or with a access token generated with oauth token. To obtain the oauth token this tool has been developed. For more about github ratelimits, please refer the [doc](https://docs.github.com/en/rest/overview/resources-in-the-rest-api?apiVersion=2022-11-28#rate-limiting)

## Usage
Create virtual environment
```
python3 -m venv .venv
```
Activating virtual environment
```
source .venv/bin/activate
```
Installing Dependencies
```
pip install -r requirements.txt
```
Running the tool
```
python3 main.py
```

***Note: This tool is developed to use it in local, Please avoid using it in a publicly accessible server/instance***

### Github SSO
- Create a github oauth app and add it in the github org
    - Use `http://127.0.0.1:8080/github/callback` as Authorization callback URL
    - Generate a Client secret and set the `OAUTH_GITHUB_CLIENT_ID` and `OAUTH_GITHUB_CLIENT_SECRET` environment variables
- Create a oauth scope you need, you can refer the [doc](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps) for creating oauth scope, the token generated using this process will have access to the scope you are creating, multiple scope can be seperated by a space
- An example repo will be looks like `repo repo_deployment security_events read:org`
- Open the below url in a browser with valid scope value
    - http://127.0.0.1:8080/github/login?scope=`<created_scope_value>`
- The above url will be redirect you to complete the oauth login process
- Once you completed login,, open the below url in browser
    - http://127.0.0.1:8080/get/access_credentials
- You can see the generated token in response.

***Security concern: The endpoint `get/access_credentials` will show the oauth token generated, As this endpoint does't have any authentication, It will show the token anyone who access it, so it is better to run this tool local and exit the process once you get the oauth token***

