=========================
device.interface.trustsec
=========================


Operation: GET /dataservice/device/interface/trustsec
-----------------------------------------------------


Get policy filter memory usage from device

.. code:: python

    def trustsec(device_id: str) -> Any: ...


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
        client.device.interface.trustsec.trustsec()


