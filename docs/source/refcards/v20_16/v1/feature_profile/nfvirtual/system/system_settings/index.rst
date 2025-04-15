===================================================
v1.feature_profile.nfvirtual.system.system_settings
===================================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/system-settings
-------------------------------------------------------------------------------------------


Create System settings  Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateNfvirtualSystemSettingsParcelPostRequest,
    ) -> CreateNfvirtualSystemSettingsParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.system_settings.post()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/system-settings/{systemSettingsId}
-------------------------------------------------------------------------------------------------------------


Get System Settings Profile Parcels for System feature profile

.. code:: python

    def get(
        system_id: str, system_settings_id: str
    ) -> GetSingleNfvirtualSystemSystemSettingsPayload: ...


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
        client.v1.feature_profile.nfvirtual.system.system_settings.get()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/system-settings/{systemSettingsId}
-------------------------------------------------------------------------------------------------------------


Edit a System Settings Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        system_settings_id: str,
        payload: EditNfvirtualSystemSettingsParcelPutRequest,
    ) -> EditNfvirtualSystemSettingsParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.system_settings.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/system-settings/{systemSettingsId}
----------------------------------------------------------------------------------------------------------------


Delete System settings Profile Parcel for System feature profile

.. code:: python

    def delete(system_id: str, system_settings_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.system.system_settings.delete()


.. toctree::
    :maxdepth: 1

    models

