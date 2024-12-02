=====================
device.action.install
=====================


Operation: GET /dataservice/device/action/install
-------------------------------------------------


Generate install info

.. code:: python

    def generate_install_info(device_id: List[DeviceIp]) -> None: ...


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
        client.device.action.install.generate_install_info()


Operation: POST /dataservice/device/action/install
--------------------------------------------------


Process an installation operation

.. code:: python

    def process_install(payload: Optional[Any] = None) -> None: ...


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
        client.device.action.install.process_install()


.. toctree::
    :maxdepth: 1

    devices/index
    models

