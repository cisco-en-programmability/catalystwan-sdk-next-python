======
Models
======


.. code:: python

    from typing import Any, List, Dict, Literal, Optional, Union

    TaskStatus = Literal["failure", "in_progress", "success"]


    class ReportTaskProcessStepInfo:
        """
        The detail status for each step of report generating task
        """

        # Report file is generated or not
        file_generated: bool
        # Report data query success or not
        report_data_query: bool
        # Email sent or not, if sending report via email is enabled
        email_sent: Optional[bool]
        # Report file is all replicated or not when vManage is a cluster deployment
        file_replicated: Optional[bool]


    class ReportTaskUiInfo:
        """
        Report Task list for specific report ID
        """

        # Report Template UUID
        report_id: str
        # Report name for task
        report_name: str
        # Report schedule information
        schedule: str
        # Report task start timestamp
        start_time: int
        # Task UUID
        task_id: str
        # Report Task status
        task_status: TaskStatus
        # The detail status for each step of report generating task
        task_step_detail: ReportTaskProcessStepInfo
        # Report time frame (7 Days or 30 Days)
        time_frame: str
        # Email address to receive the report files
        email_recipient: Optional[List[str]]
        # Report task end timestamp
        end_time: Optional[int]
        # Report file type
        file_type: Optional[str]
        # In Cluster deployment, the follower vManage IP address which needs to replicate the report file from source vManage which generated the report file.
        follower_vmanages: Optional[List[str]]
        # IP address of the source vManage which is scheduled to generate report file. Default value is "localhost" for single node vManage deployment.
        on_vmanage: Optional[str]
        # Report file download URL
        report_download_url: Optional[str]


    class ReportTaskQueryResponse:
        """
        Report task query response
        """

        # Report Task list for specific report ID
        task_list: List[ReportTaskUiInfo]
        header: Optional[Dict[str, Any]]


    class TaskIdResponse:
        # Task ID
        task_id: str


