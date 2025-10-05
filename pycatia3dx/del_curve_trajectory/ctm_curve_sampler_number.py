"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class CtmCurveSamplerNumber(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CtmCurveSamplerNumber
                | 
                | Interface representing the curve sampler number.
                | 
                | Role: This interface is used to get and set number of samples.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def number_of_samples(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfSamples() As short
                |     Returns or sets the number of samples parameter used by this sampler. This
                |     parameter controls how many samples are created along the curve. All samples
                |     will be an equal distance apart.
                | 
                |     Parameters:
                | 
                |         oNumSamples
                |             The number of samples. 
                |         Example:
                | 
                |              Dim objNumberSampler As CtmCurveSamplerNumber
                |                    ........
                |              Dim oNumberOfSamples
                |              objNumberSampler.NumberOfSamples = 4
                |              oNumberOfSamples = objNumberSampler.NumberOfSamples 

        :return: int
        """

        return self.com_object.NumberOfSamples

    @number_of_samples.setter
    def number_of_samples(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfSamples = value

    def __repr__(self):
        return f'CtmCurveSamplerNumber(name="{ self.name }")'
