==========
event.page
==========


Operation: GET /dataservice/event/page
--------------------------------------


Get paginated events

.. code:: python

    def get_page_1(
        query: str,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        site_id: Optional[str] = None,
    ) -> List[Alarm]: ...


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
        client.event.page.get_page_1()


Operation: POST /dataservice/event/page
---------------------------------------


Get paginated events

.. code:: python

    def post_page_1(
        payload: Optional[Any] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        site_id: Optional[str] = None,
    ) -> List[Alarm]: ...


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
        client.event.page.post_page_1()


.. toctree::
    :maxdepth: 1

    models

