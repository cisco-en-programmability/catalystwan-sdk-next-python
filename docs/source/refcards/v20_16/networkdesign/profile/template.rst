==============================
networkdesign.profile.template
==============================


Operation: GET /dataservice/networkdesign/profile/template
----------------------------------------------------------


Deprecated!!!

Generate profile template list

.. code:: python

    def generate_profile_template_list() -> List[Any]: ...


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
        client.networkdesign.profile.template.generate_profile_template_list()


Operation: GET /dataservice/networkdesign/profile/template/{templateId}
-----------------------------------------------------------------------


Deprecated!!!

Get device profile template

.. code:: python

    def get_device_profile_template(template_id: str) -> Any: ...


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
        client.networkdesign.profile.template.get_device_profile_template()


Operation: PUT /dataservice/networkdesign/profile/template/{templateId}
-----------------------------------------------------------------------


Deprecated!!!

Edit device profile template

.. code:: python

    def edit_device_profile_template(
        template_id: str, payload: Optional[Any] = None
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
        client.networkdesign.profile.template.edit_device_profile_template()


