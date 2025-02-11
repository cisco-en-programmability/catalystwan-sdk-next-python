=========================
device.license.evaluation
=========================


Operation: GET /dataservice/device/license/evaluation
-----------------------------------------------------


Get license evaluation info from device

.. code:: python

    def get_license_eval_info(device_id: str) -> Any: ...


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
        client.device.license.evaluation.get_license_eval_info()


