==============================================
v1.securedeviceonboarding.provider_credentials
==============================================


Operation: DELETE /dataservice/v1/securedeviceonboarding/{accountId}/providerCredentials
----------------------------------------------------------------------------------------


Delete provider credentials

.. code:: python

    def delete_provider_credentials(account_id: str) -> None: ...


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
        client.v1.securedeviceonboarding.provider_credentials.delete_provider_credentials()


