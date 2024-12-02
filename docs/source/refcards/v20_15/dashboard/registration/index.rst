======================
dashboard.registration
======================


Operation: POST /dataservice/dashboard/registration
---------------------------------------------------


Register Controller to BiFrost Dashboard (by Controller)

.. code:: python

    def registration(payload: Optional[Any] = None) -> None: ...


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
        client.dashboard.registration.registration()


Operation: DELETE /dataservice/dashboard/registration
-----------------------------------------------------


De-registration Controller (by Controller)

.. code:: python

    def deregistration(
        deregister_by_force: Optional[bool] = False,
    ) -> None: ...


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
        client.dashboard.registration.deregistration()


.. toctree::
    :maxdepth: 1

    status

