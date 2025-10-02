"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_sma_mpa_base.sim_axis_system import SimAxisSystem


class SimDisplacementConstraint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimDisplacementConstraint
                | 
                | Represents the displacement constraint object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimDisplacementConstraint as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyDisplacementConstraint As SimDisplacementConstraint
                |      Set MyDisplacementConstraint = MyFeatures.Add("SimDisplacementConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimDisplacementConstraint named "Displacement Constraint.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyDisplacementConstraint As SimDisplacementConstraint
                |      Set MyDisplacementConstraint = MyFeatures.Item("Displacement Constraint.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimDisplacementConstraint as following:
                | 
                |      ...
                |      MyDisplacementConstraint = MyFeatures.Add("SimDisplacementConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimDisplacementConstraint named "Displacement Constraint.1" as
                |     following:
                | 
                |      ...
                |      MyDisplacementConstraint = MyFeatures.Item("Displacement Constraint.1")
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
                |     Returns the axis system used for the displacement constraint.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

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
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As SimDisplacementConstraintType
                |     Returns or sets the type of displacement constraint.

        :return: SimDisplacementConstraintType
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def get_maximum_displacement(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximumDisplacement(double oVal)
                |     Gets the Maximum Displacement.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: Displacement, units: m

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximumDisplacement(o_val)

    def get_maximum_total_displacement(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximumTotalDisplacement(double oVal)
                |     Gets the Maximum Total Displacement.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: Displacement, units: m

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximumTotalDisplacement(o_val)

    def get_minimum_displacement(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMinimumDisplacement(double oVal)
                |     Gets the Minimum Displacement.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: Displacement, units: m

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMinimumDisplacement(o_val)

    def set_maximum_displacement(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumDisplacement(double iVal)
                |     Sets the Maximum Displacement.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: Displacement, units: m

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximumDisplacement(i_val)

    def set_maximum_total_displacement(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumTotalDisplacement(double iVal)
                |     Sets the Maximum Total Displacement.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: Displacement, units: m

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximumTotalDisplacement(i_val)

    def set_minimum_displacement(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMinimumDisplacement(double iVal)
                |     Sets the Minimum Displacement.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: Displacement, units: m

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMinimumDisplacement(i_val)

    def __repr__(self):
        return f'SimDisplacementConstraint(name="{ self.name }")'
