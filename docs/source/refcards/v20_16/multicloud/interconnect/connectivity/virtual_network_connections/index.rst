================================================================
multicloud.interconnect.connectivity.virtual_network_connections
================================================================


Operation: GET /dataservice/multicloud/interconnect/connectivity/virtual-network-connections
--------------------------------------------------------------------------------------------


API to retrieve all exisiting Interconnect virtual network connections.

.. code:: python

    def get_interconnect_virtual_network_connections(
        connection_name: Optional[str] = None,
        cloud_type: Optional[str] = None,
        cloud_account_id: Optional[str] = None,
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
        client.multicloud.interconnect.connectivity.virtual_network_connections.get_interconnect_virtual_network_connections()


Operation: POST /dataservice/multicloud/interconnect/connectivity/virtual-network-connections
---------------------------------------------------------------------------------------------


API to create a Interconnect virtual network connection between virtual network Tags and OnRamp gateway connection.

.. code:: python

    def post(
        payload: List[InterconnectVirtualNetworkConnection],
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
        client.multicloud.interconnect.connectivity.virtual_network_connections.post()


Operation: GET /dataservice/multicloud/interconnect/connectivity/virtual-network-connections/{connection-name}
--------------------------------------------------------------------------------------------------------------


API to retrieve an exisiting Interconnect Interconnect virtual network connection.

.. code:: python

    def get(
        connection_name: str,
    ) -> InterconnectVirtualNetworkConnection: ...


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
        client.multicloud.interconnect.connectivity.virtual_network_connections.get()


Operation: PUT /dataservice/multicloud/interconnect/connectivity/virtual-network-connections/{connection-name}
--------------------------------------------------------------------------------------------------------------


API to update a virtual network connection between virtual network Tags and onRamp gateway connection.

.. code:: python

    def put(
        connection_name: str,
        payload: InterconnectVirtualNetworkConnection,
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
        client.multicloud.interconnect.connectivity.virtual_network_connections.put()


Operation: DELETE /dataservice/multicloud/interconnect/connectivity/virtual-network-connections/{connection-name}
-----------------------------------------------------------------------------------------------------------------


API to delete an Interconnect virtual network connection.

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
        client.multicloud.interconnect.connectivity.virtual_network_connections.delete()


.. toctree::
    :maxdepth: 1

    models

