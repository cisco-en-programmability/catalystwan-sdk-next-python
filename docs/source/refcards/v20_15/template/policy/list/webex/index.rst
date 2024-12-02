==========================
template.policy.list.webex
==========================


Operation: POST /dataservice/template/policy/list/webex
-------------------------------------------------------


TEMP-Create Webex policy lists

.. code:: python

    def create_webex_prefix_lists() -> List[Any]: ...


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
        client.template.policy.list.webex.create_webex_prefix_lists()


.. toctree::
    :maxdepth: 1

    update

