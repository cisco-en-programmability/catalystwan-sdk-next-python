==============================
device.dpi.qosmos.applications
==============================


Operation: GET /dataservice/device/dpi/qosmos/applications
----------------------------------------------------------


Deprecated!!!

Get DPI QoSMos application list from device

.. code:: python

    def get_qosmos_application_list() -> List[Any]: ...


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
        client.device.dpi.qosmos.applications.get_qosmos_application_list()


