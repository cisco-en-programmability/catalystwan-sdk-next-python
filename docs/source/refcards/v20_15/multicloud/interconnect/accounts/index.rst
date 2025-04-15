================================
multicloud.interconnect.accounts
================================


Operation: POST /dataservice/multicloud/interconnect/accounts
-------------------------------------------------------------


API to associate an Interconnect provider account to vManage.

.. code:: python

    def post(payload: InterconnectAccount) -> InterconnectAccount: ...


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
        client.multicloud.interconnect.accounts.post()


Operation: PUT /dataservice/multicloud/interconnect/accounts/{interconnect-account-id}
--------------------------------------------------------------------------------------


API to edit associated Interconnect provider account name and description.

.. code:: python

    def put(
        interconnect_account_id: str, payload: InterconnectAccount
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
        client.multicloud.interconnect.accounts.put()


Operation: DELETE /dataservice/multicloud/interconnect/accounts/{interconnect-account-id}
-----------------------------------------------------------------------------------------


API to disassociate Interconnect provider account from vManage.

.. code:: python

    def delete(interconnect_account_id: str) -> None: ...


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
        client.multicloud.interconnect.accounts.delete()


Operation: GET /dataservice/multicloud/interconnect/accounts
------------------------------------------------------------


.. code:: python

    @overload
    def get(
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
        client.multicloud.interconnect.accounts.get()


Operation: GET /dataservice/multicloud/interconnect/accounts/{interconnect-account-id}
--------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(interconnect_account_id: str) -> InterconnectAccount: ...


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
        client.multicloud.interconnect.accounts.get()


.. toctree::
    :maxdepth: 1

    credentials/index
    billing_accounts/index
    cloud/index
    connectivity/index
    locations/index
    models

