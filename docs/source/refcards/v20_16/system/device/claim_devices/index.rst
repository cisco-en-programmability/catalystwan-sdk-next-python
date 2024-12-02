===========================
system.device.claim_devices
===========================


Operation: POST /dataservice/system/device/claimDevices
-------------------------------------------------------


Claim the selected unclaimed devices

.. code:: python

    def claim_devices(
        payload: Optional[ClaimDevicesRequest] = None,
    ) -> ClaimDevicesResponse: ...


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
        client.system.device.claim_devices.claim_devices()


.. toctree::
    :maxdepth: 1

    models

