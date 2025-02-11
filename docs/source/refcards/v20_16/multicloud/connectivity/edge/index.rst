============================
multicloud.connectivity.edge
============================


Operation: GET /dataservice/multicloud/connectivity/edge
--------------------------------------------------------


Deprecated!!!

Get Interconnect Connectivity details

.. code:: python

    def get_edge_connectivity_details(
        edge_type: Optional[EdgeTypeParam] = None,
        connectivity_name: Optional[str] = None,
        connectivity_type: Optional[str] = None,
        edge_gateway_name: Optional[str] = None,
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
        client.multicloud.connectivity.edge.get_edge_connectivity_details()


Operation: PUT /dataservice/multicloud/connectivity/edge
--------------------------------------------------------


Deprecated!!!

Update Interconnect connectivity

.. code:: python

    def update_edge_connectivity(
        payload: Optional[Any] = None,
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
        client.multicloud.connectivity.edge.update_edge_connectivity()


Operation: POST /dataservice/multicloud/connectivity/edge
---------------------------------------------------------


Deprecated!!!

Create Interconnect connectivity

.. code:: python

    def create_edge_connectivity(
        payload: Optional[Any] = None,
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
        client.multicloud.connectivity.edge.create_edge_connectivity()


Operation: DELETE /dataservice/multicloud/connectivity/edge/{connectionName}
----------------------------------------------------------------------------


Deprecated!!!

Delete Interconnect connectivity

.. code:: python

    def delete_edge_connectivity(
        connection_name: str, delete_cloud_resources: Optional[str] = None
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
        client.multicloud.connectivity.edge.delete_edge_connectivity()


Operation: GET /dataservice/multicloud/connectivity/edge/{connectivityName}
---------------------------------------------------------------------------


Deprecated!!!

Get Interconnect Connectivity by name

.. code:: python

    def get_edge_connectivity_detail_by_name(
        connectivity_name: str,
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
        client.multicloud.connectivity.edge.get_edge_connectivity_detail_by_name()


.. toctree::
    :maxdepth: 1

    models

