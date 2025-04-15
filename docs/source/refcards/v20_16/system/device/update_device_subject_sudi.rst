========================================
system.device.update_device_subject_sudi
========================================


Operation: PUT /dataservice/system/device/updateDeviceSubjectSUDI/{uuid}
------------------------------------------------------------------------


update subject sudi value of given device uuid

.. code:: python

    def put(uuid: str) -> None: ...


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
        client.system.device.update_device_subject_sudi.put()


