====================================
device.utd.signature.version.details
====================================


Operation: GET /dataservice/device/utd/signature/version/details
----------------------------------------------------------------


Get UTD Signature version information from Device

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.device.utd.signature.version.details.get()


