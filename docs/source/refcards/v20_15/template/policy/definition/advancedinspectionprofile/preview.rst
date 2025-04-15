============================================================
template.policy.definition.advancedinspectionprofile.preview
============================================================


Operation: POST /dataservice/template/policy/definition/advancedinspectionprofile/preview
-----------------------------------------------------------------------------------------


Preview policy definition

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
        client.template.policy.definition.advancedinspectionprofile.preview.post()


Operation: GET /dataservice/template/policy/definition/advancedinspectionprofile/preview/{id}
---------------------------------------------------------------------------------------------


Preview policy definition

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
        client.template.policy.definition.advancedinspectionprofile.preview.get()


