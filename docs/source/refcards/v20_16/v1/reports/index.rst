==========
v1.reports
==========


Operation: POST /dataservice/v1/reports
---------------------------------------


create a new report template

.. code:: python

    def post(payload: ExecutiveSummaryReport) -> ReportInfo: ...


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
        client.v1.reports.post()


Operation: PUT /dataservice/v1/reports/{reportId}
-------------------------------------------------


Update the report template by report ID

.. code:: python

    def put(
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
        client.v1.reports.put()


Operation: DELETE /dataservice/v1/reports/{reportId}
----------------------------------------------------


Delete the report template and all report files associated with it

.. code:: python

    def delete(report_id: str) -> UpdateReportTemplateResponse: ...


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
        client.v1.reports.delete()


Operation: GET /dataservice/v1/reports
--------------------------------------


.. code:: python

    @overload
    def get() -> ReportSummaryResponse: ...


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
        client.v1.reports.get()


Operation: GET /dataservice/v1/reports/{reportId}
-------------------------------------------------


.. code:: python

    @overload
    def get(report_id: str) -> ReportSummaryResponse: ...


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
        client.v1.reports.get()


.. toctree::
    :maxdepth: 1

    preview/index
    action/index
    tasks/index
    models

