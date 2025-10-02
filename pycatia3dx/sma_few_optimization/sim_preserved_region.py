"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimPreservedRegion(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimPreservedRegion
                | 
                | Represents the Frozen Region object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimPreservedRegion as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      Dim MyDesignSpace As SimDesignEnvelope
                |      
                | 
                |      Dim MyFrozenRegion As SimPreservedRegion
                |      Set MyFrozenRegion = MyFeatures.AddSubFeature("SimPreservedRegion", MyDesignSpace)
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimPreservedRegion as following:
                | 
                |      ...
                |      MyFrozenRegion = MyFeatures.AddSubFeature("SimPreservedRegion", MyDesignSpace)
                |      
                | 
                | See also:
                |     SMAIAFeaOptimizationFeatureSet SMAIAFeaDesignArea
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'SimPreservedRegion(name="{ self.name }")'
