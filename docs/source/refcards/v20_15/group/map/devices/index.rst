=================
group.map.devices
=================


Operation: GET /dataservice/group/map/devices
---------------------------------------------


Retrieve group devices for map

.. code:: python

    def get(
        group_id: Optional[str] = None,
        vpn_id: Optional[List[Vpnid]] = None,
    ) -> None: ...


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
        client.group.map.devices.get()


.. toctree::
    :maxdepth: 1

    links
    models

