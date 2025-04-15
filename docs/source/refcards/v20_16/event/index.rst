=====
event
=====


Operation: GET /dataservice/event
---------------------------------


Get events for given query. If query is empty then last 30 mins data will be returned.

.. code:: python

    def get(
        query: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        site_id: Optional[str] = None,
        include_tenants: Optional[bool] = None,
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
        client.event.get()


Operation: POST /dataservice/event
----------------------------------


Get events for given query.

.. code:: python

    def post(
        payload: Any,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        site_id: Optional[str] = None,
        include_tenants: Optional[bool] = None,
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
        client.event.post()


.. toctree::
    :maxdepth: 1

    aggregation/index
    byuuids
    component/index
    doccount
    enable/index
    get_events_by_component/index
    listeners
    page/index
    query/index
    severity/index
    types/index

