==========================
network.connectionssummary
==========================


Operation: GET /dataservice/network/connectionssummary
------------------------------------------------------


Retrieve vManage control status

.. code:: python

    def get(
        is_cached: Optional[bool] = False,
        vpn_id: Optional[List[Vpnid]] = None,
        site_id: Optional[str] = None,
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
        client.network.connectionssummary.get()


.. toctree::
    :maxdepth: 1

    models

