=================================
device.control.connectionshistory
=================================


Operation: GET /dataservice/device/control/connectionshistory
-------------------------------------------------------------


Get connections history list from device (Real Time)

.. code:: python

    def get(
        device_id: str,
        peer_type: Optional[PeerTypeParam] = None,
        system_ip: Optional[str] = None,
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
        client.device.control.connectionshistory.get()


.. toctree::
    :maxdepth: 1

    models

