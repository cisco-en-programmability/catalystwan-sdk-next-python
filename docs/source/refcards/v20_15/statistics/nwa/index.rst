==============
statistics.nwa
==============


Operation: POST /dataservice/statistics/nwa
-------------------------------------------


Get network availability raw data based on input query and filters.

.. code:: python

    def post(
        query: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
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
        client.statistics.nwa.post()


.. toctree::
    :maxdepth: 1

    aggregation/index
    details/index
    models

