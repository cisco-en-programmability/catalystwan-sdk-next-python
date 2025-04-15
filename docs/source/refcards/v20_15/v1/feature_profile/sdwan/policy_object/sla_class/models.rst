======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    EntriesCriteriaDef = Literal[
        "jitter",
        "jitter-latency",
        "jitter-latency-loss",
        "jitter-loss",
        "jitter-loss-latency",
        "latency",
        "latency-jitter",
        "latency-jitter-loss",
        "latency-loss",
        "latency-loss-jitter",
        "loss",
        "loss-jitter",
        "loss-jitter-latency",
        "loss-latency",
        "loss-latency-jitter",
    ]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class OneOfEntriesLatencyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesLossOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesJitterOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ParcelReferenceDef:
        ref_id: RefId


    class OneOfEntriesCriteriaOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesCriteriaDef


    class FallbackBestTunnel:
        """
        Object with a criteria and variance
        """

        criteria: Optional[OneOfEntriesCriteriaOptionsDef]
        jitter_variance: Optional[OneOfEntriesJitterOptionsDef]
        latency_variance: Optional[OneOfEntriesLatencyOptionsDef]
        loss_variance: Optional[OneOfEntriesLossOptionsDef]


    class Entries1:
        latency: OneOfEntriesLatencyOptionsDef
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[FallbackBestTunnel]
        jitter: Optional[OneOfEntriesJitterOptionsDef]
        loss: Optional[OneOfEntriesLossOptionsDef]


    class Entries2:
        loss: OneOfEntriesLossOptionsDef
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[FallbackBestTunnel]
        jitter: Optional[OneOfEntriesJitterOptionsDef]
        latency: Optional[OneOfEntriesLatencyOptionsDef]


    class Entries3:
        jitter: OneOfEntriesJitterOptionsDef
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[FallbackBestTunnel]
        latency: Optional[OneOfEntriesLatencyOptionsDef]
        loss: Optional[OneOfEntriesLossOptionsDef]


    class Data:
        # Sla class List
        entries: List[Union[Entries1, Entries2, Entries3]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        Sla class profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Payload:
        """
        Sla class profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # Sla class profile parcel schema for POST request
        payload: Optional[Payload]


