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

    def put(payload: Any) -> Any: ...


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
        client.multicloud.connectivity.edge.put()


Operation: POST /dataservice/multicloud/connectivity/edge
---------------------------------------------------------


Deprecated!!!

Create Interconnect connectivity

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.multicloud.connectivity.edge.post()


Operation: DELETE /dataservice/multicloud/connectivity/edge/{connectionName}
----------------------------------------------------------------------------


Deprecated!!!

Delete Interconnect connectivity

.. code:: python

    def delete(
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
        client.multicloud.connectivity.edge.delete()


Operation: GET /dataservice/multicloud/connectivity/edge/{connectivityName}
---------------------------------------------------------------------------


Deprecated!!!

Get Interconnect Connectivity by name

.. code:: python

    def get(connectivity_name: str) -> Any: ...


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
        client.multicloud.connectivity.edge.get()


.. toctree::
    :maxdepth: 1

    models

