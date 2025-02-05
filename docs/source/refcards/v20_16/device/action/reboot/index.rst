====================
device.action.reboot
====================


Operation: GET /dataservice/device/action/reboot
------------------------------------------------


Get device reboot information

.. code:: python

    def generate_reboot_info(device_id: List[DeviceIp]) -> List[Any]: ...


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
        client.device.action.reboot.generate_reboot_info()


Operation: POST /dataservice/device/action/reboot
-------------------------------------------------


Process a reboot operation

.. code:: python

    def process_reboot(payload: Optional[Any] = None) -> TaskId: ...


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
        client.device.action.reboot.process_reboot()


.. toctree::
    :maxdepth: 1

    devices/index
    models

