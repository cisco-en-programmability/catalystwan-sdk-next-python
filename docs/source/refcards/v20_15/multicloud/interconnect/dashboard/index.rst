=================================
multicloud.interconnect.dashboard
=================================


Operation: GET /dataservice/multicloud/interconnect/dashboard
-------------------------------------------------------------


API to retrieve Multicloud Interconnect dashboard view.

.. code:: python

    def get() -> List[InterconnectDashboard]: ...


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
        client.multicloud.interconnect.dashboard.get()


.. toctree::
    :maxdepth: 1

    models

