=====================================
v1.feature_profile.sdwan.system.basic
=====================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/basic
----------------------------------------------------------------------------


Get Basic Profile Feature for System feature profile

.. code:: python

    def get_basic_profile_feature_for_system(system_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.system.basic.get_basic_profile_feature_for_system()


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/basic
-----------------------------------------------------------------------------


Create a Basic Profile Feature for System feature profile

.. code:: python

    def create_basic_profile_feature_for_system(
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
        client.v1.feature_profile.sdwan.system.basic.create_basic_profile_feature_for_system()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/basic/{basicId}
--------------------------------------------------------------------------------------


Get Basic Profile Feature by FeatureId for System feature profile

.. code:: python

    def get_basic_profile_feature_by_feature_id_for_system(
        system_id: str, basic_id: str
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
        client.v1.feature_profile.sdwan.system.basic.get_basic_profile_feature_by_feature_id_for_system()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/basic/{basicId}
--------------------------------------------------------------------------------------


Update a Basic Profile Feature for System feature profile

.. code:: python

    def edit_basic_profile_feature_for_system(
        system_id: str, basic_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.system.basic.edit_basic_profile_feature_for_system()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/basic/{basicId}
-----------------------------------------------------------------------------------------


Delete a Basic Profile Feature for System feature profile

.. code:: python

    def delete_basic_profile_feature_for_system(
        system_id: str, basic_id: str
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
        client.v1.feature_profile.sdwan.system.basic.delete_basic_profile_feature_for_system()


.. toctree::
    :maxdepth: 1

    schema/index

