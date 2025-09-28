"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeScaling(HybridShape):

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
                |                         HybridShapeScaling
                | 
                | Represents the hybrid shape scaling feature object.
                | Role: To access the data of the hybrid shape feature object. This data
                | includes:
                | 
                |     The element to be transformed using the scaling
                |     The reference element for the scaling which is a point or a
                |     plane
                |     The ratio and its value
                | 
                | Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def center(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Center() As Reference
                |     Returns or sets the reference element.This element can be a point or a
                |     plane.
                |     Sub-element(s) supported (see Boundary object): PlanarFace or
                |     Vertex.
                | 
                |     Example:
                |         This example retrieves in RefElem the reference element for the Scaling
                |         hybrid shape feature.
                | 
                |          Dim RefElem As Reference
                |          Set RefElem = Scaling.Center

        :return: Reference
        """

        return Reference(self.com_object.Center)

    @center.setter
    def center(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Center = value

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
                |          the hybShpScaling hybrid shape scaling to creation
                |          
                | 
                |          hybShpScaling.CreationMode = True

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
    def elem_to_scale(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ElemToScale() As Reference
                |     Returns or sets the element to scale.
                | 
                |     Example:
                |         This example retrieves in Elem the element to scale for the Scaling
                |         hybrid shape feature.
                | 
                |          Dim Elem As Reference
                |          Set Elem = Scaling.ElemToScale

        :return: Reference
        """

        return Reference(self.com_object.ElemToScale)

    @elem_to_scale.setter
    def elem_to_scale(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ElemToScale = value

    @property
    def ratio(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Ratio() As RealParam (Read Only)
                |     Returns the scaling ratio.

        :return: RealParam
        """

        return RealParam(self.com_object.Ratio)

    @property
    def ratio_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RatioValue() As double
                |     Returns or sets the scaling ratio value.
                | 
                |     Example:
                |         This example retrieves in Value the ratio value for the Scaling hybrid
                |         shape feature.
                | 
                |          Dim Value As double
                |          Set Value = Scaling.RatioValue

        :return: float
        """

        return self.com_object.RatioValue

    @ratio_value.setter
    def ratio_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.RatioValue = value

    @property
    def volume_result(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property VolumeResult() As boolean
                |     Returns or sets the volume result.
                |     Legal values: True if the result of Scaling is required as volume (option
                |     is effective only in case of volumes,requires GSO License) and False if it is
                |     needed as surface .
                | 
                |     Example:
                | 
                |          This example sets that the result of
                |          the hybShpScaling hybrid shape scaling is volume.
                |          
                | 
                |          hybShpScaling.VolumeResult = True

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
        return f'HybridShapeScaling(name="{ self.name }")'
