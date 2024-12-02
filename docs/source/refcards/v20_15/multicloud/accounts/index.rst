===================
multicloud.accounts
===================


Operation: GET /dataservice/multicloud/accounts
-----------------------------------------------


Obtain all accounts for all clouds

.. code:: python

    def get_all_cloud_accounts(
        cloud_type: Optional[str] = None,
        cloud_gateway_enabled: Optional[str] = None,
    ) -> List[GetAccounts]: ...


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
        client.multicloud.accounts.get_all_cloud_accounts()


Operation: POST /dataservice/multicloud/accounts
------------------------------------------------


Add Cloud Account

.. code:: python

    def validate_account_add(
        payload: Optional[PostAccounts] = None,
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
        client.multicloud.accounts.validate_account_add()


Operation: GET /dataservice/multicloud/accounts/{accountId}
-----------------------------------------------------------


Obtain all accounts for all clouds

.. code:: python

    def get_cloud_account_details(account_id: str) -> GetAccounts: ...


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
        client.multicloud.accounts.get_cloud_account_details()


Operation: PUT /dataservice/multicloud/accounts/{accountId}
-----------------------------------------------------------


Obtain all accounts for all clouds

.. code:: python

    def update_account(
        account_id: str, payload: Optional[PutAccounts] = None
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
        client.multicloud.accounts.update_account()


Operation: DELETE /dataservice/multicloud/accounts/{accountId}
--------------------------------------------------------------


Obtain all accounts for all clouds

.. code:: python

    def delete_account(account_id: str) -> None: ...


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
        client.multicloud.accounts.delete_account()


.. toctree::
    :maxdepth: 1

    edge/index
    credentials/index
    models

