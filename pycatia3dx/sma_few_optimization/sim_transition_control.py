"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimTransitionControl(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimTransitionControl
                | 
                | Represents the Transition Control object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimTransitionControl as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      Dim MyLocalOptimizationArea As SimLocalOptimizationArea
                |      ...
                |      Dim MyTransitionControl As SimTransitionControl
                |      Set MyTransitionControl = MyFeatures.AddSubFeature("SimTransitionControl", MyLocalOptimizationArea)
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimTransitionControl as following:
                | 
                |      ...
                |      MyTransitionControl = MyFeatures.AddSubFeature("SimTransitionControl", MyLocalOptimizationArea)
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_transition_distance(self, o_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTransitionDistance(double oVal)
                |     Gets the Transition Distance.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Distance Value. Quantity: LENGTH, units:m

        :param float o_val:
        :return: None
        """
        return self.com_object.GetTransitionDistance(o_val)

    def set_transition_distance(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTransitionDistance(double iVal)
                |     Sets the Transition Distance.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Distance Value. Quantity: LENGTH, units:m 


        :param float i_val:
        :return: None
        """
        return self.com_object.SetTransitionDistance(i_val)

    def __repr__(self):
        return f'SimTransitionControl(name="{ self.name }")'
