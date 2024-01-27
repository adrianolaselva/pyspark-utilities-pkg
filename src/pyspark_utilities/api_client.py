"""Module api_client"""

from requests import Session
from pandas import DataFrame

from pyspark_utilities.serializations import DataSerializer, DataFrameSerializer


class ApiClient:
    """
    Class api client
    """

    def __init__(self,
                 base_url: str = "https://api.thecatapi.com",
                 data_serializer: DataSerializer = DataFrameSerializer()):
        self.base_url = base_url
        self.data_serializer = data_serializer

        self.session = Session()
        self.session.headers.update({
            'Content-Type': 'application/json'
        })

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

    def build_response(self, data: dict) -> DataFrame:
        return self.data_serializer.serialize(data)

