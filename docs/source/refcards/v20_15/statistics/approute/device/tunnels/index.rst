==================================
statistics.approute.device.tunnels
==================================


Operation: GET /dataservice/statistics/approute/device/tunnels
--------------------------------------------------------------


Get statistics for top applications per tunnel in a grid table

.. code:: python

    def get(
        query: Optional[str] = None,
    ) -> List[AppRouteRespWithPageInfo]: ...


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
        client.statistics.approute.device.tunnels.get()


.. toctree::
    :maxdepth: 1

    models

