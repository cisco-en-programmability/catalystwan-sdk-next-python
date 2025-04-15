==========================
admin.user.active_sessions
==========================


Operation: GET /dataservice/admin/user/activeSessions
-----------------------------------------------------


Get active sessions

.. code:: python

    def get() -> Any: ...


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
        client.admin.user.active_sessions.get()


