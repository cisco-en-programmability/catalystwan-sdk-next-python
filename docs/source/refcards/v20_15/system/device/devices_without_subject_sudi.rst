==========================================
system.device.devices_without_subject_sudi
==========================================


Operation: GET /dataservice/system/device/devicesWithoutSubjectSudi
-------------------------------------------------------------------


retrieve devices without subject sudi

.. code:: python

    def devices_without_subject_sudi() -> List[Any]: ...


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
        client.system.device.devices_without_subject_sudi.devices_without_subject_sudi()


