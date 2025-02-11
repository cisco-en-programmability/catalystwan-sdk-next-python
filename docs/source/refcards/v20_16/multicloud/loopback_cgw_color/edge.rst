==================================
multicloud.loopback_cgw_color.edge
==================================


Operation: GET /dataservice/multicloud/loopbackCGWColor/edge
------------------------------------------------------------


Deprecated!!!

Get Edge Loopback CGW supported colors

.. code:: python

    def get_supported_loopback_cgw_colors() -> Any: ...


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
        client.multicloud.loopback_cgw_color.edge.get_supported_loopback_cgw_colors()


