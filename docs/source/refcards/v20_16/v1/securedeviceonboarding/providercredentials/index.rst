=============================================
v1.securedeviceonboarding.providercredentials
=============================================


Operation: POST /dataservice/v1/securedeviceonboarding/providercredentials
--------------------------------------------------------------------------


Create service provider credentials

.. code:: python

    def create_provider_credentials(
        payload: Optional[None] = None,
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
        client.v1.securedeviceonboarding.providercredentials.create_provider_credentials()


Operation: GET /dataservice/v1/securedeviceonboarding/{accountId}/providercredentials
-------------------------------------------------------------------------------------


Get provider credentials by account id

.. code:: python

    def get_provider_credentials_by_account_id(
        account_id: str,
    ) -> ProviderAccountDetailsList: ...


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
        client.v1.securedeviceonboarding.providercredentials.get_provider_credentials_by_account_id()


Operation: PUT /dataservice/v1/securedeviceonboarding/{accountId}/providercredentials
-------------------------------------------------------------------------------------


Edit service provider credentials

.. code:: python

    def edit_provider_credentials(
        account_id: str, payload: Optional[ProviderAccountDetails] = None
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
        client.v1.securedeviceonboarding.providercredentials.edit_provider_credentials()


.. toctree::
    :maxdepth: 1

    models

