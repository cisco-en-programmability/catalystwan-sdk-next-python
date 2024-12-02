=======================
device.history.doccount
=======================


Operation: GET /dataservice/device/history/doccount
---------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_20(query: str) -> Any: ...


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
        client.device.history.doccount.get_count_20()


Operation: POST /dataservice/device/history/doccount
----------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_20(payload: Optional[Any] = None) -> Any: ...


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
        client.device.history.doccount.get_count_post_20()


