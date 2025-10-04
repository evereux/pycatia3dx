"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimDisplayGroup(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimDisplayGroup
                | 
                | Represents the display group.
                | Role:The already created disaply groups can be retrieved and set to the plots,
                | sensor etc.
                | Example:
                | 
                |  Given a SimResultsAnalysisCase object, you can retrieve the existing display
                |  group objects as following.
                |  
                | 
                |  Dim oResultsSet As SimResultsSet
                |  Set oResultsSet = oResultsAnalysisCase.GetSet("DisplayGroupSet")
                | 
                |  Dim oDisplayGroup As SimDisplayGroup
                |  Set oDisplayGroup = oResultsSet.Item(1)
                |  
                | 
                | See also:
                |     SimResultsAnalysisCase

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'SimDisplayGroup(name="{ self.name }")'
