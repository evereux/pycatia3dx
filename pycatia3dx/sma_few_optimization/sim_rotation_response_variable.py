"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_few_optimization.sim_non_parametric_response_variable import SimNonParametricResponseVariable
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem


class SimRotationResponseVariable(SimNonParametricResponseVariable):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    SMAFeaOptimizationIDLItf.SimDesignImprovementResponseVariable
                |                        SMAFeaOptimizationIDLItf.SimNonParametricResponseVariable
                |                             SimRotationResponseVariable
                | 
                | Represents the rotation response variable object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimRotationResponseVariable as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyRotationResponseVariable As
                |      SimRotationResponseVariable
                |      Set MyRotationResponseVariable = MyFeatures.Add("SimRotationResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimRotationResponseVariable named "Rotation Response Variable.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyRotationResponseVariable As
                |      SimRotationResponseVariable
                |      Set MyRotationResponseVariable = MyFeatures.Item("Rotation Response Variable.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimRotationResponseVariable as following:
                | 
                |      ...
                |      MyRotationResponseVariable = MyFeatures.Add("SimRotationResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimRotationResponseVariable named "Rotation Response Variable.1" as
                |     following:
                | 
                |      ...
                |      MyRotationResponseVariable = MyFeatures.Item("Rotation Response Variable.1")
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
                |     Returns the axis system used for the rotation design response.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def direction(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Direction() As SimDesignResponseDirection
                |     Returns or sets the direction of rotation design response.

        :return: int
        """

        return self.com_object.Direction

    @direction.setter
    def direction(self, value: int):
        """
        :param int value:
        """

        self.com_object.Direction = value

    @property
    def load_case(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LoadCase() As CATBaseDispatch (Read Only)
                |     Returns the Linear Loadcase.

        :return: AnyObject
        """

        return AnyObject(self.com_object.LoadCase)

    @property
    def use_absolute_value_of_direction_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UseAbsoluteValueOfDirectionFlag() As boolean

        :return: bool
        """

        return self.com_object.UseAbsoluteValueOfDirectionFlag

    @use_absolute_value_of_direction_flag.setter
    def use_absolute_value_of_direction_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UseAbsoluteValueOfDirectionFlag = value

    def __repr__(self):
        return f'SimRotationResponseVariable(name="{ self.name }")'
