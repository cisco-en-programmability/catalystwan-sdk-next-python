=========================
multicloud.dashboard.edge
=========================


Operation: GET /dataservice/multicloud/dashboard/edge
-----------------------------------------------------


Deprecated!!!

Get interconnect edge gateway dashboard info

.. code:: python

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
        client.multicloud.dashboard.edge.get()


