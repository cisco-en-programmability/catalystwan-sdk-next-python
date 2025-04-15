=============
event.byuuids
=============


Operation: POST /dataservice/event/byuuids
------------------------------------------


Get Events for given uuids

.. code:: python

    def post(
        payload: List[None], time_filter: Optional[str] = None
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
        client.event.byuuids.post()


