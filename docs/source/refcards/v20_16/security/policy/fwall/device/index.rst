============================
security.policy.fwall.device
============================


Operation: POST /dataservice/security/policy/fwall/device
---------------------------------------------------------


Get firewall devices list

.. code:: python

    def post(payload: Any) -> List[DeviceLists]: ...


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
        client.security.policy.fwall.device.post()


.. toctree::
    :maxdepth: 1

    models

