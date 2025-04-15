===========================
system.device.generate_payg
===========================


Operation: POST /dataservice/system/device/generate-payg
--------------------------------------------------------


Authenticate vSmart user account

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.system.device.generate_payg.post()


