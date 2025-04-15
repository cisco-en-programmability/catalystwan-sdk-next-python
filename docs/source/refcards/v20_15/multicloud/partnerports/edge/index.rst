============================
multicloud.partnerports.edge
============================


Operation: GET /dataservice/multicloud/partnerports/edge
--------------------------------------------------------


Deprecated!!!

Get partner ports

.. code:: python

    def get(
        edge_type: Optional[EdgeTypeParam] = None,
        account_id: Optional[str] = None,
        cloud_type: Optional[str] = None,
        connect_type: Optional[str] = None,
        vxc_permitted: Optional[str] = None,
        authorization_key: Optional[str] = None,
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
        client.multicloud.partnerports.edge.get()


.. toctree::
    :maxdepth: 1

    models

