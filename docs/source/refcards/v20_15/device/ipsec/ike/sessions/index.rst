=========================
device.ipsec.ike.sessions
=========================


Operation: GET /dataservice/device/ipsec/ike/sessions
-----------------------------------------------------


Get IPsec IKE sessions from device

.. code:: python

    def create_ike_sessions(
        device_id: str,
        remote_tloc_address: Optional[str] = None,
        remote_tloc_color: Optional[RemoteTlocColorParam] = None,
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
        client.device.ipsec.ike.sessions.create_ike_sessions()


.. toctree::
    :maxdepth: 1

    models

