============
admin.events
============


Operation: GET /dataservice/admin/events/{sseSessionId}
-------------------------------------------------------


.. code:: python

    def get(sse_session_id: str) -> None: ...


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
        client.admin.events.get()


