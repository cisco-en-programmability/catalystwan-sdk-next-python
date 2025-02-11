==============
event.doccount
==============


Operation: GET /dataservice/event/doccount
------------------------------------------


Get the count of events as per the query passed.

.. code:: python

    def get_doc_count_2(
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
        client.event.doccount.get_doc_count_2()


Operation: POST /dataservice/event/doccount
-------------------------------------------


Get the count of events as per the query passed.

.. code:: python

    def post_doc_count_1(
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
        client.event.doccount.post_doc_count_1()


