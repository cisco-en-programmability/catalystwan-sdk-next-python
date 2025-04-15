======================
template.feature.clone
======================


Operation: POST /dataservice/template/feature/clone
---------------------------------------------------


Clone a feature template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def post(id: str, name: str, desc: str) -> Any: ...


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
        client.template.feature.clone.post()


