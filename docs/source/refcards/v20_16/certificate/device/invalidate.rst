=============================
certificate.device.invalidate
=============================


Operation: POST /dataservice/certificate/device/invalidate
----------------------------------------------------------


invalidate the device

.. code:: python

    def invalidate_device(payload: Optional[Any] = None) -> str: ...


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
        client.certificate.device.invalidate.invalidate_device()


