"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.part.prism import Prism


class Pocket(Prism):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         CATPartIDLItf.SketchBasedShape
                |                             CATPartIDLItf.Prism
                |                                 Pocket
                | 
                | Represents the pocket shape.
                | A pocket is created by extruding a profile represented by a sketch in one or
                | two opposite directions. It is a "negative" shape: it removes material from the
                | body it belongs to. The sketch is usually drawn on another shape
                | face.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'Pocket(name="{ self.name }")'
