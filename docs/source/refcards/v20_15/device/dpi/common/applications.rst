==============================
device.dpi.common.applications
==============================


Operation: GET /dataservice/device/dpi/common/applications
----------------------------------------------------------


Get DPI common application list from device

.. code:: python

    def get_common_application_list() -> List[Any]: ...


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
        client.device.dpi.common.applications.get_common_application_list()


