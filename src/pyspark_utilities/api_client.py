"""Module api_client"""

from requests import Session
from pandas import DataFrame


class ApiClient:
    """
    Class api client
    """

    def __init__(self, base_url: str = "https://api.thecatapi.com", headers: dict = None):
        self.session = Session()
        self.base_url = base_url
        self.session.headers.update({
            'Content-Type': 'application/json'
        })

        if headers is not None:
            self.session.headers.update(headers)

    def make_request(self, method: str, endpoint: str, params=None, data=None):
        """
        Make request method

        :param method:
        :param endpoint:
        :param params:
        :param data:
        :return:
        """

        return self.session.request(method,
                                    url=f"{self.base_url}/{endpoint}",
                                    params=params,
                                    data=data)

    def build_response(self, result: dict) -> DataFrame:
        return DataFrame(result)

