=====================
multicloud.map.status
=====================


Operation: GET /dataservice/multicloud/map/status
-------------------------------------------------


Get mapping status

.. code:: python

    def get(
        cloud_type: str, region: Optional[str] = None
    ) -> List[MapStatus]: ...


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
        client.multicloud.map.status.get()


.. toctree::
    :maxdepth: 1

    models

