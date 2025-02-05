==============================
networkdesign.global_.template
==============================


Operation: GET /dataservice/networkdesign/global/template/{templateId}
----------------------------------------------------------------------


Deprecated!!!

Get global template

.. code:: python

    def get_global_template(template_id: str) -> Any: ...


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
        client.networkdesign.global_.template.get_global_template()


Operation: PUT /dataservice/networkdesign/global/template/{templateId}
----------------------------------------------------------------------


Deprecated!!!

Edit global template

.. code:: python

    def edit_global_template(
        template_id: str, payload: Optional[Any] = None
    ) -> None: ...


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
        client.networkdesign.global_.template.edit_global_template()


