"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class VSODocument(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VSODocument
                | 
                | Interface representing a RSO Document feature.
                | 
                | Role: Components that implement CATIAVSODocument are Virtual to Real Shape
                | Morphind documents linked to an external element (SIMULIA result, VPM Document,
                | ...) This interface allows to synchronize the document with its
                | reference.
                | 
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def synchronize(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Synchronize()

        :return: None
        """
        return self.com_object.Synchronize()

    def __repr__(self):
        return f'VsoDocument(name="{self.name}")'
