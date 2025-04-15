======================
statistics.nwa.details
======================


Operation: POST /dataservice/statistics/nwa/details
---------------------------------------------------


Get network availability aggregated data with details based on input query and filters.

.. code:: python

    def post(
        payload: Any, include_prev: Optional[bool] = False
    ) -> List[NetworkAvailabilityResp]: ...


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
        client.statistics.nwa.details.post()


.. toctree::
    :maxdepth: 1

    models

