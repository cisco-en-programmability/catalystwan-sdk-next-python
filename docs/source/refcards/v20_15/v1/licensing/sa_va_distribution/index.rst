===============================
v1.licensing.sa_va_distribution
===============================


Operation: POST /dataservice/v1/licensing/sa-va-distribution
------------------------------------------------------------


Get Smart account and virtual account distribution of selected licenses

.. code:: python

    def post(
        payload: SaVaDistributionRequest,
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
        client.v1.licensing.sa_va_distribution.post()


.. toctree::
    :maxdepth: 1

    models

