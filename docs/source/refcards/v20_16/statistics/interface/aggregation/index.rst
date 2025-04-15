================================
statistics.interface.aggregation
================================


Operation: GET /dataservice/statistics/interface/aggregation
------------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def get(query: str) -> List[InterfaceAggRespWithPageInfo]: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.statistics.interface.aggregation.get()


Operation: POST /dataservice/statistics/interface/aggregation
-------------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def post(payload: Any) -> List[InterfaceAggResp]: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.statistics.interface.aggregation.post()


.. toctree::
    :maxdepth: 1

    models

