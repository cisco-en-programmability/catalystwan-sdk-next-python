===========
alarms.uuid
===========


Operation: GET /dataservice/alarms/uuid/{alarm_uuid}
----------------------------------------------------


Get alarm details for given UUID

.. code:: python

    def get_alarm_details(alarm_uuid: str) -> AlarmResponse: ...


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
        client.alarms.uuid.get_alarm_details()


.. toctree::
    :maxdepth: 1

    models

