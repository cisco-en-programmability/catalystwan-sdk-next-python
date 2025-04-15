==============================================
v1.securedeviceonboarding.providerscredentials
==============================================


Operation: GET /dataservice/v1/securedeviceonboarding/providerscredentials
--------------------------------------------------------------------------


Get all providers credentials

.. code:: python

    def get() -> ProviderAccountDetails: ...


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
        client.v1.securedeviceonboarding.providerscredentials.get()


.. toctree::
    :maxdepth: 1

    models

