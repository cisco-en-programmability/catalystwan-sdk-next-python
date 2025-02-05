===============================
template.policy.assembly.vsmart
===============================


Operation: POST /dataservice/template/policy/assembly/vsmart
------------------------------------------------------------


Get policy assembly preview

.. code:: python

    def preview_3(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.assembly.vsmart.preview_3()


Operation: GET /dataservice/template/policy/assembly/vsmart/{id}
----------------------------------------------------------------


Get policy assembly preview for feature policy

.. code:: python

    def preview_by_id_3(id: str) -> Any: ...


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
        client.template.policy.assembly.vsmart.preview_by_id_3()


