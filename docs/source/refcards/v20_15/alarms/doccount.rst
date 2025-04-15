===============
alarms.doccount
===============


Operation: GET /dataservice/alarms/doccount
-------------------------------------------


Get the count of alarms as per the query passed.

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
        client.alarms.doccount.get()


Operation: POST /dataservice/alarms/doccount
--------------------------------------------


Get the count of alarms as per the query passed.

.. code:: python

    def post(payload: Any, site_id: Optional[str] = None) -> Any: ...


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
        client.alarms.doccount.post()


