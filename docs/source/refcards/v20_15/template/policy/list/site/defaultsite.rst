=====================================
template.policy.list.site.defaultsite
=====================================


Operation: POST /dataservice/template/policy/list/site/defaultsite
------------------------------------------------------------------


Create default site list for sites missing from centralized policy

.. code:: python

    def create_default_site_list() -> Any: ...


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
        client.template.policy.list.site.defaultsite.create_default_site_list()


