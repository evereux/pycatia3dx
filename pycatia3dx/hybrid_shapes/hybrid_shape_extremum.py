"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeExtremum(HybridShape):

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
                |                         HybridShapeExtremum
                | 
                | Represents the hybrid shape extremum feature object.
                | Role: To access the data of the hybrid shape extremum feature object. This data
                | includes:
                | 
                |     The three directions into which the extremum is detected
                |     The object onto which the extremum is detected
                |     The extremum type of each direction
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeExtremum
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Direction() As HybridShapeDirection
                |     Returns or sets the direction into which the extremum is detected.

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.Direction)

    @direction.setter
    def direction(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.Direction = value

    @property
    def direction2(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Direction2() As HybridShapeDirection
                |     Returns or sets the second direction into which the extremum is detected.

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.Direction2)

    @direction2.setter
    def direction2(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.Direction2 = value

    @property
    def direction3(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Direction3() As HybridShapeDirection
                |     Returns or sets the third direction into which the extremum is detected.

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.Direction3)

    @direction3.setter
    def direction3(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.Direction3 = value

    @property
    def extremum_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ExtremumType() As long
                |     Returns or sets the extremum type.
                |     Legal values: 1 to get a maximum element or 0 to get a minimum element.

        :return: int
        """

        return self.com_object.ExtremumType

    @extremum_type.setter
    def extremum_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ExtremumType = value

    @property
    def extremum_type2(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ExtremumType2() As long
                |     Returns or sets the extremum type of the second direction.
                |     Legal values: 1 to get a maximum element or 0 to get a minimum element.

        :return: int
        """

        return self.com_object.ExtremumType2

    @extremum_type2.setter
    def extremum_type2(self, value: int):
        """
        :param int value:
        """

        self.com_object.ExtremumType2 = value

    @property
    def extremum_type3(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ExtremumType3() As long
                |     Returns or sets the extremum type of the third direction.
                |     Legal values: 1 to get a maximum element or 0 to get a minimum element.

        :return: int
        """

        return self.com_object.ExtremumType3

    @extremum_type3.setter
    def extremum_type3(self, value: int):
        """
        :param int value:
        """

        self.com_object.ExtremumType3 = value

    @property
    def reference_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ReferenceElement() As Reference
                |     Returns or sets the object on which the extremum is detected.

        :return: Reference
        """

        return Reference(self.com_object.ReferenceElement)

    @reference_element.setter
    def reference_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ReferenceElement = value

    def __repr__(self):
        return f'HybridShapeExtremum(name="{ self.name }")'
