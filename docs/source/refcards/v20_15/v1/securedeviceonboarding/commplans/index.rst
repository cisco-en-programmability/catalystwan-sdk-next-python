===================================
v1.securedeviceonboarding.commplans
===================================


Operation: GET /dataservice/v1/securedeviceonboarding/{accountId}/commplans
---------------------------------------------------------------------------


Get communication plans by account Id

.. code:: python

    def get(account_id: str) -> CommunicationPlansResponse: ...


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
        client.v1.securedeviceonboarding.commplans.get()


.. toctree::
    :maxdepth: 1

    models

