==========================
security.policy.devicelist
==========================


Operation: GET /dataservice/security/policy/devicelist
------------------------------------------------------


Get security policy device list

.. code:: python

    def get() -> List[SecurityPolicyDeviceList]: ...


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
        client.security.policy.devicelist.get()


.. toctree::
    :maxdepth: 1

    models

