=============================================
v1.securedeviceonboarding.providercredentials
=============================================


Operation: POST /dataservice/v1/securedeviceonboarding/providercredentials
--------------------------------------------------------------------------


Create service provider credentials

.. code:: python

    def post(payload: None) -> None: ...


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
        client.v1.securedeviceonboarding.providercredentials.post()


Operation: GET /dataservice/v1/securedeviceonboarding/{accountId}/providercredentials
-------------------------------------------------------------------------------------


Get provider credentials by account id

.. code:: python

    def get(account_id: str) -> ProviderAccountDetailsList: ...


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
        client.v1.securedeviceonboarding.providercredentials.get()


Operation: PUT /dataservice/v1/securedeviceonboarding/{accountId}/providercredentials
-------------------------------------------------------------------------------------


Edit service provider credentials

.. code:: python

    def put(account_id: str, payload: ProviderAccountDetails) -> None: ...


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
        client.v1.securedeviceonboarding.providercredentials.put()


.. toctree::
    :maxdepth: 1

    models

