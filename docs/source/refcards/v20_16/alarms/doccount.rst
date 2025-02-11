===============
alarms.doccount
===============


Operation: GET /dataservice/alarms/doccount
-------------------------------------------


Get the count of alarms as per the query passed.

.. code:: python

    def get_doc_count(
        query: str, site_id: Optional[str] = None
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
        client.alarms.doccount.get_doc_count()


Operation: POST /dataservice/alarms/doccount
--------------------------------------------


Get the count of alarms as per the query passed.

.. code:: python

    def post_doc_count(
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
        client.alarms.doccount.post_doc_count()


