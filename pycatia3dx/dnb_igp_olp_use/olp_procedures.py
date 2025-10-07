"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.dnb_igp_olp_use.olp_procedure import OLPProcedure
from pycatia3dx.types.general import CATVariant


class OLPProcedures(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OlpProcedures
                | 
                | A list of procedures.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_robot_task(self) -> OLPProcedure:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRobotTask() As OlpProcedure
                | 
                |     Deprecated:
                |         R425 CreateRobotTaskWithMotionGroups

        :return: OLPProcedure
        """
        return OLPProcedure(self.com_object.CreateRobotTask())

    def create_robot_task_with_motion_groups(self, i_motion_groups: tuple) -> OLPProcedure:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRobotTaskWithMotionGroups(CATSafeArrayVariant iMotionGroups) As
                | OlpProcedure
                |     Create a new robot task.
                |     This creates a procedure that can contain robot motions and is exposed as a
                |     service. The name is automatically generated but can be set using
                |     OlpProcedure.Name
                | 
                |     Parameters:
                | 
                |         iMotionGroups
                |             The motion group(s) controlled by the task. 
                | 
                |     Returns:
                |         The new procedure.

        :param tuple i_motion_groups:
        :return: OLPProcedure
        """
        return OLPProcedure(self.com_object.CreateRobotTaskWithMotionGroups(i_motion_groups))

    def item(self, i_index: CATVariant) -> OLPProcedure:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As OlpProcedure
                |     Retrieve a procedure by its name or index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             If this is a number then it is the index of the procedure in the
                |             collection. The index of the first procedure in the collection is 1, and the
                |             index of the last procedure is Count. If this is a string then it is the name
                |             of the procedure. 
                | 
                |     Returns:
                |         The procedure retrieved. If the procedure with the given name does not
                |         exist, Nothing is returned but the function succeeds. If the index is out of
                |         bounds, the function fails. 

        :param CATVariant i_index:
        :return: OLPProcedure
        """
        return OLPProcedure(self.com_object.Item(i_index))

    def __repr__(self):
        return f'OLPProcedures(name="{ self.name }")'
