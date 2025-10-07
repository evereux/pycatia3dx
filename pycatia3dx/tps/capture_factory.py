"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.factory import Factory
from pycatia3dx.tps.capture import Capture


class CaptureFactory(Factory):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Factory
                |                         CaptureFactory
                | 
                | Interface for the Capture Factory.
                | This factory is implemented on the Set object. All the created Captures are
                | added to the Set from which this interface is retrieved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_capture(self) -> Capture:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateCapture() As Capture
                |     Create a Capture.
                | 
                |     Parameters:
                | 
                |         oCapture
                |             The new created Capture. 

        :return: Capture
        """
        return Capture(self.com_object.CreateCapture())

    def __repr__(self):
        return f'CaptureFactory(name="{ self.name }")'
