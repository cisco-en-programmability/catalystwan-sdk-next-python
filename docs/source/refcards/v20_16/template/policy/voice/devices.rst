=============================
template.policy.voice.devices
=============================


Operation: GET /dataservice/template/policy/voice/devices
---------------------------------------------------------


Get all device list

.. code:: python

    def get_voice_policy_device_list() -> List[Any]: ...


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
        client.template.policy.voice.devices.get_voice_policy_device_list()


Operation: GET /dataservice/template/policy/voice/devices/{policyId}
--------------------------------------------------------------------


Get device list by policy Id

.. code:: python

    def get_device_list_by_policy_id(policy_id: str) -> List[Any]: ...


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
        client.template.policy.voice.devices.get_device_list_by_policy_id()


