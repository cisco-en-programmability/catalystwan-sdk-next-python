==============================
template.policy.assembly.vedge
==============================


Operation: POST /dataservice/template/policy/assembly/vedge
-----------------------------------------------------------


Get policy assembly preview

.. code:: python

    def preview_1(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.assembly.vedge.preview_1()


Operation: GET /dataservice/template/policy/assembly/vedge/{id}
---------------------------------------------------------------


Get policy assembly preview for feature policy

.. code:: python

    def preview_by_id_1(id: str) -> Any: ...


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
        client.template.policy.assembly.vedge.preview_by_id_1()


