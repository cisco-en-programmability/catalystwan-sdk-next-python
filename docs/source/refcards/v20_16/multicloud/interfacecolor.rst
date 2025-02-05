=========================
multicloud.interfacecolor
=========================


Operation: GET /dataservice/multicloud/interfacecolor
-----------------------------------------------------


Get WAN interface colors

.. code:: python

    def get_wan_interface_colors() -> List[str]: ...


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
        client.multicloud.interfacecolor.get_wan_interface_colors()


