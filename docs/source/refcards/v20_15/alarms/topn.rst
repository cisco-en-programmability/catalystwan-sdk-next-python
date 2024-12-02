===========
alarms.topn
===========


Operation: POST /dataservice/alarms/topn
----------------------------------------


Returns top-n alarm count based on given query

.. code:: python

    def get_top_n(
        payload: Optional[Any] = None, site_id: Optional[str] = None
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
        client.alarms.topn.get_top_n()


