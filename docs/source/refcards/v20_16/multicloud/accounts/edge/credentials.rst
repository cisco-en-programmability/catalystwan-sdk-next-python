====================================
multicloud.accounts.edge.credentials
====================================


Operation: PUT /dataservice/multicloud/accounts/edge/{accountId}/credentials
----------------------------------------------------------------------------


Deprecated!!!

Update Multicloud edge account credential

.. code:: python

    def validate_edge_account_update_credentials(
        account_id: str, payload: Optional[Any] = None
    ) -> None: ...


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
        client.multicloud.accounts.edge.credentials.validate_edge_account_update_credentials()


