====================
device.policy.vsmart
====================


Operation: GET /dataservice/device/policy/vsmart
------------------------------------------------


show Sdwan Policy From Vsmart

.. code:: python

    def show_sdwan_policy_from_vsmart(device_id: str) -> Any: ...


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
        client.device.policy.vsmart.show_sdwan_policy_from_vsmart()


