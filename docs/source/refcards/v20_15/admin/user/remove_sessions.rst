==========================
admin.user.remove_sessions
==========================


Operation: DELETE /dataservice/admin/user/removeSessions
--------------------------------------------------------


Remove sessions

.. code:: python

    def remove_sessions_1(payload: Optional[List[Any]] = None) -> Any: ...


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
        client.admin.user.remove_sessions.remove_sessions_1()


