"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.del_point_trajectory.point_trajectory import PointTrajectory


class PointTrajectoryFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PointTrajectoryFactory
                | 
                | Interface representing a Point Trajectory Factory to create and delete Point
                | Trajectory.
                | 
                | Role: This interface is used to create and delete Point
                | Trajectory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_point_trajectory(self, i_trajectory_type: str, i_name: str) -> PointTrajectory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreatePointTrajectory(CATBSTR iTrajectoryType,CATBSTR iName) As
                | PointTrajectory
                |     Creates a Point Trajectory.
                | 
                |     Returns:
                |         oPointTrajectory The created Point Trajectory. 
                |     Parameters:
                | 
                |         iTrajectoryType
                |             Type of Point Trajectory to create (Could be "Weld", "Rivet").
                |             
                |         iName
                |             Name of the Point trajectory to Create. 
                | 
                |     Example:
                | 
                |            
                | 
                |             Dim objPointTrajectoryFactory As
                |             PointTrajectoryFactory
                |                   ......
                |             Dim TrajectoryName As String
                |             TrajectoryName = "SpotTrajectory.VB"
                |             Dim objPointTrajectory As PointTrajectory
                |             Set objPointTrajectory = objPointTrajectoryFactory.CreatePointTrajectory("Weld", TrajectoryName)

        :param str i_trajectory_type:
        :param str i_name:
        :return: PointTrajectory
        """
        return PointTrajectory(self.com_object.CreatePointTrajectory(i_trajectory_type, i_name))

    def destroy_point_trajectory(self, i_point_trajectory: PointTrajectory) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DestroyPointTrajectory(PointTrajectory iPointTrajectory)
                |     Deletes a Point Trajectory.
                | 
                |     Parameters:
                | 
                |         iPointTrajectory
                |             The Point Trajectory to delete 
                | 
                |     Example:
                | 
                |            
                | 
                |             Dim objPointTrajectoryFactory As
                |             PointTrajectoryFactory
                |             Dim objPointTrajectory As PointTrajectory
                |                   ......
                |             Call objPointTrajectoryFactory.DestroyPointTrajectory(objPointTrajectory)

        :param PointTrajectory i_point_trajectory:
        :return: None
        """
        return self.com_object.DestroyPointTrajectory(i_point_trajectory.com_object)

    def __repr__(self):
        return f'PointTrajectoryFactory(name="{ self.name }")'
