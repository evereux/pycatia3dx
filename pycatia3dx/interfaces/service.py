"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class Service(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Service
                | 
                | Represents a service.
                | A service is a set of object-independent operations that globally apply to the
                | objects controlled by the active editor and aggregated to the root object. A
                | service can apply to the session level if the operations apply to any PLM type
                | root object, or to the editor level if it applies only to a dedicated PLM type
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'Service(name="{self.name}")'
