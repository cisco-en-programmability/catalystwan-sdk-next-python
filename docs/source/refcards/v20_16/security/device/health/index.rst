======================
security.device.health
======================


Operation: GET /dataservice/security/device/health
--------------------------------------------------


Get security device health

.. code:: python

    def get_security_device_health(
        device_ip: Optional[str] = None,
    ) -> List[SecurityDeviceHealth]: ...


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
        client.security.device.health.get_security_device_health()


.. toctree::
    :maxdepth: 1

    models

