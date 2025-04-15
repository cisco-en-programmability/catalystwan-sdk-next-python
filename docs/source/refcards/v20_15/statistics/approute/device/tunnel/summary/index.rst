=========================================
statistics.approute.device.tunnel.summary
=========================================


Operation: GET /dataservice/statistics/approute/device/tunnel/summary
---------------------------------------------------------------------


Get statistics for top applications per tunnel in a grid table

.. code:: python

    def get(
        query: Optional[str] = None,
    ) -> List[AppRouteTunnenSummarResp]: ...


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
        client.statistics.approute.device.tunnel.summary.get()


.. toctree::
    :maxdepth: 1

    models

