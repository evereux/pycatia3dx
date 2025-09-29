"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DPCOperation(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DPCOperation
                | 
                | Represents a user operation.
                | Role: A User Operation is a set of tasks performed on a technological object.
                | It can be V6 command, CAA command, VBA command, external application or
                | operation defined into the DPC product. An operation contains a set of
                | variables: the inputs entered by the user and the outputs produced by the
                | operation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'DpcOperation(name="{self.name}")'
