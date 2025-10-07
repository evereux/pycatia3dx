"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.reference import Reference
from pycatia3dx.todo_part.boolean_shape import BooleanShape


class Trim(BooleanShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         CATPartIDLItf.BooleanShape
                |                             Trim
                | 
                | Represents the Trim, or union trim boolean operation.
                | It is performed between a body and the current shape.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_face_to_keep(self, i_face_to_keep: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddFaceToKeep(Reference iFaceToKeep)
                |     Adds a new face to be kept (if face is not divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToKeep
                |             The new face to process
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example adds the new face face to Keep for the Trim
                |         firstTrim:
                | 
                |          call firstTrim.AddFaceToKeep(face)

        :param Reference i_face_to_keep:
        :return: None
        """
        return self.com_object.AddFaceToKeep(i_face_to_keep.com_object)

    def add_face_to_keep2(self, i_face_to_keep: Reference, i_face_adjacent_for_keep: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddFaceToKeep2(Reference iFaceToKeep,Reference
                | iFaceAdjacentForKeep)
                |     Adds a new face to be kept (if face is divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToKeep
                |             The new face to process
                |             The following Boundary object is supported: Face. 
                |         iFaceAdjacentForKeep
                |             An adjacent face of iFaceToKeep belonging to the other
                |             operand
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example adds the new face face to Keep for the Trim
                |         firstTrim:
                | 
                |          call firstTrim.AddFaceToKeep(face)

        :param Reference i_face_to_keep:
        :param Reference i_face_adjacent_for_keep:
        :return: None
        """
        return self.com_object.AddFaceToKeep2(i_face_to_keep.com_object, i_face_adjacent_for_keep.com_object)

    def add_face_to_remove(self, i_face_to_remove: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddFaceToRemove(Reference iFaceToRemove)
                |     Adds a new face to be Removed (if face not divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToRemove
                |             The new face to process
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example adds the new face face to Remove for the Trim
                |         firstTrim:
                | 
                |          call firstTrim.AddFaceToRemove(face)

        :param Reference i_face_to_remove:
        :return: None
        """
        return self.com_object.AddFaceToRemove(i_face_to_remove.com_object)

    def add_face_to_remove2(self, i_face_to_remove: Reference, i_face_adjacent_for_remove: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddFaceToRemove2(Reference iFaceToRemove,Reference
                | iFaceAdjacentForRemove)
                |     Adds a new face to be Removed (if face is divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToRemove
                |             The new face to process
                |             The following Boundary object is supported: Face. 
                |         iFaceAdjacentForRemove
                |             An adjacent face of iFaceToRemove belonging to the other
                |             operand
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example adds the new face face to Remove for the Trim
                |         firstTrim:
                | 
                |          call firstTrim.AddFaceToRemove(face)

        :param Reference i_face_to_remove:
        :param Reference i_face_adjacent_for_remove:
        :return: None
        """
        return self.com_object.AddFaceToRemove2(i_face_to_remove.com_object, i_face_adjacent_for_remove.com_object)

    def withdraw_face_to_keep(self, i_face_to_withdraw: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub WithdrawFaceToKeep(Reference iFaceToWithdraw)
                |     Withdraws an existing Kept face (if face is not divided by operation)
                |     .
                | 
                |     Parameters:
                | 
                |         iFaceToWithdraw
                |             The face to withdraw
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example withdraws the existing face Kept face from the
                |         Trim firstTrim:
                | 
                |          call firstTrim.WithdrawFaceToKeep(face)

        :param Reference i_face_to_withdraw:
        :return: None
        """
        return self.com_object.WithdrawFaceToKeep(i_face_to_withdraw.com_object)

    def withdraw_face_to_keep2(self, i_face_to_withdraw: Reference, i_face_adjacent_for_keep: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub WithdrawFaceToKeep2(Reference iFaceToWithdraw,Reference
                | iFaceAdjacentForKeep)
                |     Withdraws an existing Kept face (if face is divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToWithdraw
                |             The face to withdraw
                |             The following Boundary object is supported: Face. 
                |         iFaceAdjacentForKeep
                |             An adjacent face of iFaceToKeep belonging to the other
                |             operand
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example withdraws the existing face Kept face from the
                |         Trim firstTrim:
                | 
                |          call firstTrim.WithdrawFaceToKeep(face)

        :param Reference i_face_to_withdraw:
        :param Reference i_face_adjacent_for_keep:
        :return: None
        """
        return self.com_object.WithdrawFaceToKeep2(i_face_to_withdraw.com_object, i_face_adjacent_for_keep.com_object)

    def withdraw_face_to_remove(self, i_face_to_withdraw: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub WithdrawFaceToRemove(Reference iFaceToWithdraw)
                |     Withdraws an existing Removed face (if face not divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToWithdraw
                |             The face to withdraw
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example withdraws the existing face Removed face from the
                |         Trim firstTrim:
                | 
                |          call firstTrim.WithdrawFaceToRemove(face)

        :param Reference i_face_to_withdraw:
        :return: None
        """
        return self.com_object.WithdrawFaceToRemove(i_face_to_withdraw.com_object)

    def withdraw_face_to_remove2(self, i_face_to_withdraw: Reference, i_face_adjacent_for_remove: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub WithdrawFaceToRemove2(Reference iFaceToWithdraw,Reference
                | iFaceAdjacentForRemove)
                |     Withdraws an existing Removed face (if face is divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToWithdraw
                |             The face to withdraw
                |             The following Boundary object is supported: Face. 
                |         iFaceAdjacentForRemove
                |             An adjacent face of iFaceToRemove belonging to the other
                |             operand
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example withdraws the existing face Removed face from the
                |         Trim firstTrim:
                | 
                |          call firstTrim.WithdrawFaceToRemove(face)

        :param Reference i_face_to_withdraw:
        :param Reference i_face_adjacent_for_remove:
        :return: None
        """
        return self.com_object.WithdrawFaceToRemove2(i_face_to_withdraw.com_object, i_face_adjacent_for_remove.com_object)

    def __repr__(self):
        return f'Trim(name="{ self.name }")'
