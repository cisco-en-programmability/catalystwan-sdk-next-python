==========================
statistics.device.doccount
==========================


Operation: GET /dataservice/statistics/device/doccount
------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_15(query: str) -> Any: ...


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
        client.statistics.device.doccount.get_count_15()


Operation: POST /dataservice/statistics/device/doccount
-------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_16(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.device.doccount.get_count_post_16()


