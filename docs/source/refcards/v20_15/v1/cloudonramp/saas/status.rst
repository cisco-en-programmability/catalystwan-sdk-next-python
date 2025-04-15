==========================
v1.cloudonramp.saas.status
==========================


Operation: GET /dataservice/v1/cloudonramp/saas/status
------------------------------------------------------


Get Cloud On Ramp App details per device

.. code:: python

    def get(device_ip: str) -> None: ...


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
        client.v1.cloudonramp.saas.status.get()


