=============================
dashboard.registration.status
=============================


Operation: GET /dataservice/dashboard/registration/status
---------------------------------------------------------


Check if vManage is registred with BiFrost

.. code:: python

    def get_registration_status() -> None: ...


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
        client.dashboard.registration.status.get_registration_status()


