=====================
template.cor.scale.up
=====================


Operation: POST /dataservice/template/cor/scale/up
--------------------------------------------------


Deprecated!!!

Scale up cloud on ramp

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
        client.template.cor.scale.up.post()


