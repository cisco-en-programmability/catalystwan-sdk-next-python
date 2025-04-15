=======================
statistics.flowlog.page
=======================


Operation: GET /dataservice/statistics/flowlog/page
---------------------------------------------------


Get stats pagination raw data

.. code:: python

    def get(
        query: Optional[str] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> FlowlogPaginationResponse: ...


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
        client.statistics.flowlog.page.get()


Operation: POST /dataservice/statistics/flowlog/page
----------------------------------------------------


Get stats pagination raw data

.. code:: python

    def post(
        payload: Any,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> FlowlogPaginationResponse: ...


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
        client.statistics.flowlog.page.post()


.. toctree::
    :maxdepth: 1

    models

