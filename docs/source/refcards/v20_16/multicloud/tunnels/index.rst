==================
multicloud.tunnels
==================


Operation: GET /dataservice/multicloud/tunnels/{cloudType}
----------------------------------------------------------


Get the tunnels for cloudType

.. code:: python

    def get_tunnel_names(
        cloud_type: CloudTypeParam, cloud_gateway_name: str
    ) -> List[GetTunnelsResponse]: ...


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
        client.multicloud.tunnels.get_tunnel_names()


.. toctree::
    :maxdepth: 1

    models

