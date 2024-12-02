===========================
v1.smart_licensing.template
===========================


Operation: POST /dataservice/v1/smart-licensing/template
--------------------------------------------------------


Create and assign license template.

.. code:: python

    def save_template(
        payload: Optional[SaveTemplateRequest] = None,
    ) -> Any: ...


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
        client.v1.smart_licensing.template.save_template()


Operation: DELETE /dataservice/v1/smart-licensing/template/{templateId}
-----------------------------------------------------------------------


Delete a license template

.. code:: python

    def delete_template(template_id: str) -> None: ...


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
        client.v1.smart_licensing.template.delete_template()


.. toctree::
    :maxdepth: 1

    models

