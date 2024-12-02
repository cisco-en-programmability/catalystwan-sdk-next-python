=================
v1.reports.action
=================


Operation: PUT /dataservice/v1/reports/{reportId}/action/{action}
-----------------------------------------------------------------


User operations for specific report template, which includes activate,deactivate and run immediately

.. code:: python

    def report_action(
        report_id: str, action: ActionParam
    ) -> UpdateReportTemplateResponse: ...


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
        client.v1.reports.action.report_action()


.. toctree::
    :maxdepth: 1

    models

