==========================
multicloud.devicelink.edge
==========================


Operation: GET /dataservice/multicloud/devicelink/edge
------------------------------------------------------


Deprecated!!!

Get Device Links

.. code:: python

    def get(
        edge_type: Optional[EdgeTypeParam] = None,
        device_link_name: Optional[str] = None,
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
        client.multicloud.devicelink.edge.get()


Operation: PUT /dataservice/multicloud/devicelink/edge
------------------------------------------------------


Deprecated!!!

Update Device Link

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
        client.multicloud.devicelink.edge.put()


Operation: POST /dataservice/multicloud/devicelink/edge
-------------------------------------------------------


Deprecated!!!

Create Device Link

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
        client.multicloud.devicelink.edge.post()


Operation: DELETE /dataservice/multicloud/devicelink/edge/{deviceLinkName}
--------------------------------------------------------------------------


Deprecated!!!

Delete Device Link

.. code:: python

    def delete(device_link_name: str) -> Any: ...


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
        client.multicloud.devicelink.edge.delete()


.. toctree::
    :maxdepth: 1

    portspeed/index
    models

