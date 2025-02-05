=========================
device.ipsec.pwk.outbound
=========================


Operation: GET /dataservice/device/ipsec/pwk/outbound
-----------------------------------------------------


Get IPSEC pairwise key outbound entry from device

.. code:: python

    def create_i_psec_pwk_outbound_connections(
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
        client.device.ipsec.pwk.outbound.create_i_psec_pwk_outbound_connections()


.. toctree::
    :maxdepth: 1

    models

