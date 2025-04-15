===========================
v1.cloudonramp.saas.devices
===========================


Operation: GET /dataservice/v1/cloudonramp/saas/devices
-------------------------------------------------------


Get site, apps and device role information for cloud on ramp devices

.. code:: python

    def get() -> None: ...


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
        client.v1.cloudonramp.saas.devices.get()


