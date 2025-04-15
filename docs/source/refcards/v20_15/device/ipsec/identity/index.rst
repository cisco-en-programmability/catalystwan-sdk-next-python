=====================
device.ipsec.identity
=====================


Operation: GET /dataservice/device/ipsec/identity
-------------------------------------------------


Get Crypto IPSEC identity entry from device

.. code:: python

    def get(
        device_id: str,
        remote_tloc_address: Optional[str] = None,
        remote_tloc_color: Optional[RemoteTlocColorParam] = None,
        local_tloc_color: Optional[LocalTlocColorParam] = None,
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
        client.device.ipsec.identity.get()


.. toctree::
    :maxdepth: 1

    models

