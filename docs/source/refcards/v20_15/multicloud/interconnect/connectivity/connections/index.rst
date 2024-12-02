================================================
multicloud.interconnect.connectivity.connections
================================================


Operation: GET /dataservice/multicloud/interconnect/connectivity/connections
----------------------------------------------------------------------------


API to retrieve all exisiting Interconnect connectivity.

.. code:: python

    def get_interconnect_connectivitys(
        interconnect_type: Optional[str] = None,
        interconnect_gateway_name: Optional[str] = None,
        connection_name: Optional[str] = None,
        connection_type: Optional[str] = None,
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
        client.multicloud.interconnect.connectivity.connections.get_interconnect_connectivitys()


Operation: POST /dataservice/multicloud/interconnect/connectivity/connections
-----------------------------------------------------------------------------


API to create a private transit or cloud connection on an Interconnect Gateway at an Interconnect Provider.

.. code:: python

    def create_interconnect_connectivity(
        payload: Optional[Any] = None,
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
        client.multicloud.interconnect.connectivity.connections.create_interconnect_connectivity()


Operation: GET /dataservice/multicloud/interconnect/connectivity/connections/{connection-name}
----------------------------------------------------------------------------------------------


API to retrieve an exisiting Interconnect connectivity.

.. code:: python

    def get_interconnect_connectivity(connection_name: str) -> Any: ...


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
        client.multicloud.interconnect.connectivity.connections.get_interconnect_connectivity()


Operation: PUT /dataservice/multicloud/interconnect/connectivity/connections/{connection-name}
----------------------------------------------------------------------------------------------


API to update an Interconnect connectivity at an Interconnect provider.

.. code:: python

    def update_interconnect_connectivity(
        connection_name: str, payload: Optional[Any] = None
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
        client.multicloud.interconnect.connectivity.connections.update_interconnect_connectivity()


Operation: DELETE /dataservice/multicloud/interconnect/connectivity/connections/{connection-name}
-------------------------------------------------------------------------------------------------


API to delete an Interconnect connectivity at an Interconnect provider.

.. code:: python

    def delete_interconnect_connectivity(
        connection_name: str,
        delete_cloud_resources: Optional[str] = "false",
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
        client.multicloud.interconnect.connectivity.connections.delete_interconnect_connectivity()


.. toctree::
    :maxdepth: 1

    tags/index
    models

