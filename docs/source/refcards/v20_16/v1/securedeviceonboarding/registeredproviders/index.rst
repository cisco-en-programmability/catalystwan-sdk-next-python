=============================================
v1.securedeviceonboarding.registeredproviders
=============================================


Operation: GET /dataservice/v1/securedeviceonboarding/registeredproviders
-------------------------------------------------------------------------


Get Registered Providers Info

.. code:: python

    def get_providers_info() -> ProviderInfo: ...


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
        client.v1.securedeviceonboarding.registeredproviders.get_providers_info()


.. toctree::
    :maxdepth: 1

    models

