"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class CtmCurveSamplerDistance(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CtmCurveSamplerDistance
                | 
                | Interface representing the curve sampler distance.
                | 
                | Role: This interface is used to get and set the distance paramter used by the
                | sampler, as well as the sag.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def distance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Distance() As double
                |     Returns or sets the distance parameter used by this sampler. This parameter
                |     controls how far apart to space the points on the curve. This will be the
                |     maximum distance between the positions. The sag parameter could override the
                |     distance and generate the positions closer together in areas of high
                |     curvature.
                | 
                |     Parameters:
                | 
                |         oDistance
                |             The distance parameter. 
                |         Example:
                | 
                |              Dim objDistSampler As CtmCurveSamplerDistance
                |                    ........
                |              Dim oDistance As Double
                |              objDistSampler.Distance = 5
                |              oDistance = objDistSampler.Distance

        :return: float
        """

        return self.com_object.Distance

    @distance.setter
    def distance(self, value: float):
        """
        :param float value:
        """

        self.com_object.Distance = value

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
                |     consecutive points and the curve. If the sag is less than the value of this
                |     parameter, then the spacing points will be controlled by the distance
                |     parameter.
                | 
                |     Parameters:
                | 
                |         oSag
                |             The sag parameter. 
                |         Example:
                | 
                |              Dim objDistSampler As CtmCurveSamplerDistance
                |                    ........
                |              Dim oSag As Double
                |              objDistSampler.Sag = 7
                |              oSag = objDistSampler.Sag

        :return: float
        """

        return self.com_object.Sag

    @sag.setter
    def sag(self, value: float):
        """
        :param float value:
        """

        self.com_object.Sag = value

    def __repr__(self):
        return f'CtmCurveSamplerDistance(name="{ self.name }")'
