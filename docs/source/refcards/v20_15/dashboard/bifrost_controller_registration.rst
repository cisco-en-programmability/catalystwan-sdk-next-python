=========================================
dashboard.bifrost_controller_registration
=========================================


Operation: POST /dataservice/dashboard/bifrostControllerRegistration
--------------------------------------------------------------------


Register Controller to BiFrost Dashboard (by Controller)

.. code:: python

    def bifrost_controller_registration() -> None: ...


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
        client.dashboard.bifrost_controller_registration.bifrost_controller_registration()


