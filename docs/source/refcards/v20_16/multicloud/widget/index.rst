=================
multicloud.widget
=================


Operation: GET /dataservice/multicloud/widget
---------------------------------------------


.. code:: python

    @overload
    def get() -> List[CloudWidget]: ...


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
        client.multicloud.widget.get()


Operation: GET /dataservice/multicloud/widget/{cloudType}
---------------------------------------------------------


.. code:: python

    @overload
    def get(cloud_type: str) -> CloudWidget: ...


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
        client.multicloud.widget.get()


.. toctree::
    :maxdepth: 1

    edge
    models

