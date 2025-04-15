===============================
multicloud.accounts.credentials
===============================


Operation: PUT /dataservice/multicloud/accounts/{accountId}/credentials
-----------------------------------------------------------------------


Update Cloud Account Credentials

.. code:: python

    def put(
        account_id: str, payload: PostAccounts
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
        client.multicloud.accounts.credentials.put()


.. toctree::
    :maxdepth: 1

    models

