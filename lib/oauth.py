from abc import ABC, abstractmethod


class Oauth(ABC):

    @abstractmethod
    def fetch_credentials(self, *args, **kwargs):
        pass

