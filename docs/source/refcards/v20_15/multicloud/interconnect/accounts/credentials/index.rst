============================================
multicloud.interconnect.accounts.credentials
============================================


Operation: PUT /dataservice/multicloud/interconnect/accounts/{interconnect-account-id}/credentials
--------------------------------------------------------------------------------------------------


API to edit associated Interconnect provider account credentials.

.. code:: python

    def update_interconnect_account_credentials(
        interconnect_account_id: str,
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
        client.multicloud.interconnect.accounts.credentials.update_interconnect_account_credentials()


.. toctree::
    :maxdepth: 1

    models

