from pyspark_utilities import ApiClient


class ImagesApi(object):
    api_client: ApiClient

    def __init__(self, api_client: ApiClient = ApiClient()):
        self.api_client = api_client

    def search(self, limit: int = 10):
        response = self.api_client.make_request(method='GET', endpoint="v1/images/search", params={
            'limit': limit
        })

        return self.api_client.build_response(response.json())
