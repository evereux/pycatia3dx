"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class CtmCurveSampler(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CtmCurveSampler
                | 
                | Interface representing the curve sampler.
                | 
                | Role: This interface is used to get and set start and end offsets for Curve
                | trajectory.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def end_offset(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EndOffset() As double
                |     Returns or sets the end offset for the curve. The offset indicates the
                |     distance from the end of the curve at which sampling will end, and a tag will
                |     be placed at the end. 
                | Example:
                | 
                |      Dim objSampler As CtmCurveSampler
                |            ........
                |      Dim oEndOffset As Double
                |      objSampler.EndOffset = 12
                |      oEndOffset = objSampler.EndOffset

        :return: float
        """

        return self.com_object.EndOffset

    @end_offset.setter
    def end_offset(self, value: float):
        """
        :param float value:
        """

        self.com_object.EndOffset = value

    @property
    def start_offset(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartOffset() As double
                |     Returns or sets the start offset for the curve. The offset indicates the
                |     distance along the curve at which sampling will start, after a tag has been
                |     placed at the start of the curve. 
                | Example:
                | 
                |      Dim objSampler As CtmCurveSampler
                |            ........
                |      Dim oStartOffset As Double
                |      objSampler.StartOffset = 10
                |      oStartOffset = objSampler.StartOffset 

        :return: float
        """

        return self.com_object.StartOffset

    @start_offset.setter
    def start_offset(self, value: float):
        """
        :param float value:
        """

        self.com_object.StartOffset = value

    def __repr__(self):
        return f'CtmCurveSampler(name="{ self.name }")'
