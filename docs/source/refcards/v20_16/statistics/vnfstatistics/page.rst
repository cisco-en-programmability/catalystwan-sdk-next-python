=============================
statistics.vnfstatistics.page
=============================


Operation: GET /dataservice/statistics/vnfstatistics/page
---------------------------------------------------------


Get stats raw data

.. code:: python

    def get(
        query: Optional[str] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> Any: ...


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
        client.statistics.vnfstatistics.page.get()


Operation: POST /dataservice/statistics/vnfstatistics/page
----------------------------------------------------------


Get stats raw data

.. code:: python

    def post(
        payload: Any,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> Any: ...


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
        client.statistics.vnfstatistics.page.post()


