"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SurfaceTrajectoryFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SurfaceTrajectoryFactory
                | 
                | Interface representing a Surface Trajectory Factory to create, destroy, and
                | retrieve Surface Trajectories.
                | 
                | Role: This interface is used to create, destroy, and retrieve Surface
                | Trajectories..
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_surface_trajectory(self, i_trajectory_type: str, i_name: str, i_surf_list: tuple, i_prod_list: tuple) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSurfaceTrajectory(CATBSTR iTrajectoryType,CATBSTR
                | iName,CATSafeArrayVariant iSurfList,CATSafeArrayVariant iProdList) As
                | AnyObject
                |     This method creates a SurfaceTrajectory
                | 
                |     Parameters:
                | 
                |         iTrajectoryType
                |             Input the trajectory type. The type can be either Paint, Sealant,
                |             General. 
                |         iName,
                |             Name of the trajectory. The default value is "". This means the
                |             default trajectory name would be, "Trajectory".. If a name is provided then the
                |             trajectory name would be, ..
                |         iSurfList
                |             List of Surfaces to create trajectory. 
                |         iProdList
                |             List of Product Occurrences. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param str i_trajectory_type:
        :param str i_name:
        :param tuple i_surf_list:
        :param tuple i_prod_list:
        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateSurfaceTrajectory(i_trajectory_type, i_name, i_surf_list, i_prod_list))

    def destroy_surface_trajectory(self, osp_surface_traj: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DestroySurfaceTrajectory(AnyObject ospSurfaceTraj)
                |     This method destroys a SurfaceTrajectory
                | 
                |     Parameters:
                | 
                |         ospSurfaceTraj
                |             SurfaceTrajectory to be deleted. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The TagGroup is successfully deleted 
                |         E_FAIL
                |             The TagGroup was not deleted successfully

        :param AnyObject osp_surface_traj:
        :return: None
        """
        return self.com_object.DestroySurfaceTrajectory(osp_surface_traj.com_object)

    def get_all_surface_trajectories(self, i_search_children: bool, o_traj_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAllSurfaceTrajectories(boolean iSearchChildren,CATSafeArrayVariant
                | oTrajList)
                |     This method retrieves all Surface trajectories under the organizational
                |     resource.
                | 
                |     Parameters:
                | 
                |         iSearchChildren
                |             Search children for trajectories recursively 
                |         oTrajList
                |             List of Surface Trajectories. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The List of Trajectories is successfully returned
                |         E_FAIL
                |             The List of Trajectories could not be retrieved

        :param bool i_search_children:
        :param tuple o_traj_list:
        :return: None
        """
        return self.com_object.GetAllSurfaceTrajectories(i_search_children, o_traj_list)

    def __repr__(self):
        return f'SurfaceTrajectoryFactory(name="{ self.name }")'
