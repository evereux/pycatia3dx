"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimUserCsys(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimUserCsys
                | 
                | Represents the class for User Csys used for setting the results axis
                | system.
                | Role:The class be used to set the various parameters to the user csys object.
                | Currenty this class can be used only to get the user csys from the analysis
                | case
                | Example:
                | 
                |  Dim oUserCsysSet As SimResultsSet
                |  Set oUserCsysSet = ResultsAnalysisCase.GetSet("UserCsysSet")
                |  Dim oUserCsys As CATBaseDispatch
                |  Set oUserCsys = oUserCsysSet.Item(1)

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'SimUserCsys(name="{ self.name }")'
