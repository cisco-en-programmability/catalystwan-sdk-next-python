================
v1.reports.tasks
================


Operation: GET /dataservice/v1/reports/{reportId}/tasks
-------------------------------------------------------


Get all report task detail information by report ID

.. code:: python

    def get_all_report_tasks_by_report_id(
        report_id: str,
    ) -> ReportTaskQueryResponse: ...


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
        client.v1.reports.tasks.get_all_report_tasks_by_report_id()


Operation: DELETE /dataservice/v1/reports/{reportId}/tasks/{taskId}
-------------------------------------------------------------------


Delete the report task file by task ID

.. code:: python

    def delete_report_task_by_task_id(
        report_id: str, task_id: str
    ) -> TaskIdResponse: ...


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
        client.v1.reports.tasks.delete_report_task_by_task_id()


.. toctree::
    :maxdepth: 1

    download
    models

