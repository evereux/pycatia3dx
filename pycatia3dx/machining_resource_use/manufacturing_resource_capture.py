"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingResourceCapture(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingResourceCapture
                | 
                | Interface use to capture a screenshot to illustrate resource
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def save_capture(self, filepath: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SaveCapture(CATBSTR filepath)
                | 
                |     Save Capture:
                | 
                |     Parameters:
                | 
                |         filepath
                |             file path where capture is saved 
                | 
                |     Returns:
                | 
                |         S_OK
                |         E_FAIL
                | 
                |     Deprecated:
                |         R424 Use ManufacturingResourceCapture::SaveScreenshot with is3DPrefered
                |         parameter

        :param str filepath:
        :return: None
        """
        return self.com_object.SaveCapture(filepath)

    def save_screenshot(self, filepath: str, is3_d_prefered: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SaveScreenshot(CATBSTR filepath,boolean is3DPrefered)
                | 
                |     Save Capture:
                | 
                |     Parameters:
                | 
                |         filepath
                |             file path where capture is saved 
                |         is3DPrefered
                |             Capture in 3D if available else capture in 2D if available
                |             
                | 
                |     Returns:
                | 
                |         S_OK
                |         E_FAIL

        :param str filepath:
        :param bool is3_d_prefered:
        :return: None
        """
        return self.com_object.SaveScreenshot(filepath, is3_d_prefered)

    def __repr__(self):
        return f'ManufacturingResourceCapture(name="{ self.name }")'
