===============================
multicloud.accounts.credentials
===============================


Operation: PUT /dataservice/multicloud/accounts/{accountId}/credentials
-----------------------------------------------------------------------


Update Cloud Account Credentials

.. code:: python

    def validate_account_update_credentials(
        account_id: str, payload: Optional[PostAccounts] = None
    ) -> PostAccountsResponse: ...


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
        client.multicloud.accounts.credentials.validate_account_update_credentials()


.. toctree::
    :maxdepth: 1

    models

