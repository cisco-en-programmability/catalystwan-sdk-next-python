=============================================
msla.monitoring.licensed_distribution_details
=============================================


Operation: GET /dataservice/msla/monitoring/licensedDistributionDetails
-----------------------------------------------------------------------


Get all license distribution

.. code:: python

    def get() -> LicenseDistribution: ...


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
        client.msla.monitoring.licensed_distribution_details.get()


.. toctree::
    :maxdepth: 1

    models

