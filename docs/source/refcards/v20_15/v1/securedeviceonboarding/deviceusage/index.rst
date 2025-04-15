=====================================
v1.securedeviceonboarding.deviceusage
=====================================


Operation: GET /dataservice/v1/securedeviceonboarding/{deviceUUID}/deviceusage
------------------------------------------------------------------------------


Get device data usage using device uuid

.. code:: python

    def get(device_uuid: str) -> DeviceUsageDetails: ...


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
        client.v1.securedeviceonboarding.deviceusage.get()


.. toctree::
    :maxdepth: 1

    models

