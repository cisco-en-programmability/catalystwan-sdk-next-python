========================================
v1.feature_profile.sdwan.system.security
========================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/security
-------------------------------------------------------------------------------


Get Security for System feature profile

.. code:: python

    def get_security_for_system(system_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.system.security.get_security_for_system()


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/security
--------------------------------------------------------------------------------


Create Security for System feature profile

.. code:: python

    def create_security_for_system(
        system_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.system.security.create_security_for_system()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/security/{securityId}
--------------------------------------------------------------------------------------------


Get Security by securityId for System feature profile

.. code:: python

    def get_security_by_security_id_for_system(
        system_id: str, security_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.system.security.get_security_by_security_id_for_system()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/security/{securityId}
--------------------------------------------------------------------------------------------


Update Security for System feature profile

.. code:: python

    def edit_security_for_system(
        system_id: str, security_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.system.security.edit_security_for_system()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/security/{securityId}
-----------------------------------------------------------------------------------------------


Delete Security for System feature profile

.. code:: python

    def delete_security_for_system(
        system_id: str, security_id: str
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
        client.v1.feature_profile.sdwan.system.security.delete_security_for_system()


