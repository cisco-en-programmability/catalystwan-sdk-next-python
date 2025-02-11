============================
device.hardwarehealth.detail
============================


Operation: GET /dataservice/device/hardwarehealth/detail
--------------------------------------------------------


Get hardware health details for device

.. code:: python

    def get_hardware_health_details(
        device_id: Optional[str] = None, state: Optional[str] = None
    ) -> List[DeviceHardwareHealthDetail]: ...


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
        client.device.hardwarehealth.detail.get_hardware_health_details()


.. toctree::
    :maxdepth: 1

    models

