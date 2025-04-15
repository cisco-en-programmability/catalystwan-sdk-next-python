=========================
statistics.interface.page
=========================


Operation: GET /dataservice/statistics/interface/page
-----------------------------------------------------


Get stats raw data

.. code:: python

    def get(
        query: str, count: str, scroll_id: Optional[str] = None
    ) -> InterfaceAggRespWithPageInfo: ...


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
        client.statistics.interface.page.get()


Operation: POST /dataservice/statistics/interface/page
------------------------------------------------------


Get stats raw data

.. code:: python

    def post(
        count: str, payload: Any, scroll_id: Optional[str] = None
    ) -> InterfaceAggRespWithPageInfo: ...


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
        client.statistics.interface.page.post()


.. toctree::
    :maxdepth: 1

    models

