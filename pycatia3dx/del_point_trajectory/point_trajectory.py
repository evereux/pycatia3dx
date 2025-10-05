"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class PointTrajectory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PointTrajectory
                | 
                | Interface representing a PointTrajectory.
                | 
                | Role: This interface is used to get and set attributes specific to a Point
                | Trajectory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CATBSTR (Read Only)
                |     This property returns the type of the Point Trajectory
                | 
                |     Returns:
                |         oType The type of the Point Trajectory. 
                |     Example:
                | 
                |            
                | 
                |            Dim objTrajectory As PointTrajectory
                |                   ......
                |         Dim oType
                |         oType = objTrajectory.Type

        :return: str
        """

        return self.com_object.Type

    def add_point(self, i_fastener_occurrence: AnyObject, i_index: int, o_tag: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddPoint(AnyObject iFastenerOccurrence,short iIndex,AnyObject
                | oTag)
                |     Creates a new Tag in the Point Trajectory. If no context is specified, this
                |     will return the Tag's location wrt the global context
                | 
                |     Parameters:
                | 
                |         iFastenerOccurrence
                |             Occurrence of the Fastener to which this tag has to be linked. If
                |             there is no fastener occurrence, set it to NULL. 
                |         iIndex
                |             Index at which the tag is created. Set it to -1 to create tag at
                |             the end 
                |         oTag
                |             Created Tag. 
                | 
                |     Example:
                | 
                |            
                | 
                |             Dim objPointrajectory As PointTrajectory
                |             Dim objTag As Tag
                |             Dim objFastenerOcc As AnyObject
                |                   ......
                |             Call objPointrajectory.AddPoint(objFastenerOcc, -1,
                |             objTag)

        :param AnyObject i_fastener_occurrence:
        :param int i_index:
        :param AnyObject o_tag:
        :return: None
        """
        return self.com_object.AddPoint(i_fastener_occurrence.com_object, i_index, o_tag.com_object)

    def remove_point(self, i_tag: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemovePoint(AnyObject iTag)
                |     Deletes a Tag.
                | 
                |     Parameters:
                | 
                |         iTag
                |             The Tag to delete 
                | 
                |     Example:
                | 
                |            
                | 
                |             Dim objPointrajectory As PointTrajectory
                |             Dim objTag As Tag
                |                   ......
                |             Call objPointrajectory.RemovePoint(objTag)

        :param AnyObject i_tag:
        :return: None
        """
        return self.com_object.RemovePoint(i_tag.com_object)

    def __repr__(self):
        return f'PointTrajectory(name="{ self.name }")'
