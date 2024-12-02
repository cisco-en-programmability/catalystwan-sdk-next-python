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

    def create_interconnect_cross_connection(
        payload: Optional[List[InterconnectCrossConnection]] = None,
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
        client.multicloud.interconnect.connectivity.virtual_cross_connections.create_interconnect_cross_connection()


Operation: GET /dataservice/multicloud/interconnect/connectivity/virtual-cross-connections/{connection-name}
------------------------------------------------------------------------------------------------------------


API to retrieve an exisiting Interconnect virtual cross connection.

.. code:: python

    def get_interconnect_cross_connection(
        connection_name: str,
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
        client.multicloud.interconnect.connectivity.virtual_cross_connections.get_interconnect_cross_connection()


Operation: PUT /dataservice/multicloud/interconnect/connectivity/virtual-cross-connections/{connection-name}
------------------------------------------------------------------------------------------------------------


API to update a virtual cross connection connection on an Interconnect Gateway at an Interconnect Provider.

.. code:: python

    def update_interconnect_cross_connection(
        connection_name: str,
        payload: Optional[InterconnectCrossConnection] = None,
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
        client.multicloud.interconnect.connectivity.virtual_cross_connections.update_interconnect_cross_connection()


Operation: DELETE /dataservice/multicloud/interconnect/connectivity/virtual-cross-connections/{connection-name}
---------------------------------------------------------------------------------------------------------------


API to delete an Interconnect virtual cross connection at an Interconnect provider.

.. code:: python

    def delete_interconnect_cross_connection(
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
        client.multicloud.interconnect.connectivity.virtual_cross_connections.delete_interconnect_cross_connection()


.. toctree::
    :maxdepth: 1

    models

