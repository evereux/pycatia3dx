"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.annotation import Annotation
from pycatia3dx.tps.annotation_2 import Annotation2


class AssociatedRefFrame(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AssociatedRefFrame
                | 
                | Interface dedicated to manage Datum Reference Frame associated to a
                | TPS.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def reference_frame(self) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceFrame() As Annotation (Read Only)
                |     Retrieves the Datum Reference Frame associated to a TPS. Deprecated method:
                |     ReferenceFrame method is replaced by ReferenceFrame2 has.

        :return: Annotation
        """

        return Annotation(self.com_object.ReferenceFrame)

    @property
    def reference_frame2(self) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceFrame2() As Annotation2 (Read Only)
                |     Retrieves the Datum Reference Frame associated to a TPS. 

        :return: Annotation2
        """

        return Annotation2(self.com_object.ReferenceFrame2)

    def __repr__(self):
        return f'AssociatedRefFrame(name="{ self.name }")'
