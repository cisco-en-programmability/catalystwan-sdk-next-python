===============
sig.datacenters
===============


Operation: GET /dataservice/sig/datacenters/{type}/{tunneltype}
---------------------------------------------------------------


.. code:: python

    @overload
    def get(type_: str, tunneltype: str) -> GetDataCenters: ...


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
        client.sig.datacenters.get()


Operation: GET /dataservice/sig/datacenters/{type}/{tunneltype}/{devicetype}
----------------------------------------------------------------------------


.. code:: python

    @overload
    def get(type_: str, tunneltype: str, devicetype: str) -> Any: ...


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
        client.sig.datacenters.get()


.. toctree::
    :maxdepth: 1

    models

