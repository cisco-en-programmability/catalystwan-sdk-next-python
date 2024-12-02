=======================
stream.device.umts.save
=======================


Operation: POST /dataservice/stream/device/umts/{deviceUUID}/save
-----------------------------------------------------------------


Save UMTS Data, this api is called by device side

.. code:: python

    def save_umts_data(
        device_uuid: str, payload: Optional[Any] = None
    ) -> str: ...


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
        client.stream.device.umts.save.save_umts_data()


