=================================
template.policy.list.webex.update
=================================


Operation: POST /dataservice/template/policy/list/webex/update
--------------------------------------------------------------


TEMP-Update Webex policy lists from Webex config

.. code:: python

    def post() -> List[Any]: ...


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
        client.template.policy.list.webex.update.post()


