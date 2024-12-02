=====================================
dashboard.get_controller_client_token
=====================================


Operation: POST /dataservice/dashboard/getControllerClientToken
---------------------------------------------------------------


Register Controller to BiFrost Dashboard (by Controller)

.. code:: python

    def get_controller_client_token(
        payload: Optional[Any] = None,
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
        client.dashboard.get_controller_client_token.get_controller_client_token()


