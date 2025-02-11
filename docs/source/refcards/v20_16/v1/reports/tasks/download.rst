=========================
v1.reports.tasks.download
=========================


Operation: GET /dataservice/v1/reports/{reportId}/tasks/{taskId}/download
-------------------------------------------------------------------------


Download a report file

.. code:: python

    def download_report_data_file(
        report_id: str, task_id: str
    ) -> str: ...


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
        client.v1.reports.tasks.download.download_report_data_file()


