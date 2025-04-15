=======================
template.cor.scale.down
=======================


Operation: POST /dataservice/template/cor/scale/down
----------------------------------------------------


Deprecated!!!

Scale down cloud on ramp

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.template.cor.scale.down.post()


