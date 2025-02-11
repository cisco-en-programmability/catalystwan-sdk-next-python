============
alarms.count
============


Operation: GET /dataservice/alarms/count
----------------------------------------


Get the count of alarms which are active and not acknowledged by user.

.. code:: python

    def get_non_viewed_active_alarms_count(
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
        client.alarms.count.get_non_viewed_active_alarms_count()


Operation: POST /dataservice/alarms/count
-----------------------------------------


Get the count of alarms as per the query passed.

.. code:: python

    def post_count(
        payload: Optional[Any] = None,
        site_id: Optional[str] = None,
        include_tenants: Optional[bool] = None,
    ) -> List[AlarmCountPost]: ...


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
        client.alarms.count.post_count()


.. toctree::
    :maxdepth: 1

    models

