=============================
template.policy.vedge.devices
=============================


Operation: GET /dataservice/template/policy/vedge/devices
---------------------------------------------------------


Get device list

.. code:: python

    def get_v_edge_policy_device_list() -> List[Any]: ...


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
        client.template.policy.vedge.devices.get_v_edge_policy_device_list()


Operation: GET /dataservice/template/policy/vedge/devices/{policyId}
--------------------------------------------------------------------


Get device list by policy

.. code:: python

    def get_device_list_by_policy(policy_id: str) -> List[Any]: ...


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
        client.template.policy.vedge.devices.get_device_list_by_policy()


