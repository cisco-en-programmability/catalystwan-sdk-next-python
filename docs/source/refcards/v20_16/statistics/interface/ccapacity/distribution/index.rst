===========================================
statistics.interface.ccapacity.distribution
===========================================


Operation: GET /dataservice/statistics/interface/ccapacity/distribution
-----------------------------------------------------------------------


Get bandwidth distribution

.. code:: python

    def get_bandwidth_distribution(
        site_id: Optional[str] = None,
    ) -> CapacityResp: ...


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
        client.statistics.interface.ccapacity.distribution.get_bandwidth_distribution()


.. toctree::
    :maxdepth: 1

    models

