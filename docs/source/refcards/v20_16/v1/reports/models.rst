======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    ReportStatus = Literal[
        "completed", "failed", "in_progress", "not_scheduled", "scheduled"
    ]

    ActiveStatus = Literal["active", "cancelled"]

    FileType = Literal["csv", "pdf"]

    ScheduleType = Literal[
        "on_demand",
        "reoccur_daily",
        "reoccur_monthly",
        "reoccur_onetime",
        "reoccur_weekly",
    ]

    TemplateType = Literal[
        "app_usage",
        "executive_summary",
        "firewall_enforcement",
        "internet_browsing",
        "ips_events_collected",
        "link_availability",
        "link_sla",
        "link_utilization",
        "malware_files_collected",
        "site_availability",
    ]

    TimeRange = Literal["one_day", "one_month", "one_week"]


    class ReportSummaryInfo:
        """
        Report summary information
        """

        business_hours: str
        file_type: str
        # If the report template has running task records or not
        has_task: bool
        # Report next running timestamp
        next_run_time: int
        # vManage which scheduled report generating tasks
        on_vmanage: str
        # The report UUID for report template
        report_id: str
        # The report template name
        report_name: str
        # Report schedule status(not_scheduled/scheduled/in_progress/completed/failed))
        report_status: ReportStatus
        # Report schedule information
        schedule: str
        # The number of scheduled tasks for report template
        task_num: int
        template_type: str
        # Report time frame(7 Days/30 Days)
        time_frame: str
        # Email address list to receive the report files
        email_recipient: Optional[List[str]]


    class ReportSummaryResponse:
        """
        Query all reports summary information response
        """

        # Report List
        reports: List[ReportSummaryInfo]
        header: Optional[Dict[str, Any]]


    class ReportBusinessHours:
        """
        Report business hours for data generating
        """

        end_time: str
        start_time: str


    class ScheduleConfig1:
        """
        On-demand schedule
        """

        # Schedule type
        schedule_type: ScheduleType


    class ScheduleConfig2:
        # Schedule type
        schedule_type: ScheduleType
        # startTime string format is yyyy-MM-dd HH:mm:ss,UTC timezone
        start_time: str


    class ScheduleConfig3:
        # Schedule type
        schedule_type: ScheduleType
        # startTime string format is HH:mm:ss
        start_time: str


    class ScheduleConfig4:
        # The day number of a week, mapping is as 1 - Sun, 2 - Mon, 3 - Tus, 4 - Wed, 5 - Thu, 6 - Fri, 7 - Sat
        day_of_week: int
        # Schedule type
        schedule_type: ScheduleType
        # startTime string format is HH:mm:ss
        start_time: str


    class ScheduleConfig5:
        # Schedule type
        schedule_type: ScheduleType
        # startTime string format is (yyyy-MM-dd HH:mm:ss), time zone is UTC
        start_time: str


    class ExecutiveSummaryReport:
        """
        Executive summary report template
        """

        # Email address list to receive the report files
        email_recipient: List[str]
        # Report Name
        report_name: str
        # schedule config
        schedule_config: Union[
            ScheduleConfig1,
            ScheduleConfig2,
            ScheduleConfig3,
            ScheduleConfig4,
            ScheduleConfig5,
        ]
        # Time range for report(one_week/one_month)
        time_range: TimeRange
        # Report business hours for data generating
        business_hours: Optional[ReportBusinessHours]
        file_type: Optional[FileType]
        # Filtering by Site ID list is optional, if no site Id is included, all site ID will be used for report generating.
        site_ids: Optional[List[int]]
        template_type: Optional[TemplateType]


    class ReportInfo:
        """
        Report Template detail info
        """

        # Report active status(active,cancelled)
        active_status: ActiveStatus
        # user name for who created the report template.
        created_by: str
        # If the report template has running task records or not
        has_task: bool
        # Report template last update timestamp
        last_update_time: int
        # Report next running timestamp
        next_run_time: int
        # vManage which scheduled report generating tasks
        on_vmanage: str
        # Executive summary report template
        report_config: ExecutiveSummaryReport
        # The report UUID for report template
        report_id: str
        # Report schedule status(not_scheduled/scheduled/in_progress/completed/failed))
        report_status: ReportStatus
        debug_info: Optional[str]
        file_type: Optional[FileType]
        need_run_immediately: Optional[bool]
        task_num: Optional[int]
        template_type: Optional[TemplateType]


    class UpdateReportTemplateResponse:
        # Report ID
        report_id: str


