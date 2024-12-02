=============================
device.control.validvmanageid
=============================


Operation: GET /dataservice/device/control/validvmanageid
---------------------------------------------------------


Get valid vManage from device (Real Time)

.. code:: python

    def get_valid_v_manage_id_real_time(device_id: str) -> Any: ...


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
        client.device.control.validvmanageid.get_valid_v_manage_id_real_time()


