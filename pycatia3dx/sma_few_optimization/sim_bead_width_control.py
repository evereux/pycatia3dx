"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimBeadWidthControl(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimBeadWidthControl
                | 
                | Represents the Bead Width control object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimBeadWidthControl as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyBeadWidthControl As SimBeadWidthControl
                |      Set MyBeadWidthControl = MyFeatures.Add("SimBeadWidthControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimBeadWidthControl named "Bead Width Control.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyBeadWidthControl As SimBeadWidthControl
                |      Set MyBeadWidthControl = MyFeatures.Item("Bead Width Control.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimBeadWidthControl as following:
                | 
                |      ...
                |      MyBeadWidthControl = MyFeatures.Add("SimBeadWidthControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimBeadWidthControl named "Bead Width Control.1" as
                |     following:
                | 
                |      ...
                |      MyBeadWidthControl = MyFeatures.Item("Bead Width Control.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_minimum_width(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMinimumWidth(double oVal)
                |     Gets the Minimum Width.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Width value. Quantity: Width, units: m

        :param float o_val:
        :return: None
        """
        return self.com_object.GetMinimumWidth(o_val)

    def set_minimum_width(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMinimumWidth(double iVal)
                |     Sets the Minimum Width.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Width value. Quantity: Width, units: m

        :param float i_val:
        :return: None
        """
        return self.com_object.SetMinimumWidth(i_val)

    def __repr__(self):
        return f'SimBeadWidthControl(name="{ self.name }")'
