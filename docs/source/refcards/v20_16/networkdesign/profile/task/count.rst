================================
networkdesign.profile.task.count
================================


Operation: GET /dataservice/networkdesign/profile/task/count
------------------------------------------------------------


Deprecated!!!

Get device profile configuration task count

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
        client.networkdesign.profile.task.count.get()


