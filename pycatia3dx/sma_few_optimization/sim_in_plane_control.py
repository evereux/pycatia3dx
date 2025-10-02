"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimInPlaneControl(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimInPlaneControl
                | 
                | Represents the In Plane Control object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimInPlaneControl as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      Dim MyLocalOptimizationArea As SimLocalOptimizationArea
                |      ...
                |      Dim MyInPlaneControl As SimInPlaneControl
                |      Set MyInPlaneControl = MyFeatures.AddSubFeature("SimInPlaneControl", MyLocalOptimizationArea)
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimInPlaneControl as following:
                | 
                |      ...
                |      MyInPlaneControl = MyFeatures.AddSubFeature("SimInPlaneControl", MyLocalOptimizationArea)
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'SimInPlaneControl(name="{ self.name }")'
