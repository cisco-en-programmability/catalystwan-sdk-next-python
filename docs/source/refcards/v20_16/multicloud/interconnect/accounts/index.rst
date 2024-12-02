================================
multicloud.interconnect.accounts
================================


Operation: GET /dataservice/multicloud/interconnect/accounts
------------------------------------------------------------


API to retrieve Interconnect provider accounts.

.. code:: python

    def get_interconnect_accounts(
        interconnect_type: Optional[str] = None,
    ) -> List[InterconnectAccount]: ...


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
        client.multicloud.interconnect.accounts.get_interconnect_accounts()


Operation: POST /dataservice/multicloud/interconnect/accounts
-------------------------------------------------------------


API to associate an Interconnect provider account to vManage.

.. code:: python

    def add_interconnect_account(
        payload: Optional[InterconnectAccount] = None,
    ) -> InterconnectAccount: ...


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
        client.multicloud.interconnect.accounts.add_interconnect_account()


Operation: GET /dataservice/multicloud/interconnect/accounts/{interconnect-account-id}
--------------------------------------------------------------------------------------


API to retrieve associated Interconnect provider account details by id.

.. code:: python

    def get_interconnect_account(
        interconnect_account_id: str,
    ) -> InterconnectAccount: ...


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
        client.multicloud.interconnect.accounts.get_interconnect_account()


Operation: PUT /dataservice/multicloud/interconnect/accounts/{interconnect-account-id}
--------------------------------------------------------------------------------------


API to edit associated Interconnect provider account name and description.

.. code:: python

    def update_interconnect_account(
        interconnect_account_id: str,
        payload: Optional[InterconnectAccount] = None,
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
        client.multicloud.interconnect.accounts.update_interconnect_account()


Operation: DELETE /dataservice/multicloud/interconnect/accounts/{interconnect-account-id}
-----------------------------------------------------------------------------------------


API to disassociate Interconnect provider account from vManage.

.. code:: python

    def delete_interconnect_account(
        interconnect_account_id: str,
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
        client.multicloud.interconnect.accounts.delete_interconnect_account()


.. toctree::
    :maxdepth: 1

    credentials/index
    billing_accounts/index
    cloud/index
    connectivity/index
    locations/index
    models

