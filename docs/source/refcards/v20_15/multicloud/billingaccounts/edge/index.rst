===============================
multicloud.billingaccounts.edge
===============================


Operation: GET /dataservice/multicloud/billingaccounts/edge/{edgeType}/{edgeAccountId}
--------------------------------------------------------------------------------------


Deprecated!!!

Get Edge Billing Accounts

.. code:: python

    def get_edge_billing_accounts(
        edge_type: EdgeTypeParam,
        edge_account_id: str,
        region: Optional[str] = None,
    ) -> Any: ...


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
        client.multicloud.billingaccounts.edge.get_edge_billing_accounts()


.. toctree::
    :maxdepth: 1

    models

