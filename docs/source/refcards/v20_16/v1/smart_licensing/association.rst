==============================
v1.smart_licensing.association
==============================


Operation: GET /dataservice/v1/smart-licensing/association
----------------------------------------------------------


Get the devices associated with a template

.. code:: python

    def get(template_id: Optional[str] = None) -> Any: ...


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
        client.v1.smart_licensing.association.get()


