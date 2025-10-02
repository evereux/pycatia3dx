"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimGeneralConstraint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimGeneralConstraint
                | 
                | Represents the general constraint object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimGeneralConstraint as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyGeneralConstraint As SimGeneralConstraint
                |      Set MyGeneralConstraint = MyFeatures.Add("SimGeneralConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimGeneralConstraint named "General Constraint.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyGeneralConstraint As SimGeneralConstraint
                |      Set MyGeneralConstraint = MyFeatures.Item("General Constraint.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimGeneralConstraint as following:
                | 
                |      ...
                |      MyGeneralConstraint = MyFeatures.Add("SimGeneralConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimGeneralConstraint named "General Constraint.1" as
                |     following:
                | 
                |      ...
                |      MyGeneralConstraint = MyFeatures.Item("General Constraint.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_maximum(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximum(double oVal)
                |     Gets the Maximum value.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: Response variable units

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximum(o_val)

    def get_minimum(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMinimum(double oVal)
                |     Gets the Minimum value.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: Response variable units

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMinimum(o_val)

    def set_maximum(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximum(double iVal)
                |     Sets the Maximum value.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: Response variable units

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximum(i_val)

    def set_minimum(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMinimum(double iVal)
                |     Sets the Minimum value.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: Response variable units

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMinimum(i_val)

    def __repr__(self):
        return f'SimGeneralConstraint(name="{ self.name }")'
