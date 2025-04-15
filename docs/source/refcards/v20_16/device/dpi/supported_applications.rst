=================================
device.dpi.supported_applications
=================================


Operation: GET /dataservice/device/dpi/supported-applications
-------------------------------------------------------------


Get supported applications from device (Real Time)

.. code:: python

    def get(
        device_id: str,
        application: Optional[str] = None,
        family: Optional[str] = None,
    ) -> List[Any]: ...


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
        client.device.dpi.supported_applications.get()


