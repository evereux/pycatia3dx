"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimMassConstraint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMassConstraint
                | 
                | Represents the mass constraint object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimMassConstraint as following :
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyMassConstraint As SimMassConstraint
                |      Set MyMassConstraint = MyFeatures.Add("SimMassConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures< / code> object, you can retrieve a
                |     SimMassConstraint< / code> named " Mass Constraint.1" as following
                |     :
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyMassConstraint As SimMassConstraint
                |      Set MyMassConstraint = MyFeatures.Item("Mass Constraint.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimMassConstraint as following:
                | 
                |      ...
                |      MyMassConstraint = MyFeatures.Add("SimMassConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimMassConstraint named "Mass Constraint.1" as following:
                | 
                |      ...
                |      MyMassConstraint = MyFeatures.Item("Mass Constraint.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As SimMassConstraintType
                |     Returns or sets the type of mass constraint.

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def get_absolute_mass_target(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAbsoluteMassTarget(double oVal)
                |     Gets the absolute mass target.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: WEIGHT, units:kg

        :param float o_val:
        :return: None
        """
        return self.com_object.GetAbsoluteMassTarget(o_val)

    def get_target_mass_ratio(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTargetMassRatio(double oVal)
                |     Gets the relative mass target.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: WEIGHT, units:%

        :param float o_val:
        :return: None
        """
        return self.com_object.GetTargetMassRatio(o_val)

    def set_absolute_mass_target(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAbsoluteMassTarget(double iVal)
                |     Sets the absolute mass target.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: WEIGHT, units:kg

        :param float i_val:
        :return: None
        """
        return self.com_object.SetAbsoluteMassTarget(i_val)

    def set_target_mass_ratio(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTargetMassRatio(double iVal)
                |     Sets the relative mass target.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: WEIGHT, units:%

        :param float i_val:
        :return: None
        """
        return self.com_object.SetTargetMassRatio(i_val)

    def __repr__(self):
        return f'SimMassConstraint(name="{ self.name }")'
