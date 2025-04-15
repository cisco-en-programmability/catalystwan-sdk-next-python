=======================
multicloud.license.edge
=======================


Operation: GET /dataservice/multicloud/license/edge
---------------------------------------------------


Deprecated!!!

Get License Info for Edge Gateways/Connections

.. code:: python

    def get(
        edge_type: Optional[EdgeTypeParam] = None,
        account_id: Optional[str] = None,
        product_type: Optional[ProductTypeParam] = None,
        refresh: Optional[str] = None,
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
        client.multicloud.license.edge.get()


.. toctree::
    :maxdepth: 1

    models

