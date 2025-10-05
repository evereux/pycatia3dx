"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem


class SimOverhangControl(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimOverhangControl
                | 
                | Represents the overhang constraint object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimOverhangControl as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyOverhangConstraint As SimOverhangControl
                |      Set MyOverhangConstraint = MyFeatures.Add("SimOverhangControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimOverhangControl named "Overhang Constraint.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyOverhangConstraint As SimOverhangControl
                |      Set MyOverhangConstraint = MyFeatures.Item("Overhang Constraint.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimOverhangControl as following:
                | 
                |      ...
                |      MyOverhangConstraint = MyFeatures.Add("SimOverhangControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimOverhangControl named "Overhang Constraint.1" as
                |     following:
                | 
                |      ...
                |      MyOverhangConstraint = MyFeatures.Item("Overhang Constraint.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisSystem() As SimAxisSystem (Read Only)
                |     Returns the axis system used for overhang constraint.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def base_plane(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BasePlane() As SimBasePlaneType
                |     Returns or sets the type of Base plane.

        :return: int
        """

        return self.com_object.BasePlane

    @base_plane.setter
    def base_plane(self, value: int):
        """
        :param int value:
        """

        self.com_object.BasePlane = value

    @property
    def specify_support_frozen_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecifySupportFrozenFlag() As boolean
                |     Returns or sets the prevent overhang for functional regions flag.
                |     FALSE : No overhang for functional regions,
                |     TRUE : Overhang considers functional regions.

        :return: bool
        """

        return self.com_object.SpecifySupportFrozenFlag

    @specify_support_frozen_flag.setter
    def specify_support_frozen_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SpecifySupportFrozenFlag = value

    def get_maximum_overhang_angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaximumOverhangAngle() As double
                |     Gets the Maximum Overhang Angle
                | 
                |     Parameters:
                | 
                |         oAngle
                |             [out] Constraint value. Quantity: ANGLE, units: rad

        :return: float
        """
        return self.com_object.GetMaximumOverhangAngle()

    def set_maximum_overhang_angle(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumOverhangAngle(double iAngle)
                |     Sets the Maximum Overhang Angle
                | 
                |     Parameters:
                | 
                |         iAngle
                |             [in] Constraint value. Quantity: ANGLE, units: rad

        :param float i_angle:
        :return: None
        """
        return self.com_object.SetMaximumOverhangAngle(i_angle)

    def __repr__(self):
        return f'SimOverhangControl(name="{ self.name }")'
