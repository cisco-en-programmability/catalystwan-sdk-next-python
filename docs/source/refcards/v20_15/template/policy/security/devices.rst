================================
template.policy.security.devices
================================


Operation: GET /dataservice/template/policy/security/devices
------------------------------------------------------------


Get device list

.. code:: python

    def get_security_policy_device_list_1() -> List[Any]: ...


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
        client.template.policy.security.devices.get_security_policy_device_list_1()


Operation: GET /dataservice/template/policy/security/devices/{policyId}
-----------------------------------------------------------------------


Get device list by Id

.. code:: python

    def get_device_list_by_id(policy_id: str) -> List[Any]: ...


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
        client.template.policy.security.devices.get_device_list_by_id()


