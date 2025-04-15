======================
multicloud.widget.edge
======================


Operation: GET /dataservice/multicloud/widget/edge
--------------------------------------------------


Deprecated!!!

.. code:: python

    @overload
    def get() -> Any: ...


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
        client.multicloud.widget.edge.get()


Operation: GET /dataservice/multicloud/widget/edge/{edgeType}
-------------------------------------------------------------


Deprecated!!!

.. code:: python

    @overload
    def get(edge_type: str) -> Any: ...


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
        client.multicloud.widget.edge.get()


