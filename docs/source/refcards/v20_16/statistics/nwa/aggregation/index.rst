==========================
statistics.nwa.aggregation
==========================


Operation: POST /dataservice/statistics/nwa/aggregation
-------------------------------------------------------


Get network availability aggregated data based on input query and filters.

.. code:: python

    def post(payload: Any) -> List[NetworkAvailabilityResp]: ...


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
        client.statistics.nwa.aggregation.post()


.. toctree::
    :maxdepth: 1

    models

