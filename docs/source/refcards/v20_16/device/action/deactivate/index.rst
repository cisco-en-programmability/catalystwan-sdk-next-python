========================
device.action.deactivate
========================


Operation: GET /dataservice/device/action/deactivate
----------------------------------------------------


Get deactivate partition information

.. code:: python

    def generate_deactivate_info(
        device_id: List[DeviceIp],
    ) -> GenerateDeactivateInfo: ...


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
        client.device.action.deactivate.generate_deactivate_info()


Operation: POST /dataservice/device/action/deactivate
-----------------------------------------------------


Process deactivate operation for smu image

.. code:: python

    def process_deactivate_smu(payload: Optional[Any] = None) -> Any: ...


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
        client.device.action.deactivate.process_deactivate_smu()


.. toctree::
    :maxdepth: 1

    models

