====================
device.ipsec.localsa
====================


Operation: GET /dataservice/device/ipsec/localsa
------------------------------------------------


Get IPsec local SA list from device

.. code:: python

    def create_local_sa_list(device_id: str) -> List[Any]: ...


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
        client.device.ipsec.localsa.create_local_sa_list()


