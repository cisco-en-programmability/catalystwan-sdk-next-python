=================================
system.device.management.systemip
=================================


Operation: GET /dataservice/system/device/management/systemip
-------------------------------------------------------------


Get management system IP mapping

.. code:: python

    def get_management_system_ip_info_1() -> Any: ...


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
        client.system.device.management.systemip.get_management_system_ip_info_1()


