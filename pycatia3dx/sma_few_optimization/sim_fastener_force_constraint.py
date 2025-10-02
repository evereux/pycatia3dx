"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimFastenerForceConstraint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimFastenerForceConstraint
                | 
                | Represents the fastener force constraint object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimFastenerForceConstraint as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyFastenerForceConstraint As
                |      SimFastenerForceConstraint
                |      Set MyFastenerForceConstraint = MyFeatures.Add("SimFastenerForceConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimFastenerForceConstraint named "Fastener Force Constraint.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyFastenerForceConstraint As
                |      SimFastenerForceConstraint
                |      Set MyFastenerForceConstraint = MyFeatures.Item("Fastener Force Constraint.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimFastenerForceConstraint as following:
                | 
                |      ...
                |      MyFastenerForceConstraint = MyFeatures.Add("SimFastenerForceConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimFastenerForceConstraint named "Fastener Force Variable.1" as
                |     following:
                | 
                |      ...
                |      MyFastenerForceConstraint = MyFeatures.Item("Fastener Force Variable.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def load_case(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LoadCase() As CATBaseDispatch (Read Only)
                |     Returns the Linear Loadcase used for the fastener force constraint.

        :return: AnyObject
        """

        return AnyObject(self.com_object.LoadCase)

    def get_maximum_shear(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximumShear(double oVal)
                |     Gets the Maximum Shear
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: FORCE, units:N

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximumShear(o_val)

    def get_maximum_tension(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximumTension(double oVal)
                |     Gets the Maximum Tension.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: FORCE, units:N

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximumTension(o_val)

    def set_maximum_shear(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumShear(double iVal)

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximumShear(i_val)

    def set_maximum_tension(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumTension(double iVal)
                |     Sets the Maximum Tension.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: FORCE, units:N

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximumTension(i_val)

    def __repr__(self):
        return f'SimFastenerForceConstraint(name="{ self.name }")'
