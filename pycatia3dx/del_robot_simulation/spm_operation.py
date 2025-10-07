"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SpmOperation(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SPMOperation
                | 
                | Interface representing an SPMOperation.
                | 
                | Role: This interface is used to work with SPMOperations
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def export_process_points(self, file_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ExportProcessPoints(CATBSTR filePath)
                |     Export Process Points of Motion activities under this SPMOperation to an
                |     external file.
                | 
                |     Parameters:
                | 
                |         filePath
                |             Path of file to which Process points' data will be exported.
                |             
                | 
                |     Example:
                | 
                |           Dim objSPMOp As SPMOperation
                |                   ......
                |         Dim filePath as String
                |           filePath = "D:\\user1\\SPMOperation\\ExportProcessPoints.xls"
                |         Call objSPMOp.ExportProcessPoints(filePath)

        :param str file_path:
        :return: None
        """
        return self.com_object.ExportProcessPoints(file_path)

    def get_all_motion_activities(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAllMotionActivities() As CATSafeArrayVariant
                |     Retrieves all the Motion activities under this
                |     SPMOperation.
                | 
                |     Parameters:
                | 
                |         olMotionActivities
                |             List of all the motion activities created. 
                | 
                |     Example:
                | 
                |            
                | 
                |           Dim objSPMOp As SPMOperation
                |                   ......
                |         Dim oMotionActList(10)
                |         Call objSPMOp.GetAllMotionActivities(oMotionActList)

        :return: tuple
        """
        return self.com_object.GetAllMotionActivities()

    def import_process_points(self, file_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ImportProcessPoints(CATBSTR filePath)
                |     Import Process Points from an external file to Motion activities under this
                |     SPMOperation.
                | 
                |     Parameters:
                | 
                |         filePath
                |             Path of file containing the Process points' data 
                | 
                |     Example:
                | 
                |            
                | 
                |           Dim objSPMOp As SPMOperation
                |                   ......
                |         Dim filePath as String
                |           filePath = "D:\\user1\\SPMOperation\\ImportProcessPoints.xls"
                |         Call objSPMOp.ImportProcessPoints(filePath)

        :param str file_path:
        :return: None
        """
        return self.com_object.ImportProcessPoints(file_path)

    def __repr__(self):
        return f'SpmOperation(name="{ self.name }")'
