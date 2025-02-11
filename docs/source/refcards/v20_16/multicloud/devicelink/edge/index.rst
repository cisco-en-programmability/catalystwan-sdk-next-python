==========================
multicloud.devicelink.edge
==========================


Operation: GET /dataservice/multicloud/devicelink/edge
------------------------------------------------------


Deprecated!!!

Get Device Links

.. code:: python

    def get_device_links(
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
        client.multicloud.devicelink.edge.get_device_links()


Operation: PUT /dataservice/multicloud/devicelink/edge
------------------------------------------------------


Deprecated!!!

Update Device Link

.. code:: python

    def update_device_link(payload: Optional[Any] = None) -> Any: ...


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
        client.multicloud.devicelink.edge.update_device_link()


Operation: POST /dataservice/multicloud/devicelink/edge
-------------------------------------------------------


Deprecated!!!

Create Device Link

.. code:: python

    def create_device_link(payload: Optional[Any] = None) -> Any: ...


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
        client.multicloud.devicelink.edge.create_device_link()


Operation: DELETE /dataservice/multicloud/devicelink/edge/{deviceLinkName}
--------------------------------------------------------------------------


Deprecated!!!

Delete Device Link

.. code:: python

    def delete_device_link(device_link_name: str) -> Any: ...


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
        client.multicloud.devicelink.edge.delete_device_link()


.. toctree::
    :maxdepth: 1

    portspeed/index
    models

