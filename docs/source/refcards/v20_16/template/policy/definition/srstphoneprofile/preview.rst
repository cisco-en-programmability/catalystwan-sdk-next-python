===================================================
template.policy.definition.srstphoneprofile.preview
===================================================


Operation: POST /dataservice/template/policy/definition/srstphoneprofile/preview
--------------------------------------------------------------------------------


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
        client.template.policy.definition.srstphoneprofile.preview.post()


Operation: GET /dataservice/template/policy/definition/srstphoneprofile/preview/{id}
------------------------------------------------------------------------------------


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
        client.template.policy.definition.srstphoneprofile.preview.get()


