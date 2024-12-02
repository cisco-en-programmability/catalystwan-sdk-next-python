====================================
v1.cloudonramp.saas.legacydevicelist
====================================


Operation: GET /dataservice/v1/cloudonramp/saas/legacydevicelist
----------------------------------------------------------------


Get Legacy Devices List

.. code:: python

    def get_legacy_device_list() -> None: ...


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
        client.v1.cloudonramp.saas.legacydevicelist.get_legacy_device_list()


