================
dashboard.enroll
================


Operation: POST /dataservice/dashboard/enroll/{profileId}
---------------------------------------------------------


Enroll a Controller with CD profiles

.. code:: python

    def enroll_cd_profiles(profile_id: str) -> None: ...


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
        client.dashboard.enroll.enroll_cd_profiles()


