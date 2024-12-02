============================================================
v1.feature_profile.sdwan.policy_object.unified.url_filtering
============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/url-filtering
----------------------------------------------------------------------------------------------------------


Create Feature for Security Policy

.. code:: python

    def create_security_profile_parcel(
        policy_object_id: str,
        payload: Optional[
            Union[
                Union[
                    CreateSecurityProfileParcelPostRequest11,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest21,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest31,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest41,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest31,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest61,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest31,
                    CreateSecurityProfileParcelPostRequest12,
                ],
            ]
        ] = None,
    ) -> CreateSecurityProfileParcelPostResponse: ...


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
        client.v1.feature_profile.sdwan.policy_object.unified.url_filtering.create_security_profile_parcel()


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/url-filtering/{parcelId}
--------------------------------------------------------------------------------------------------------------------


Get Security Features for a given ParcelType

.. code:: python

    def get_security_profile_parcel(
        policy_object_id: str,
        parcel_id: str,
        reference_count: Optional[bool] = False,
    ) -> GetSecurityProfileParcelGetResponse: ...


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
        client.v1.feature_profile.sdwan.policy_object.unified.url_filtering.get_security_profile_parcel()


.. toctree::
    :maxdepth: 1

    models

