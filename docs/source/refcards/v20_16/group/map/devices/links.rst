=======================
group.map.devices.links
=======================


Operation: GET /dataservice/group/map/devices/links
---------------------------------------------------


Retrieve devices in group for map

.. code:: python

    def list_group_links_for_map(
        group_id: Optional[str] = None,
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
        client.group.map.devices.links.list_group_links_for_map()


