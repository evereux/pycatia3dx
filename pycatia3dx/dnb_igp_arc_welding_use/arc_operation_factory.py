"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.cat_base_unknown import CATBaseUnknown


class ArcOperationFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArcOperationFactory

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_arc_operation(self, i_mode: int, i_reference_instruction: CATBaseUnknown, i_parent_seq: CATBaseUnknown, i_motion_group: CATBaseUnknown) -> CATBaseUnknown:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateArcOperation(InsertMode iMode,CATBaseUnknown
                | iReferenceInstruction,CATBaseUnknown iParentSeq,CATBaseUnknown iMotionGroup) As
                | CATBaseUnknown

        :param int i_mode:
        :param CATBaseUnknown i_reference_instruction:
        :param CATBaseUnknown i_parent_seq:
        :param CATBaseUnknown i_motion_group:
        :return: CATBaseUnknown
        """
        return CATBaseUnknown(self.com_object.CreateArcOperation(i_mode, i_reference_instruction.com_object, i_parent_seq.com_object, i_motion_group.com_object))

    def delete_arc_operation(self, isp_motion_activity: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteArcOperation(CATBaseUnknown ispMotionActivity)

        :param CATBaseUnknown isp_motion_activity:
        :return: None
        """
        return self.com_object.DeleteArcOperation(isp_motion_activity.com_object)

    def __repr__(self):
        return f'ArcOperationFactory(name="{ self.name }")'
