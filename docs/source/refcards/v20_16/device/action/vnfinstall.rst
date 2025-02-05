========================
device.action.vnfinstall
========================


Operation: POST /dataservice/device/action/vnfinstall
-----------------------------------------------------


Deprecated!!!

Process an installation operation

.. code:: python

    def process_vnf_install(payload: Optional[Any] = None) -> Any: ...


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
        client.device.action.vnfinstall.process_vnf_install()


