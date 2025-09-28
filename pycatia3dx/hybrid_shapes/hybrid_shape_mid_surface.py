"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeMidSurface(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapeMidSurface
                | 
                | Represents the hybrid shape MidSurface feature object.
                | Role: To access the data of the hybrid shape MidSurface feature
                | object.
                | This data includes:
                | 
                |     Support Body
                |     Creation Mode
                |     Threshold Thickness
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeMidSurface
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def auto_thickness_threshold(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AutoThicknessThreshold() As long
                |     Returns or sets AutoThicknessThreshold. Automatic Thickmess Threshold Check Button ON :1, OFF : 0 (Only Automatic Creation Mode Available for Automation)

        :return: int
        """

        return self.com_object.AutoThicknessThreshold

    @auto_thickness_threshold.setter
    def auto_thickness_threshold(self, value: int):
        """
        :param int value:
        """

        self.com_object.AutoThicknessThreshold = value

    @property
    def creation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CreationMode() As long
                |     Returns or sets CreationMode. Face Pairs : 0, Faces To Offset : 1, Automatic : 2 (Only Automatic Creation Mode Available for Automation)

        :return: int
        """

        return self.com_object.CreationMode

    @creation_mode.setter
    def creation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.CreationMode = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or sets Support Body. Reference.

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    @property
    def threshold(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Threshold() As Length
                |     Returns or sets Threshold Thickness. Length.

        :return: Length
        """

        return Length(self.com_object.Threshold)

    @threshold.setter
    def threshold(self, value: Length):
        """
        :param Length value:
        """

        self.com_object.Threshold = value

    def __repr__(self):
        return f'HybridShapeMidSurface(name="{ self.name }")'
