"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem


class SimRibControl(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimRibControl
                | 
                | Represents the rib control object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a SimRibControl
                |     as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyRibControl As SimRibControl
                |      Set MyRibControl = MyFeatures.Add("SimRibControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimRibControl named "Rib Control.1" as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyRibControl As SimRibControl
                |      Set MyRibControl = MyFeatures.Item("Rib Control.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a SimRibControl
                |     as following:
                | 
                |      ...
                |      MyRibControl = MyFeatures.Add("SimRibControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimRibControl named "Rib Control.1" as following:
                | 
                |      ...
                |      MyRibControl = MyFeatures.Item("Rib Control.1")
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
                |     Returns the axis system used for the rib control.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    def get_rib_distance(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetRibDistance(double oVal)
                |     Gets the Rib Distance.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Distance value. Quantity: Distance, units: m

        :param float o_val:
        :return: None
        """
        return self.com_object.GetRibDistance(o_val)

    def get_rib_thickness(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetRibThickness(double oVal)
                |     Gets the Rib Thickness.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Thickness value. Quantity: Thickness, units: m

        :param float o_val:
        :return: None
        """
        return self.com_object.GetRibThickness(o_val)

    def set_rib_distance(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRibDistance(double iVal)
                |     Sets the Rib Distance.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Constraint value. Quantity: Distance, units: m

        :param float i_val:
        :return: None
        """
        return self.com_object.SetRibDistance(i_val)

    def set_rib_thickness(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRibThickness(double iVal)
                |     Sets the Rib Thickness.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Thickness value. Quantity: Thickness, units: m

        :param float i_val:
        :return: None
        """
        return self.com_object.SetRibThickness(i_val)

    def __repr__(self):
        return f'SimRibControl(name="{ self.name }")'
