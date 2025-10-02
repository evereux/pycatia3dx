"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimThicknessControl(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimThicknessControl
                | 
                | Represents the thickness control object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimThicknessControl as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyThicknessControl As SimThicknessControl
                |      Set MyThicknessControl = MyFeatures.Add("SimThicknessControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimThicknessControl named "Thickness Control.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyThicknessControl As SimThicknessControl
                |      Set MyThicknessControl = MyFeatures.Item("Thickness Control.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimThicknessControl as following:
                | 
                |      ...
                |      MyThicknessControl = MyFeatures.Add("SimThicknessControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimThicknessControl named "Thickness Control.1" as
                |     following:
                | 
                |      ...
                |      MyThicknessControl = MyFeatures.Item("Thickness Control.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_maximum_thickness(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaximumThickness(double oVal)
                |     Gets the Maximum thickness.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: LENGTH, units:m

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMaximumThickness(o_val)

    def get_minimum_thickness(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMinimumThickness(double oVal)
                |     Gets the Minimum thickness.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Constraint value. Quantity: LENGTH, units:m

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMinimumThickness(o_val)

    def set_maximum_thickness(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaximumThickness(double iVal)
                |     Sets the Maximum thickness.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: LENGTH, units:m

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMaximumThickness(i_val)

    def set_minimum_thickness(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMinimumThickness(double iVal)
                |     Sets the Minimum thickness.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: LENGTH, units:m

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMinimumThickness(i_val)

    def __repr__(self):
        return f'SimThicknessControl(name="{ self.name }")'
