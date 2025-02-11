==================
device.ipsec.ikev1
==================


Operation: GET /dataservice/device/ipsec/ikev1
----------------------------------------------


Get Crypto IKEv1 SA entry from device

.. code:: python

    def create_cryptov1_local_sa_list(
        device_id: str,
        remote_tloc_address: Optional[str] = None,
        remote_tloc_color: Optional[RemoteTlocColorParam] = None,
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
        client.device.ipsec.ikev1.create_cryptov1_local_sa_list()


.. toctree::
    :maxdepth: 1

    models

