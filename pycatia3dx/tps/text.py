"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.annotation.drawing_text import DrawingText
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.tps_parallel_on_screen import TPSParallelOnScreen


class Text(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Text
                | 
                | Interface for the TPS Text object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def text(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Text() As CATBSTR
                |     Gets the annotation's text.

        :return: str
        """

        return self.com_object.Text

    @text.setter
    def text(self, value: str):
        """
        :param str value:
        """

        self.com_object.Text = value

    def get2d_annot(self) -> DrawingText:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Get2dAnnot() As DrawingText
                |     Retrieves Drafting text.

        :return: DrawingText
        """
        return DrawingText(self.com_object.Get2dAnnot())

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
        return f'Text(name="{ self.name }")'
