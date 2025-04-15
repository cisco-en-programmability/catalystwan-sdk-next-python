==============================================================
multicloud.interconnect.connectivity.virtual_cross_connections
==============================================================


Operation: GET /dataservice/multicloud/interconnect/connectivity/virtual-cross-connections
------------------------------------------------------------------------------------------


API to retrieve all exisiting Interconnect virtual cross connections.

.. code:: python

    def get_interconnect_cross_connections(
        interconnect_type: Optional[str] = None,
        interconnect_gateway_name: Optional[str] = None,
        connection_name: Optional[str] = None,
        connection_type: Optional[str] = None,
        cloud_type: Optional[str] = None,
        refresh: Optional[str] = "false",
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
        client.multicloud.interconnect.connectivity.virtual_cross_connections.get_interconnect_cross_connections()


Operation: POST /dataservice/multicloud/interconnect/connectivity/virtual-cross-connections
-------------------------------------------------------------------------------------------


API to create an Interconnect virtual cross connection on an Interconnect Gateway at an Interconnect Provider.

.. code:: python

    def post(
        payload: List[InterconnectCrossConnection],
    ) -> ProcessResponse: ...


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
        client.multicloud.interconnect.connectivity.virtual_cross_connections.post()


Operation: GET /dataservice/multicloud/interconnect/connectivity/virtual-cross-connections/{connection-name}
------------------------------------------------------------------------------------------------------------


API to retrieve an exisiting Interconnect virtual cross connection.

.. code:: python

    def get(connection_name: str) -> Any: ...


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
        client.multicloud.interconnect.connectivity.virtual_cross_connections.get()


Operation: PUT /dataservice/multicloud/interconnect/connectivity/virtual-cross-connections/{connection-name}
------------------------------------------------------------------------------------------------------------


API to update a virtual cross connection connection on an Interconnect Gateway at an Interconnect Provider.

.. code:: python

    def put(
        connection_name: str, payload: InterconnectCrossConnection
    ) -> ProcessResponse: ...


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
        client.multicloud.interconnect.connectivity.virtual_cross_connections.put()


Operation: DELETE /dataservice/multicloud/interconnect/connectivity/virtual-cross-connections/{connection-name}
---------------------------------------------------------------------------------------------------------------


API to delete an Interconnect virtual cross connection at an Interconnect provider.

.. code:: python

    def delete(connection_name: str) -> ProcessResponse: ...


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
        client.multicloud.interconnect.connectivity.virtual_cross_connections.delete()


.. toctree::
    :maxdepth: 1

    models

