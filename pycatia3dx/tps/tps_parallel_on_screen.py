"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class TPSParallelOnScreen(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TPSParallelOnScreen
                | 
                | Interface for Parallel On Screen.
                | TPS for Technological Product Specifications.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def parallel_on_screen(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ParallelOnScreen() As boolean
                |     Retrieves the Parallel On Screen for the annotation.

        :return: bool
        """

        return self.com_object.ParallelOnScreen

    @parallel_on_screen.setter
    def parallel_on_screen(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ParallelOnScreen = value

    @property
    def zoomable(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Zoomable() As boolean
                |     Retrieves the Zoomable for the annotation. 

        :return: bool
        """

        return self.com_object.Zoomable

    @zoomable.setter
    def zoomable(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Zoomable = value

    def __repr__(self):
        return f'TpsParallelOnScreen(name="{ self.name }")'
