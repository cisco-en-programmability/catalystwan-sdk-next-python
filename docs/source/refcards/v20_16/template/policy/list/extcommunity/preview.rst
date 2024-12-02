=========================================
template.policy.list.extcommunity.preview
=========================================


Operation: POST /dataservice/template/policy/list/extcommunity/preview
----------------------------------------------------------------------


Preview a policy list based on the policy list type

.. code:: python

    def preview_policy_list_12(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.extcommunity.preview.preview_policy_list_12()


Operation: GET /dataservice/template/policy/list/extcommunity/preview/{id}
--------------------------------------------------------------------------


Preview a specific policy list entry based on id provided

.. code:: python

    def preview_policy_list_by_id_12(id: str) -> Any: ...


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
        client.template.policy.list.extcommunity.preview.preview_policy_list_by_id_12()


