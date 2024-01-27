# Pyspark utilities package

Package test...


## Example

```python
from pyspark_utilities import ApiClient
from pyspark_utilities.resources import ImagesApi

images_api = ImagesApi(api_client=ApiClient())

images_api.search(limit=10)
```

## Build library

```shell
python setup.py sdist bdist_wheel
```
> build library


```shell
pip3 install -e .
```
> install package for tests

```shell
pylint ./src
```
> run pylint
