=================================
template.policy.assembly.security
=================================


Operation: POST /dataservice/template/policy/assembly/security
--------------------------------------------------------------


Get policy assembly preview

.. code:: python

    def preview(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.assembly.security.preview()


Operation: GET /dataservice/template/policy/assembly/security/{id}
------------------------------------------------------------------


Get policy assembly preview for feature policy

.. code:: python

    def preview_by_id(id: str) -> Any: ...


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
        client.template.policy.assembly.security.preview_by_id()


