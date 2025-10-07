"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference
from pycatia3dx.mode.references import References
from pycatia3dx.part.dress_up_shape import DressUpShape


class Shell(DressUpShape):

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
                |                         CATPartIDLItf.DressUpShape
                |                             Shell
                | 
                | Represents the shell shape.
                | A shell shape is made up of a list of faces to process and two thickness
                | parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def external_thickness(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ExternalThickness() As Length (Read Only)
                |     Returns the shell external thickness.
                | 
                |     Example:
                |         The following example returns in extThick the external thickness of the
                |         shell firstShell:
                | 
                |          Set extThick = firstShell.ExternalThickness

        :return: Length
        """

        return Length(self.com_object.ExternalThickness)

    @property
    def faces_to_remove(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FacesToRemove() As References (Read Only)
                |     Returns the collection of faces to be removed by the shell
                |     process.
                | 
                |     Example:
                |         The following example returns in list the faces to be removed from the
                |         shell firstShell:
                | 
                |          Set list = firstShell.FacesToRemove

        :return: References
        """

        return References(self.com_object.FacesToRemove)

    @property
    def internal_thickness(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InternalThickness() As Length (Read Only)
                |     Returns the shell internal thickness.
                | 
                |     Example:
                |         The following example returns in intThick the internal thickness of the
                |         shell firstShell:
                | 
                |          Set intThick = firstShell.InternalThickness

        :return: Length
        """

        return Length(self.com_object.InternalThickness)

    def add_face_to_remove(self, i_face_to_remove: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddFaceToRemove(Reference iFaceToRemove)
                |     Adds a new face to those to be removed by the shell
                |     process.
                | 
                |     Parameters:
                | 
                |         iFaceToRemove
                |             The face to be removed
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example adds the new face face to be removed in the shell
                |         firstShell:
                | 
                |          call firstShell.AddFaceToRemove(face)

        :param Reference i_face_to_remove:
        :return: None
        """
        return self.com_object.AddFaceToRemove(i_face_to_remove.com_object)

    def add_face_with_different_thickness(self, i_face_to_thicken: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddFaceWithDifferentThickness(Reference iFaceToThicken)
                |     Adds a new face to be thicken with different offset
                |     values.
                | 
                |     Parameters:
                | 
                |         iFaceToThicken
                |             The face to be thicken with different offset
                |             values
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example adds the new face face to be thicken with
                |         different offset values in the shell firstShell:
                | 
                |          call firstShell.AddFaceWithDifferentThickness(face)

        :param Reference i_face_to_thicken:
        :return: None
        """
        return self.com_object.AddFaceWithDifferentThickness(i_face_to_thicken.com_object)

    def remove_face_with_different_thickness(self, i_face_to_remove: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveFaceWithDifferentThickness(Reference iFaceToRemove)
                |     Removes an existing face from those to be thicken with different offset
                |     values by the shell process.
                | 
                |     Parameters:
                | 
                |         iFaceToRemove
                |             The face to be removed from the shell
                |             specifications
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example removes the face face from the list of faces in
                |         the shell firstShell:
                | 
                |          call
                |          firstShell.RemoveFaceWithDifferentThickness(face)

        :param Reference i_face_to_remove:
        :return: None
        """
        return self.com_object.RemoveFaceWithDifferentThickness(i_face_to_remove.com_object)

    def set_volume_support(self, i_volume_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetVolumeSupport(Reference iVolumeSupport)
                |     Set the Support Volume of the faces to modify during Shell operation.

        :param Reference i_volume_support:
        :return: None
        """
        return self.com_object.SetVolumeSupport(i_volume_support.com_object)

    def withdraw_face_to_remove(self, i_face_to_withdraw: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub WithdrawFaceToRemove(Reference iFaceToWithdraw)
                |     Withdraws an existing face from those to be removed by the shell
                |     process.
                | 
                |     Parameters:
                | 
                |         iFaceToWithdraw
                |             The face to be withdrawn from the shell
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example removes the face from the list of faces in
                |         the shell firstShell:
                | 
                |          call firstShell.WithdrawFaceToRemove(face)

        :param Reference i_face_to_withdraw:
        :return: None
        """
        return self.com_object.WithdrawFaceToRemove(i_face_to_withdraw.com_object)

    def __repr__(self):
        return f'Shell(name="{ self.name }")'
