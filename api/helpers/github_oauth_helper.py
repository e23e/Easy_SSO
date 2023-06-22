from lib.github_oauth import Github_oauth
from lib.queue import Queue


class Github_Helper:

    @staticmethod
    def process_credentials(code: str):
        data_with_status = Github_oauth().fetch_credentials(code=code)
        Queue(data_with_status)
        
