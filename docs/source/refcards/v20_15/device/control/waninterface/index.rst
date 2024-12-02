===========================
device.control.waninterface
===========================


Operation: GET /dataservice/device/control/waninterface
-------------------------------------------------------


Get WAN interface list (Real Time)

.. code:: python

    def create_wan_interface_list_list(device_id: str) -> List[Any]: ...


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
        client.device.control.waninterface.create_wan_interface_list_list()


.. toctree::
    :maxdepth: 1

    color

