"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.annotation.drawing_welding import DrawingWelding
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.tps_parallel_on_screen import TPSParallelOnScreen


class Weld(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Weld

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get2d_annot(self) -> DrawingWelding:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Get2dAnnot() As DrawingWelding
                |     Retrieves Drafting Weld annotation.

        :return: DrawingWelding
        """
        return DrawingWelding(self.com_object.Get2dAnnot())

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func TPSParallelOnScreen() As TPSParallelOnScreen
                |     Gets the annotation on TPSParallelOnScreen interface. 

        :return: TPSParallelOnScreen
        """
        return TPSParallelOnScreen(self.com_object.TPSParallelOnScreen())

    def __repr__(self):
        return f'Weld(name="{ self.name }")'
