=======================================
system.device.smartaccount.authenticate
=======================================


Operation: POST /dataservice/system/device/smartaccount/authenticate
--------------------------------------------------------------------


Authenticate vSmart user account

.. code:: python

    def post(payload: Any) -> SmartAccountAuthenticateResponse: ...


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
        client.system.device.smartaccount.authenticate.post()


.. toctree::
    :maxdepth: 1

    models

