"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimDesignImprovementDesignVariable(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimDesignImprovementDesignVariable
                | 
                | Represents the Design Improvement Design Variable.
                | Base class for Design Improvement Design Variable.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures collection, you can retrieve a
                |     SimDesignImprovementDesignVariable named "Design Space.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyDesignVariable As
                |      SimDesignImprovementDesignVariable
                |      Set MyDesignVariable = MyFeatures.Item("Design Space.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures collection, you can retrieve a
                |     SimDesignImprovementDesignVariable object as following:
                | 
                |      ...
                |      MyDesignVariable  = MyFeatures.Item("Design Space.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'SimDesignImprovementDesignVariable(name="{ self.name }")'
