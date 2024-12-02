==================================
device.orchestrator.validvmanageid
==================================


Operation: GET /dataservice/device/orchestrator/validvmanageid
--------------------------------------------------------------


Get valid vManage Id from device

.. code:: python

    def get_valid_v_manage_id(device_id: str) -> Any: ...


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
        client.device.orchestrator.validvmanageid.get_valid_v_manage_id()


