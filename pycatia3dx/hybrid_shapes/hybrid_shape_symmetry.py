"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeSymmetry(HybridShape):

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
                |                         HybridShapeSymmetry
                | 
                | Represents the hybrid shape symmetry feature object.
                | Role: To access the data of the symmetry shape feature object. The data
                | includes:
                | 
                |     The element to be transformed
                |     The reference element which can be a point, a line or a
                |     plane
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | 
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
                |          the hybShpSymmetry hybrid shape symmetry to creation
                |          
                | 
                |          hybShpSymmetry.CreationMode = True

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
    def elem_to_symmetry(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ElemToSymmetry() As Reference
                |     Returns or sets the element to transform.
                | 
                |     Example:
                |         This example retrieves in Elem the element to transform for the
                |         Symmetry hybrid shape feature.
                | 
                |          Dim Elem As Reference
                |          Set Elem = Symmetry.ElemToSymmetry

        :return: Reference
        """

        return Reference(self.com_object.ElemToSymmetry)

    @elem_to_symmetry.setter
    def elem_to_symmetry(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ElemToSymmetry = value

    @property
    def reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Reference() As Reference
                |     Returns or sets the reference element.This element can be a point, a line
                |     or a plane.
                |     Sub-element(s) supported (see Boundary object): PlanarFace, Edge or
                |     Vertex.
                | 
                |     Example:
                |         This example retrieves in Ref the reference element for the Symmetry
                |         hybrid shape feature.
                | 
                |          Dim Ref As Reference
                |          Set Ref = Symmetry.Reference

        :return: Reference
        """

        return Reference(self.com_object.Reference)

    @reference.setter
    def reference(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Reference = value

    @property
    def volume_result(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property VolumeResult() As boolean
                |     Returns or sets the volume result.
                |     Legal values: True if the result of symmetry is required as volume (option
                |     is effective only in case of volumes, requires GSO License) and False if it is
                |     needed as surface .
                | 
                |     Example:
                | 
                |          This example sets that the result of
                |          the hybShpSymmetry hybrid shape symmetry is volume.
                |          
                | 
                |          hybShpSymmetry.VolumeResult = True

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
        return f'HybridShapeSymmetry(name="{ self.name }")'
