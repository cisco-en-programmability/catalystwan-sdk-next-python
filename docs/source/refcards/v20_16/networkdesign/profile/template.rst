==============================
networkdesign.profile.template
==============================


Operation: PUT /dataservice/networkdesign/profile/template/{templateId}
-----------------------------------------------------------------------


Deprecated!!!

Edit device profile template

.. code:: python

    def put(template_id: str, payload: Any) -> None: ...


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
        client.networkdesign.profile.template.put()


Operation: GET /dataservice/networkdesign/profile/template
----------------------------------------------------------


Deprecated!!!

.. code:: python

    @overload
    def get() -> List[Any]: ...


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
        client.networkdesign.profile.template.get()


Operation: GET /dataservice/networkdesign/profile/template/{templateId}
-----------------------------------------------------------------------


Deprecated!!!

.. code:: python

    @overload
    def get(template_id: str) -> Any: ...


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
        client.networkdesign.profile.template.get()


