==============================
device.policy.datapolicyfilter
==============================


Operation: GET /dataservice/device/policy/datapolicyfilter
----------------------------------------------------------


Get data policy filters from device

.. code:: python

    def create_polic_data_policy_filter(device_id: str) -> Any: ...


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
        client.device.policy.datapolicyfilter.create_polic_data_policy_filter()


