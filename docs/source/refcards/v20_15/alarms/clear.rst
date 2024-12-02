============
alarms.clear
============


Operation: POST /dataservice/alarms/clear
-----------------------------------------


Clear the alarm for a specific UUID.

.. code:: python

    def clear_stale_alarm(payload: Optional[Any] = None) -> Any: ...


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
        client.alarms.clear.clear_stale_alarm()


