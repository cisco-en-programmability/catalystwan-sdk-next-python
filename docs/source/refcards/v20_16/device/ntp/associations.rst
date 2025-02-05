=======================
device.ntp.associations
=======================


Operation: GET /dataservice/device/ntp/associations
---------------------------------------------------


Get NTP peer associations list from device (Real Time)

.. code:: python

    def create_associations_list(device_id: str) -> List[Any]: ...


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
        client.device.ntp.associations.create_associations_list()


