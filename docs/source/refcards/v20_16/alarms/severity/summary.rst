=======================
alarms.severity.summary
=======================


Operation: GET /dataservice/alarms/severity/summary
---------------------------------------------------


Get alarm severity histogram

.. code:: python

    def get(query: str, site_id: Optional[str] = None) -> Any: ...


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
        client.alarms.severity.summary.get()


