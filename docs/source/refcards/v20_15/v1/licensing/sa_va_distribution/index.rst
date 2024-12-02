===============================
v1.licensing.sa_va_distribution
===============================


Operation: POST /dataservice/v1/licensing/sa-va-distribution
------------------------------------------------------------


Get Smart account and virtual account distribution of selected licenses

.. code:: python

    def get_sava_distribution(
        payload: Optional[SaVaDistributionRequest] = None,
    ) -> SaVaDistributionResponse: ...


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
        client.v1.licensing.sa_va_distribution.get_sava_distribution()


.. toctree::
    :maxdepth: 1

    models

