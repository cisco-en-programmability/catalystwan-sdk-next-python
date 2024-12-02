=================================================
multicloud.interconnect.accounts.billing_accounts
=================================================


Operation: GET /dataservice/multicloud/interconnect/{interconnect-type}/accounts/{interconnect-account-id}/billing-accounts
---------------------------------------------------------------------------------------------------------------------------


API to retrieve billing accounts for an Interconnect provider type and account.

.. code:: python

    def get_interconnect_billing_accounts(
        interconnect_type: str,
        interconnect_account_id: str,
        region: Optional[str] = None,
    ) -> InlineResponse2001: ...


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
        client.multicloud.interconnect.accounts.billing_accounts.get_interconnect_billing_accounts()


.. toctree::
    :maxdepth: 1

    models

