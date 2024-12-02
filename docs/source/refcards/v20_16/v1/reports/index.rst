==========
v1.reports
==========


Operation: GET /dataservice/v1/reports
--------------------------------------


Get all reports information

.. code:: python

    def get_all_report_templates() -> ReportSummaryResponse: ...


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
        client.v1.reports.get_all_report_templates()


Operation: POST /dataservice/v1/reports
---------------------------------------


create a new report template

.. code:: python

    def create_report_template(
        payload: ExecutiveSummaryReport,
    ) -> ReportInfo: ...


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
        client.v1.reports.create_report_template()


Operation: GET /dataservice/v1/reports/{reportId}
-------------------------------------------------


Get the report template information by report ID

.. code:: python

    def get_report_template_by_id(
        report_id: str,
    ) -> ReportSummaryResponse: ...


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
        client.v1.reports.get_report_template_by_id()


Operation: PUT /dataservice/v1/reports/{reportId}
-------------------------------------------------


Update the report template by report ID

.. code:: python

    def update_report_template(
        report_id: str, payload: ExecutiveSummaryReport
    ) -> ReportInfo: ...


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
        client.v1.reports.update_report_template()


Operation: DELETE /dataservice/v1/reports/{reportId}
----------------------------------------------------


Delete the report template and all report files associated with it

.. code:: python

    def delete_report_template(
        report_id: str,
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
        client.v1.reports.delete_report_template()


.. toctree::
    :maxdepth: 1

    preview/index
    action/index
    tasks/index
    models

