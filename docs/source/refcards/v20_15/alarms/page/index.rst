===========
alarms.page
===========


Operation: GET /dataservice/alarms/page
---------------------------------------


Get paginated alarms

.. code:: python

    def get_page(
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
        client.alarms.page.get_page()


Operation: POST /dataservice/alarms/page
----------------------------------------


Get paginated alarm raw data

.. code:: python

    def post_page(
        payload: Optional[Any] = None,
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
        client.alarms.page.post_page()


.. toctree::
    :maxdepth: 1

    models

