===========================================
v1.feature_profile.sdwan.other.thousandeyes
===========================================


Operation: GET /dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes
---------------------------------------------------------------------------------


Get Thousandeyes Profile Parcels for Other feature profile

.. code:: python

    def get_thousandeyes_profile_parcel_for_other(
        other_id: str,
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
        client.v1.feature_profile.sdwan.other.thousandeyes.get_thousandeyes_profile_parcel_for_other()


Operation: POST /dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes
----------------------------------------------------------------------------------


Create a Thousandeyes Profile Parcel for Other feature profile

.. code:: python

    def create_thousandeyes_profile_parcel_for_other(
        other_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.other.thousandeyes.create_thousandeyes_profile_parcel_for_other()


Operation: GET /dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes/{thousandeyesId}
--------------------------------------------------------------------------------------------------


Get Thousandeyes Profile Parcel by parcelId for Other feature profile

.. code:: python

    def get_thousandeyes_profile_parcel_by_parcel_id_for_other(
        other_id: str, thousandeyes_id: str
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
        client.v1.feature_profile.sdwan.other.thousandeyes.get_thousandeyes_profile_parcel_by_parcel_id_for_other()


Operation: PUT /dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes/{thousandeyesId}
--------------------------------------------------------------------------------------------------


Update a Thousandeyes Profile Parcel for Other feature profile

.. code:: python

    def edit_thousandeyes_profile_parcel_for_other(
        other_id: str, thousandeyes_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.other.thousandeyes.edit_thousandeyes_profile_parcel_for_other()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes/{thousandeyesId}
-----------------------------------------------------------------------------------------------------


Delete a Thousandeyes Profile Parcel for Other feature profile

.. code:: python

    def delete_thousandeyes_profile_parcel_for_other(
        other_id: str, thousandeyes_id: str
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
        client.v1.feature_profile.sdwan.other.thousandeyes.delete_thousandeyes_profile_parcel_for_other()


.. toctree::
    :maxdepth: 1

    schema/index

