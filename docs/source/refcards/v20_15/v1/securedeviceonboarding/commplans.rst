===================================
v1.securedeviceonboarding.commplans
===================================


Operation: GET /dataservice/v1/securedeviceonboarding/{accountId}/commplans
---------------------------------------------------------------------------


Get communication plans by account Id

.. code:: python

    def get_comm_plans_by_acct_id(account_id: str) -> None: ...


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
        client.v1.securedeviceonboarding.commplans.get_comm_plans_by_acct_id()


