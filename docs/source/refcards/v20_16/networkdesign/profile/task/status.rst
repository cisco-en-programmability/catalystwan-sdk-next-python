=================================
networkdesign.profile.task.status
=================================


Operation: GET /dataservice/networkdesign/profile/task/status
-------------------------------------------------------------


Deprecated!!!

Get device profile configuration task status

.. code:: python

    def get_device_profile_task_status() -> Any: ...


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
        client.networkdesign.profile.task.status.get_device_profile_task_status()


Operation: GET /dataservice/networkdesign/profile/task/status/{profileId}
-------------------------------------------------------------------------


Deprecated!!!

Get device profile configuration status by profile Id

.. code:: python

    def get_device_profile_task_status_by_profile_id(
        profile_id: str,
    ) -> Any: ...


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
        client.networkdesign.profile.task.status.get_device_profile_task_status_by_profile_id()


