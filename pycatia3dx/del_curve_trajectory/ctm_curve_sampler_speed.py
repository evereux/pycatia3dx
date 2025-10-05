"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class CtmCurveSamplerSpeed(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CtmCurveSamplerSpeed

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def sag(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Sag() As double
                |     Returns or sets the sag parameter used by this sampler. This parameter
                |     controls how closely to space the points in regions of high curvature. The sag
                |     distance is the maximum distance between the chord passing through two
                |     consecutive points and the curve. If the sag is less the value of this
                |     parameter, then the spacing points will be controlled by the distance
                |     parameter.
                | 
                |     Parameters:
                | 
                |         oSag
                |             The sag parameter. 
                |         Example:
                | 
                |              Dim objSpeedSampler As CtmCurveSamplerSpeed
                |                    ........
                |              Dim oSag As Double
                |              objSpeedSampler.Sag = 12.4
                |              oSag = objSpeedSampler.Sag

        :return: float
        """

        return self.com_object.Sag

    @sag.setter
    def sag(self, value: float):
        """
        :param float value:
        """

        self.com_object.Sag = value

    @property
    def speed(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Speed() As double
                |     Returns or sets the speed parameter used by this sampler. The sag parameter
                |     could override the speed and generate the positions closer together in areas of
                |     high curvature.
                | 
                |     Parameters:
                | 
                |         oSpeed
                |             The speed parameter, in m/s 
                |         Example:
                | 
                |              Dim objSpeedSampler As CtmCurveSamplerSpeed
                |                    ........
                |              Dim oSpeed As Double
                |              objSpeedSampler.Speed = 5.5
                |              oSpeed = objSpeedSampler.Speed

        :return: float
        """

        return self.com_object.Speed

    @speed.setter
    def speed(self, value: float):
        """
        :param float value:
        """

        self.com_object.Speed = value

    def __repr__(self):
        return f'CtmCurveSamplerSpeed(name="{ self.name }")'
