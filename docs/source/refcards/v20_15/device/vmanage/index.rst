==============
device.vmanage
==============


Operation: GET /dataservice/device/vmanage
------------------------------------------


Get vManage system IP

.. code:: python

    def get_v_manage_system_ip() -> DeviceVmanageResponse: ...


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
        client.device.vmanage.get_v_manage_system_ip()


.. toctree::
    :maxdepth: 1

    models

