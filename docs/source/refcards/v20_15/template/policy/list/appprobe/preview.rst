=====================================
template.policy.list.appprobe.preview
=====================================


Operation: POST /dataservice/template/policy/list/appprobe/preview
------------------------------------------------------------------


Preview a policy list based on the policy list type

.. code:: python

    def preview_policy_list_4(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.appprobe.preview.preview_policy_list_4()


Operation: GET /dataservice/template/policy/list/appprobe/preview/{id}
----------------------------------------------------------------------


Preview a specific policy list entry based on id provided

.. code:: python

    def preview_policy_list_by_id_4(id: str) -> Any: ...


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
        client.template.policy.list.appprobe.preview.preview_policy_list_by_id_4()


