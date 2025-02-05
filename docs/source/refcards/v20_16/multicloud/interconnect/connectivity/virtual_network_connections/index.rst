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

    def create_interconenct_virtual_network_connection(
        payload: Optional[
            List[InterconnectVirtualNetworkConnection]
        ] = None,
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
        client.multicloud.interconnect.connectivity.virtual_network_connections.create_interconenct_virtual_network_connection()


Operation: GET /dataservice/multicloud/interconnect/connectivity/virtual-network-connections/{connection-name}
--------------------------------------------------------------------------------------------------------------


API to retrieve an exisiting Interconnect Interconnect virtual network connection.

.. code:: python

    def get_interconnect_virtual_network_connection(
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
        client.multicloud.interconnect.connectivity.virtual_network_connections.get_interconnect_virtual_network_connection()


Operation: PUT /dataservice/multicloud/interconnect/connectivity/virtual-network-connections/{connection-name}
--------------------------------------------------------------------------------------------------------------


API to update a virtual network connection between virtual network Tags and onRamp gateway connection.

.. code:: python

    def update_interconnect_virtual_network_connection(
        connection_name: str,
        payload: Optional[InterconnectVirtualNetworkConnection] = None,
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
        client.multicloud.interconnect.connectivity.virtual_network_connections.update_interconnect_virtual_network_connection()


Operation: DELETE /dataservice/multicloud/interconnect/connectivity/virtual-network-connections/{connection-name}
-----------------------------------------------------------------------------------------------------------------


API to delete an Interconnect virtual network connection.

.. code:: python

    def delete_interconnect_virtual_network_connection(
        connection_name: str,
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
        client.multicloud.interconnect.connectivity.virtual_network_connections.delete_interconnect_virtual_network_connection()


.. toctree::
    :maxdepth: 1

    models

