"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.plane import Plane
from pycatia3dx.mode.reference import Reference


class HybridShapePlaneMean(Plane):

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
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneMean
                | 
                | Represents the hybrid shape mean plane feature object.
                | Role: To access the data of the hybrid shape mean plane feature object. This
                | data includes:
                | 
                |     The list of points
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapePlaneMean
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_mean = com_object

    def add_point(self, i_passing_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddPoint(Reference iPassingPoint)
                |     Adds a point to the mean plane.
                | 
                |     Parameters:
                | 
                |         iPassingPoint
                |             The point to add
                | 
                |             Sub-element(s) supported (see Boundary object): Vertex.

        :param Reference i_passing_point:
        :return: None
        """
        return self.hybrid_shape_plane_mean.AddPoint(i_passing_point.com_object)

    def get_point(self, i_rank: int, o_passing_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetPoint(long iRank,Reference oPassingPoint)
                |     Retrieves the point at a given position.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the point to retrieve 
                |         oPassingPoint
                |             The point retrieved at this rank

        :param int i_rank:
        :param Reference o_passing_point:
        :return: None
        """
        return self.hybrid_shape_plane_mean.GetPoint(i_rank, o_passing_point.com_object)

    def get_pos(self, i_point: Reference) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPos(Reference iPoint) As long
                |     Gets the position of an element in the list.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             point 
                |         oPos
                |             position of point

        :param Reference i_point:
        :return: int
        """
        return self.hybrid_shape_plane_mean.GetPos(i_point.com_object)

    def get_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetSize() As long
                |     Gets the size of the list (number of points).
                | 
                |     Parameters:
                | 
                |         oSize
                |             position of point

        :return: int
        """
        return self.hybrid_shape_plane_mean.GetSize()

    def remove_all(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAll()
                |     Removes all elements in the list of points.

        :return: None
        """
        return self.hybrid_shape_plane_mean.RemoveAll()

    def remove_element(self, i_rank: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveElement(long iRank)
                |     Removes a point in the list.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the point to remove

        :param int i_rank:
        :return: None
        """
        return self.hybrid_shape_plane_mean.RemoveElement(i_rank)

    def replace_point_at_position(self, i_point: Reference, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub ReplacePointAtPosition(Reference iPoint,long iPos)
                |     Replaces a point in the list at the given position.
                | 
                |     Parameters:
                | 
                |         oPoint
                |             point 
                |         iPos
                |             position of point

        :param Reference i_point:
        :param int i_pos:
        :return: None
        """
        return self.hybrid_shape_plane_mean.ReplacePointAtPosition(i_point.com_object, i_pos)

    def __repr__(self):
        return f'HybridShapePlaneMean(name="{ self.name }")'
