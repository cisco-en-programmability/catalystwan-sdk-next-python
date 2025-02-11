========================
device.ipsec.pwk.inbound
========================


Operation: GET /dataservice/device/ipsec/pwk/inbound
----------------------------------------------------


Get IPSEC pairwise key inbound entry from device

.. code:: python

    def create_i_psec_pwk_inbound_connections(
        device_id: str,
        remote_tloc_address: Optional[str] = None,
        remote_tloc_color: Optional[RemoteTlocColorParam] = None,
        local_tloc_color: Optional[RemoteTlocColorParam] = None,
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
        client.device.ipsec.pwk.inbound.create_i_psec_pwk_inbound_connections()


.. toctree::
    :maxdepth: 1

    models

