"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeAxisToAxis(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapeAxisToAxis
                | 
                | Represents the hybrid shape axis to axis transformation feature
                | object.
                | Role: To access the data of the axis to axis transformation shape feature
                | object. The data includes:
                | 
                |     The element to be transformed
                |     The reference axis system
                |     The target axis system
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def creation_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CreationMode() As boolean
                |     Returns or sets the creation mode(creation or
                |     modification).
                |     Legal values: True if the result is a creation feature and False if the
                |     result is a modification feature.
                | 
                |     Example:
                | 
                |          This example sets that the mode of
                |          the hybShpAxisToAxis hybrid shape axis to axis to
                |          creation
                |          
                | 
                |          hybShpAxisToAxis.CreationMode = True

        :return: bool
        """

        return self.com_object.CreationMode

    @creation_mode.setter
    def creation_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CreationMode = value

    @property
    def elem_to_transform(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ElemToTransform() As Reference
                |     Returns or sets the element to transform.
                | 
                |     Example:
                |         This example retrieves in Elem the element to transform for the
                |         AxisToAxis hybrid shape feature.
                | 
                |          Dim Elem As Reference
                |          Set Elem = AxisToAxis.ElemToTransform

        :return: Reference
        """

        return Reference(self.com_object.ElemToTransform)

    @elem_to_transform.setter
    def elem_to_transform(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ElemToTransform = value

    @property
    def reference_axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ReferenceAxis() As Reference
                |     Returns or sets the reference axis.
                | 
                |     Example:
                |         This example retrieves in Ref the reference axis for the AxisToAxis
                |         hybrid shape feature.
                | 
                |          Dim Ref As Reference
                |          Set Ref = AxisToAxis.ReferenceAxis

        :return: Reference
        """

        return Reference(self.com_object.ReferenceAxis)

    @reference_axis.setter
    def reference_axis(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ReferenceAxis = value

    @property
    def target_axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TargetAxis() As Reference
                |     Returns or sets the target axis.
                | 
                |     Example:
                |         This example retrieves in Ref the target axis for the AxisToAxis hybrid
                |         shape feature.
                | 
                |          Dim Ref As Reference
                |          Set Ref = AxisToAxis.ReferenceAxis

        :return: Reference
        """

        return Reference(self.com_object.TargetAxis)

    @target_axis.setter
    def target_axis(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.TargetAxis = value

    @property
    def volume_result(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property VolumeResult() As boolean
                |     Returns or sets the volume result.
                |     Legal values: True if the result of axis to axis transformation is required
                |     as volume (option is effective only in case of volumes,requires GSO License))
                |     and False if it is needed as surface .
                | 
                |     Example:
                | 
                |          This example sets that the result of
                |          the hybShpAxisToAxis hybrid shape AxisToAxis is
                |          volume.
                |          
                | 
                |          hybShpAxisToAxis.VolumeResult = True

        :return: bool
        """

        return self.com_object.VolumeResult

    @volume_result.setter
    def volume_result(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.VolumeResult = value

    def __repr__(self):
        return f'HybridShapeAxisToAxis(name="{ self.name }")'
