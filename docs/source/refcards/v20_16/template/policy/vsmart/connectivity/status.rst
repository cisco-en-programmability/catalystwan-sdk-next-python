==========================================
template.policy.vsmart.connectivity.status
==========================================


Operation: GET /dataservice/template/policy/vsmart/connectivity/status
----------------------------------------------------------------------


Check VSmart Connectivity Status

.. code:: python

    def get() -> Any: ...


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
        client.template.policy.vsmart.connectivity.status.get()


