=============
schedule.list
=============


Operation: GET /dataservice/schedule/list
-----------------------------------------


Get a schedule record for backup by scheduler id

.. code:: python

    def list_schedules(limit: Optional[int] = 100) -> Any: ...


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
        client.schedule.list.list_schedules()


