=================================================
template.policy.list.preferredcolorgroup.filtered
=================================================


Operation: GET /dataservice/template/policy/list/preferredcolorgroup/filtered
-----------------------------------------------------------------------------


Get policy lists with specific info tag

.. code:: python

    def get_policy_lists_with_info_tag_28(
        info_tag: Optional[str] = None,
    ) -> List[Any]: ...


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
        client.template.policy.list.preferredcolorgroup.filtered.get_policy_lists_with_info_tag_28()


