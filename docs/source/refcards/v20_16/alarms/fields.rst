=============
alarms.fields
=============


Operation: GET /dataservice/alarms/fields
-----------------------------------------


Get fields and types

.. code:: python

    def get_alarm_data_fields() -> Any: ...


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
        client.alarms.fields.get_alarm_data_fields()


