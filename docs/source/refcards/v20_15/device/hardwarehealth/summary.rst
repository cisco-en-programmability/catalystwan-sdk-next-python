=============================
device.hardwarehealth.summary
=============================


Operation: GET /dataservice/device/hardwarehealth/summary
---------------------------------------------------------


Get hardware health summary for device

.. code:: python

    def get(
        vpn_id: List[str], is_cached: Optional[bool] = False
    ) -> List[Any]: ...


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
        client.device.hardwarehealth.summary.get()


