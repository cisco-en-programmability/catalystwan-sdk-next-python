========================
device.cellular.sessions
========================


Operation: GET /dataservice/device/cellular/sessions
----------------------------------------------------


Get cellular session list from device

.. code:: python

    def create_sessions_list(
        device_id: str,
        if_name: Optional[IfNameParam] = None,
        ipv4_dns_pri: Optional[str] = None,
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
        client.device.cellular.sessions.create_sessions_list()


.. toctree::
    :maxdepth: 1

    models

