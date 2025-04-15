===============================
template.policy.assembly.vsmart
===============================


Operation: POST /dataservice/template/policy/assembly/vsmart
------------------------------------------------------------


Get policy assembly preview

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.template.policy.assembly.vsmart.post()


Operation: GET /dataservice/template/policy/assembly/vsmart/{id}
----------------------------------------------------------------


Get policy assembly preview for feature policy

.. code:: python

    def get(id: str) -> Any: ...


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
        client.template.policy.assembly.vsmart.get()


