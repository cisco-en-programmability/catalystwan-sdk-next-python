=====
event
=====


Operation: GET /dataservice/event
---------------------------------


Get events for given query. If query is empty then last 30 mins data will be returned.

.. code:: python

    def get_events(
        query: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
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
        client.event.get_events()


Operation: POST /dataservice/event
----------------------------------


Get events for given query.

.. code:: python

    def post_events(
        payload: Optional[Any] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
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
        client.event.post_events()


.. toctree::
    :maxdepth: 1

    aggregation/index
    component/index
    doccount
    enable/index
    get_events_by_component/index
    listeners
    page/index
    query/index
    severity/index
    types/index

