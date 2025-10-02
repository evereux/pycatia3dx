"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimDesignImprovementObjective(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimDesignImprovementObjective
                | 
                | Represents the Design Improvement Objective.
                | Base class for Design Improvement Objective.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimDesignImprovementObjective named "Objective.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyObjective As SimDesignImprovementObjective
                |      Set MyObjective = MyFeatures.Item("Objective.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures collection, you can retrieve a
                |     SimDesignImprovementObjective object as following:
                | 
                |      ...
                |      MyObjective  = MyFeatures.Item("Objective.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'SimDesignImprovementObjective(name="{ self.name }")'
