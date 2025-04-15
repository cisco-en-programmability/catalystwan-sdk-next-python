===================================
template.policy.list.region.preview
===================================


Operation: POST /dataservice/template/policy/list/region/preview
----------------------------------------------------------------


Preview a policy list based on the policy list type

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
        client.template.policy.list.region.preview.post()


Operation: GET /dataservice/template/policy/list/region/preview/{id}
--------------------------------------------------------------------


Preview a specific policy list entry based on id provided

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
        client.template.policy.list.region.preview.get()


