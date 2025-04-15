=============================
template.policy.vedge.devices
=============================


Operation: GET /dataservice/template/policy/vedge/devices
---------------------------------------------------------


.. code:: python

    @overload
    def get() -> List[Any]: ...


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
        client.template.policy.vedge.devices.get()


Operation: GET /dataservice/template/policy/vedge/devices/{policyId}
--------------------------------------------------------------------


.. code:: python

    @overload
    def get(policy_id: str) -> List[Any]: ...


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
        client.template.policy.vedge.devices.get()


