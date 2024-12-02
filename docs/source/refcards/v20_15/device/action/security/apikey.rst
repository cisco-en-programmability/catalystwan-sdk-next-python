=============================
device.action.security.apikey
=============================


Operation: GET /dataservice/device/action/security/apikey/{uuid}
----------------------------------------------------------------


Get API key from device

.. code:: python

    def test_api_key(uuid: str) -> Any: ...


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
        client.device.action.security.apikey.test_api_key()


