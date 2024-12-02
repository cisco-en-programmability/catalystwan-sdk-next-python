==============================================
msla.monitoring.packaging_distribution_details
==============================================


Operation: GET /dataservice/msla/monitoring/packagingDistributionDetails
------------------------------------------------------------------------


Get all license distribution

.. code:: python

    def get_packaging_distribution_details() -> PackagingDistribution: ...


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
        client.msla.monitoring.packaging_distribution_details.get_packaging_distribution_details()


.. toctree::
    :maxdepth: 1

    models

