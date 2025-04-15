=================================
networkdesign.profile.task.status
=================================


Operation: GET /dataservice/networkdesign/profile/task/status
-------------------------------------------------------------


Deprecated!!!

.. code:: python

    @overload
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
        client.networkdesign.profile.task.status.get()


Operation: GET /dataservice/networkdesign/profile/task/status/{profileId}
-------------------------------------------------------------------------


Deprecated!!!

.. code:: python

    @overload
    def get(profile_id: str) -> Any: ...


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
        client.networkdesign.profile.task.status.get()


