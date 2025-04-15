==============================
device.action.security.devices
==============================


Operation: GET /dataservice/device/action/security/devices/{policyType}
-----------------------------------------------------------------------


Get list of devices by security policy type

.. code:: python

    def get(
        policy_type: PolicyTypeParam, group_id: GroupId
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
        client.device.action.security.devices.get()


.. toctree::
    :maxdepth: 1

    models

