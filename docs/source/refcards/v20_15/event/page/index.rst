==========
event.page
==========


Operation: GET /dataservice/event/page
--------------------------------------


Get paginated events

.. code:: python

    def get(
        query: str,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        site_id: Optional[str] = None,
    ) -> AlarmResponse: ...


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
        client.event.page.get()


Operation: POST /dataservice/event/page
---------------------------------------


Get paginated events

.. code:: python

    def post(
        payload: Any,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        site_id: Optional[str] = None,
    ) -> AlarmResponse: ...


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
        client.event.page.post()


.. toctree::
    :maxdepth: 1

    models

