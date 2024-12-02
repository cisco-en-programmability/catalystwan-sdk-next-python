===================
device.lacp.members
===================


Operation: GET /dataservice/device/lacp/members
-----------------------------------------------


Get device lacp port channel interface table (Real Time)

.. code:: python

    def get_lacp_members(
        device_id: str,
        channel_group: Optional[str] = None,
        if_name: Optional[str] = None,
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
        client.device.lacp.members.get_lacp_members()


