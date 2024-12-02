=============================
stream.device.umts.statistics
=============================


Operation: GET /dataservice/stream/device/umts/statistics/{deviceUUID}/{eventType}
----------------------------------------------------------------------------------


get UMTS result by type, time, and device uuid

.. code:: python

    def get_umts_data(
        device_uuid: str,
        event_type: str,
        last_n_hours: Optional[int] = 24,
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
        client.stream.device.umts.statistics.get_umts_data()


