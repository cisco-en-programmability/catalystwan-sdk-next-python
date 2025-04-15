===========================
v1.reports.preview.download
===========================


Operation: GET /dataservice/v1/reports/preview/download
-------------------------------------------------------


Download a report preview file

.. code:: python

    def get(template_type: Optional[TemplateTypeParam] = None) -> str: ...


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
        client.v1.reports.preview.download.get()


.. toctree::
    :maxdepth: 1

    models

