"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape


class HybridShapeThickness(HybridShape):

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
                |                         HybridShapeThickness
                | 
                | Represents the hybrid shape Thickness feature object.
                | Role: To access the data of the thickness on an hybrid shape feature object.
                | This data includes:
                | 
                |     The thickness orientation
                |     The thickness1 value
                |     The thickness2 value
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation() As long
                |     Returns or sets the orientation.
                |     Role:
                |     Orientation = 1 means that the first thickness is measured with the normal of the support Orientation = -1 means that the first thickness is measured with the inverted normal of the support
                | 
                |     Example:
                |         This example retrieves in Orient the orientation for the Thickness1
                |         hybrid shape feature.
                | 
                |          Dim Orient As long
                |          Set Orient = Thickness1.Orientation

        :return: int
        """

        return self.com_object.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.Orientation = value

    @property
    def thickness1(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Thickness1() As double
                |     Returns or sets the first thickness value in mm.
                | 
                |     Example: This example retrieves in ThickVal1 the first thickness value for
                |     the Thick hybrid shape feature.
                | 
                |      Dim ThickVal1 As double
                |      Set ThickVal1 = Thick.Thickness1

        :return: float
        """

        return self.com_object.Thickness1

    @thickness1.setter
    def thickness1(self, value: float):
        """
        :param float value:
        """

        self.com_object.Thickness1 = value

    @property
    def thickness1_value(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Thickness1Value() As Length (Read Only)
                |     Returns the first thickness value.
                | 
                |     Example:
                |         This example retrieves in ThickVal1 the first thickness value for the
                |         Thick hybrid shape feature.
                | 
                |          Dim ThickVal1 As Length
                |          Set ThickVal1 = Thick.Thickness1Value

        :return: Length
        """

        return Length(self.com_object.Thickness1Value)

    @property
    def thickness2(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Thickness2() As double
                |     Returns or sets the second thickness value in mm.
                | 
                |     Example: This example retrieves in ThickVal2 the second thickness value for
                |     the Thick hybrid shape feature.
                | 
                |      Dim ThickVal2 As double
                |      Set ThickVal2 = Thick.Thickness2

        :return: float
        """

        return self.com_object.Thickness2

    @thickness2.setter
    def thickness2(self, value: float):
        """
        :param float value:
        """

        self.com_object.Thickness2 = value

    @property
    def thickness2_value(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Thickness2Value() As Length (Read Only)
                |     Returns the second thickness value.
                | 
                |     Example:
                |         This example retrieves in ThickVal2 the second thickness value for the
                |         Thick hybrid shape feature.
                | 
                |          Dim ThickVal2 As Length
                |          Set ThickVal2 = Thick.Thickness2Value

        :return: Length
        """

        return Length(self.com_object.Thickness2Value)

    def __repr__(self):
        return f'HybridShapeThickness(name="{ self.name }")'
