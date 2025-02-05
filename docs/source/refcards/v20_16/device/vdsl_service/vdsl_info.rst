=============================
device.vdsl_service.vdsl_info
=============================


Operation: GET /dataservice/device/vdslService/vdslInfo
-------------------------------------------------------


Get VDSL info from device

.. code:: python

    def get_vdsl_info(device_id: str) -> Any: ...


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
        client.device.vdsl_service.vdsl_info.get_vdsl_info()


