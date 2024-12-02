===================================================
v1.feature_profile.nfvirtual.system.system_settings
===================================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/system-settings
-------------------------------------------------------------------------------------------


Create System settings  Profile Parcel for System feature profile

.. code:: python

    def create_nfvirtual_system_settings_parcel(
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
        client.v1.feature_profile.nfvirtual.system.system_settings.create_nfvirtual_system_settings_parcel()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/system-settings/{systemSettingsId}
-------------------------------------------------------------------------------------------------------------


Get System Settings Profile Parcels for System feature profile

.. code:: python

    def get_nfvirtual_system_settings_parcel(
        system_id: str, system_settings_id: str
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
        client.v1.feature_profile.nfvirtual.system.system_settings.get_nfvirtual_system_settings_parcel()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/system-settings/{systemSettingsId}
-------------------------------------------------------------------------------------------------------------


Edit a System Settings Profile Parcel for System feature profile

.. code:: python

    def edit_nfvirtual_system_settings_parcel(
        system_id: str,
        system_settings_id: str,
        payload: Optional[str] = None,
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
        client.v1.feature_profile.nfvirtual.system.system_settings.edit_nfvirtual_system_settings_parcel()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/system-settings/{systemSettingsId}
----------------------------------------------------------------------------------------------------------------


Delete System settings Profile Parcel for System feature profile

.. code:: python

    def delete_nfvirtual_system_settings_parcel(
        system_id: str, system_settings_id: str
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
        client.v1.feature_profile.nfvirtual.system.system_settings.delete_nfvirtual_system_settings_parcel()


