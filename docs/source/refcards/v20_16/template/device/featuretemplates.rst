================================
template.device.featuretemplates
================================


Operation: GET /dataservice/template/device/{templateId}/featuretemplates
-------------------------------------------------------------------------


get Associated Feature Templates Details

.. code:: python

    def get_associated_feature_templates_details(
        template_id: str,
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
        client.template.device.featuretemplates.get_associated_feature_templates_details()


