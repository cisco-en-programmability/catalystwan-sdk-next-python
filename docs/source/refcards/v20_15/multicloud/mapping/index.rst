==================
multicloud.mapping
==================


Operation: GET /dataservice/multicloud/mapping/{cloudType}
----------------------------------------------------------


Get associated mappings to the CGW

.. code:: python

    def get(
        cloud_type: str,
        cloud_gateway_name: str,
        site_uuid: Optional[str] = None,
    ) -> CgwVpnsResponse: ...


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
        client.multicloud.mapping.get()


.. toctree::
    :maxdepth: 1

    models

