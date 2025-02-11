===================================
v1.securedeviceonboarding.rateplans
===================================


Operation: GET /dataservice/v1/securedeviceonboarding/rateplans
---------------------------------------------------------------


Get rate plans by account Id

.. code:: python

    def get_rate_plans_by_acct_id(
        account_id: str,
    ) -> RatePlansResponse: ...


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
        client.v1.securedeviceonboarding.rateplans.get_rate_plans_by_acct_id()


.. toctree::
    :maxdepth: 1

    models

