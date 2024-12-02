======================
alarms.markallasviewed
======================


Operation: POST /dataservice/alarms/markallasviewed
---------------------------------------------------


Mark all alarms as acknowledged by the user

.. code:: python

    def mark_all_alarms_as_viewed(
        payload: Optional[Any] = None, type_: Optional[str] = None
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
        client.alarms.markallasviewed.mark_all_alarms_as_viewed()


