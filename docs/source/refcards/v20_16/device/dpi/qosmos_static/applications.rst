=====================================
device.dpi.qosmos_static.applications
=====================================


Operation: GET /dataservice/device/dpi/qosmos-static/applications
-----------------------------------------------------------------


Get DPI QoSMos static application list

.. code:: python

    def get_qosmos_static_application_list() -> List[Any]: ...


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
        client.device.dpi.qosmos_static.applications.get_qosmos_static_application_list()


