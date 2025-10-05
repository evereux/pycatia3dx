"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class CtmContourFromSurfaces(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CtmContourFromSurfaces
                | 
                | Interface representing a Contour created from surface
                | intersection
                | Role: This interface is used to get and set the Intersection result and surface
                | extrapolation distance for a contour generated from surface
                | intersection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def intersection_result(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IntersectionResult() As short
                |     Returns or sets the index from the intersection result which defines which
                |     curve from the result is used for this contour. The default value is 1 which
                |     uses the first curve from the intersection.
                | 
                |     Parameters:
                | 
                |         oIntersectionResultIndex
                |             The index of the curve in the intersection result.

        :return: int
        """

        return self.com_object.IntersectionResult

    @intersection_result.setter
    def intersection_result(self, value: int):
        """
        :param int value:
        """

        self.com_object.IntersectionResult = value

    @property
    def surface_extrapolation_distance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SurfaceExtrapolationDistance() As double
                |     Returns or sets the distance to extrapolate the surfaces when performing
                |     the intersection. If the surfaces do not intersect at all, the surfaces will be
                |     automatically extrapolated until an intersection is found if possible. in some
                |     cases, you may want to specify this value to obtain a cleaner curve (for
                |     example to get only 1 result instead of multiple results with gaps inbetween
                |     them.
                | 
                |     Parameters:
                | 
                |         oDistanceToExtrapolate
                |             The distance to extrapolate the surfaces. 

        :return: float
        """

        return self.com_object.SurfaceExtrapolationDistance

    @surface_extrapolation_distance.setter
    def surface_extrapolation_distance(self, value: float):
        """
        :param float value:
        """

        self.com_object.SurfaceExtrapolationDistance = value

    def __repr__(self):
        return f'CtmContourFromSurfaces(name="{ self.name }")'
