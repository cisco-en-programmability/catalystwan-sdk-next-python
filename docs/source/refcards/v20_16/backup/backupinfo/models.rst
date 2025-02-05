======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class LocalDestination:
        # Storage type. This could be [LOCAL/S3/SFTP/AZURE]
        backup_dest: Optional[str]
        # Location where the database backup file on a storage type.
        backup_dir: Optional[str]
        # Size of the database backup allowed to the stored at a backup destination
        backup_storage_in_gb: Optional[int]
        # Time to live for a database backup copy in the backup destination in days
        backup_ttl_in_days: Optional[int]
        # Number of replicas of the database backup file
        num_of_replica: Optional[int]
        # vManage software version against which the database backup was taken
        vm_version: Optional[str]


    class LocalBackupInfo:
        # Current stage of database backup workflow. This could be [SCHEDULED/IN_PROGRESS/CONFIG_DB_BACKUP_SUCCESS/CONFIG_DB_BACKUP_FAILED/STATS_DB_EXPORT_SUCCESS/STATS_DB_EXPORT_FAILED/CONFIG_DB_CONSISTENCY_CHECK_FAILED/LEADER_SUCCESS/ALL_SUCCESS/FAILURE/DELETED]
        backup_state: Optional[str]
        # Type of backup. This could be [SCHEDULED/ON_DEMAND]
        backup_type: Optional[str]
        # Epoch timestamp
        create_time: Optional[int]
        destination: Optional[LocalDestination]
        # Destination to download database backup from
        download_url: Optional[str]
        # List of vManage servers IP address who are running in follower mode
        follower_ip_address_list: Optional[List[str]]
        # A unique UUID per database back up request
        local_backup_info_id: Optional[str]
        # A unique UUID for scheduled database backup task
        schedule_id: Optional[str]
        # IP address of the source vmanage server for database backup
        src_ip_address: Optional[str]
        # Unique task Id for a given database backup task
        task_id: Optional[str]
        # Task name in human readable format
        task_name: Optional[str]


