======================================
multicloud.devicelink.metro_speed.edge
======================================


Operation: POST /dataservice/multicloud/devicelink/metroSpeed/edge
------------------------------------------------------------------


Deprecated!!!

Get Device Link Metro Speed based on device link config

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.multicloud.devicelink.metro_speed.edge.post()


