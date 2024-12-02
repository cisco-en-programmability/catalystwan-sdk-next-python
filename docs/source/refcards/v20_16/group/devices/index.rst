=============
group.devices
=============


Operation: GET /dataservice/group/devices
-----------------------------------------


Retrieve devices in group

.. code:: python

    def list_group_devices(
        group_id: Optional[str] = None,
        ssh: Optional[bool] = False,
        vpn_id: Optional[List[Vpnid]] = None,
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
        client.group.devices.list_group_devices()


.. toctree::
    :maxdepth: 1

    models

