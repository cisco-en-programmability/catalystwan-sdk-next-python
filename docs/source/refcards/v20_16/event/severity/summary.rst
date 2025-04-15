======================
event.severity.summary
======================


Operation: GET /dataservice/event/severity/summary
--------------------------------------------------


Get event severity histogram

.. code:: python

    def get(
        device_id: List[str],
        query: Optional[str] = None,
        site_id: Optional[str] = None,
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
        client.event.severity.summary.get()


