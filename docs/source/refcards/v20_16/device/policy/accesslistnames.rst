=============================
device.policy.accesslistnames
=============================


Operation: GET /dataservice/device/policy/accesslistnames
---------------------------------------------------------


Get access list names from device

.. code:: python

    def create_policy_access_list_names(device_id: str) -> Any: ...


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
        client.device.policy.accesslistnames.create_policy_access_list_names()


