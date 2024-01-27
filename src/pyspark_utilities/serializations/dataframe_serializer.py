
from pyspark_utilities.serializations.data_serializer import DataSerializer

import pandas


class DataFrameSerializer(DataSerializer):
    def serialize(self, data: dict):
        return pandas.DataFrame(data)
