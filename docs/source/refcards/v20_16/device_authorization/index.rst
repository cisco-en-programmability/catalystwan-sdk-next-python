====================
device_authorization
====================


Operation: POST /dataservice/device_authorization/{regionBaseUri}/{clientId}
----------------------------------------------------------------------------


User authorization for Cisco vManage SecureX integration

.. code:: python

    def post(client_id: str, region_base_uri: str) -> Codes: ...


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
        client.device_authorization.post()


.. toctree::
    :maxdepth: 1

    models

