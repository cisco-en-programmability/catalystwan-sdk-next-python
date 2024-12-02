================================
device.orchestrator.validvsmarts
================================


Operation: GET /dataservice/device/orchestrator/validvsmarts
------------------------------------------------------------


Get valid vSmart list from device

.. code:: python

    def create_valid_v_smarts_list(device_id: str) -> Any: ...


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
        client.device.orchestrator.validvsmarts.create_valid_v_smarts_list()


