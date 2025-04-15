======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]


    class CreatePolicyApplicationProfileParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfTargetInterfacesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfTargetInterfacesOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Target:
        """
        Interfaces
        """

        interfaces: Union[
            OneOfTargetInterfacesOptionsDef1,
            OneOfTargetInterfacesOptionsDef2,
        ]


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ParcelReferenceDef:
        ref_id: RefId


    class OneOfQosMapQosSchedulersDropsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfQosMapQosSchedulersQueueOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfQosMapQosSchedulersBandwidthPercentOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfQosMapQosSchedulersSchedulingOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class QosSchedulers:
        bandwidth_percent: Optional[
            OneOfQosMapQosSchedulersBandwidthPercentOptionsDef
        ]
        class_map_ref: Optional[ParcelReferenceDef]
        drops: Optional[OneOfQosMapQosSchedulersDropsOptionsDef]
        queue: Optional[OneOfQosMapQosSchedulersQueueOptionsDef]
        scheduling: Optional[OneOfQosMapQosSchedulersSchedulingOptionsDef]


    class QosMap:
        """
        qos-map
        """

        qos_schedulers: Optional[List[QosSchedulers]]


    class Data:
        # qos-map
        qos_map: Optional[QosMap]
        # Interfaces
        target: Optional[Target]


    class CreatePolicyApplicationProfileParcelPostRequest:
        """
        Policy qos profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class QosPolicyOneOfTargetInterfacesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class QosPolicyTarget:
        """
        Interfaces
        """

        interfaces: Union[
            QosPolicyOneOfTargetInterfacesOptionsDef1,
            OneOfTargetInterfacesOptionsDef2,
        ]


    class QosPolicyOneOfQosMapQosSchedulersDropsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class QosPolicyOneOfQosMapQosSchedulersQueueOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class QosPolicyOneOfQosMapQosSchedulersBandwidthPercentOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class QosPolicyOneOfQosMapQosSchedulersSchedulingOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class QosPolicyQosSchedulers:
        bandwidth_percent: Optional[
            QosPolicyOneOfQosMapQosSchedulersBandwidthPercentOptionsDef
        ]
        class_map_ref: Optional[ParcelReferenceDef]
        drops: Optional[QosPolicyOneOfQosMapQosSchedulersDropsOptionsDef]
        queue: Optional[QosPolicyOneOfQosMapQosSchedulersQueueOptionsDef]
        scheduling: Optional[
            QosPolicyOneOfQosMapQosSchedulersSchedulingOptionsDef
        ]


    class QosPolicyQosMap:
        """
        qos-map
        """

        qos_schedulers: Optional[List[QosPolicyQosSchedulers]]


    class QosPolicyData:
        # qos-map
        qos_map: Optional[QosPolicyQosMap]
        # Interfaces
        target: Optional[QosPolicyTarget]


    class Payload:
        """
        Policy qos profile parcel schema for PUT request
        """

        data: QosPolicyData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanApplicationPriorityQosPolicyPayload:
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # Policy qos profile parcel schema for PUT request
        payload: Optional[Payload]


    class EditPolicyApplicationProfileParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class ApplicationPriorityQosPolicyOneOfTargetInterfacesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ApplicationPriorityQosPolicyTarget:
        """
        Interfaces
        """

        interfaces: Union[
            ApplicationPriorityQosPolicyOneOfTargetInterfacesOptionsDef1,
            OneOfTargetInterfacesOptionsDef2,
        ]


    class ApplicationPriorityQosPolicyOneOfQosMapQosSchedulersDropsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class ApplicationPriorityQosPolicyOneOfQosMapQosSchedulersQueueOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class ApplicationPriorityQosPolicyOneOfQosMapQosSchedulersBandwidthPercentOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class ApplicationPriorityQosPolicyOneOfQosMapQosSchedulersSchedulingOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class ApplicationPriorityQosPolicyQosSchedulers:
        bandwidth_percent: Optional[
            ApplicationPriorityQosPolicyOneOfQosMapQosSchedulersBandwidthPercentOptionsDef
        ]
        class_map_ref: Optional[ParcelReferenceDef]
        drops: Optional[
            ApplicationPriorityQosPolicyOneOfQosMapQosSchedulersDropsOptionsDef
        ]
        queue: Optional[
            ApplicationPriorityQosPolicyOneOfQosMapQosSchedulersQueueOptionsDef
        ]
        scheduling: Optional[
            ApplicationPriorityQosPolicyOneOfQosMapQosSchedulersSchedulingOptionsDef
        ]


    class ApplicationPriorityQosPolicyQosMap:
        """
        qos-map
        """

        qos_schedulers: Optional[
            List[ApplicationPriorityQosPolicyQosSchedulers]
        ]


    class ApplicationPriorityQosPolicyData:
        # qos-map
        qos_map: Optional[ApplicationPriorityQosPolicyQosMap]
        # Interfaces
        target: Optional[ApplicationPriorityQosPolicyTarget]


    class EditPolicyApplicationProfileParcelPutRequest:
        """
        Policy qos profile parcel schema for PUT request
        """

        data: ApplicationPriorityQosPolicyData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


