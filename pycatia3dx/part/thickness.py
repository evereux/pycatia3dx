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
from pycatia3dx.todo_part.dress_up_shape import DressUpShape


class Thickness(DressUpShape):

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
                |                             Thickness
                | 
                | Represents the thickness shape.
                | The thickness shape is made up of a collection of faces to process and an
                | offset parameter.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def faces_to_thicken(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FacesToThicken() As References (Read Only)
                |     Returns the collection of faces to be thickened.
                | 
                |     Example:
                |         The following example returns in list the list of faces of the
                |         thickness firstThickness:
                | 
                |          Set list = firstThickness.FacesToThicken

        :return: References
        """

        return References(self.com_object.FacesToThicken)

    @property
    def offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Offset() As Length (Read Only)
                |     Returns the thickness offset.
                | 
                |     Example:
                |         The following example returns in offset the offset of the thickness
                |         firstThickness:
                | 
                |          Set offset = firstThickness.Offset

        :return: Length
        """

        return Length(self.com_object.Offset)

    def add_face_to_thicken(self, i_face_to_thicken: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddFaceToThicken(Reference iFaceToThicken)
                |     Adds a new face to be thickened.
                | 
                |     Parameters:
                | 
                |         iFaceToThicken
                |             The new face to process
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example adds the new face face to thicken for the
                |         thickness firstThickness:
                | 
                |          call firstThickness.AddFaceToThicken(face)

        :param Reference i_face_to_thicken:
        :return: None
        """
        return self.com_object.AddFaceToThicken(i_face_to_thicken.com_object)

    def add_face_with_different_thickness(self, i_face_to_thicken: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddFaceWithDifferentThickness(Reference iFaceToThicken)
                |     Adds a new face to thicken with a different offset value.
                | 
                |     Parameters:
                | 
                |         iFaceToThicken
                |             The new face to process
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example adds the new face face to thicken with a
                |         different offset value for the thickness
                |         firstThickness:
                | 
                |          call
                |          firstThickness.AddFaceWithDifferentThickness(face)

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
                |     Removes an existing thickened face.
                | 
                |     Parameters:
                | 
                |         iFaceToRemove
                |             The face to remove
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example removes the existing face thickened face from the
                |         thickness firstThickness:
                | 
                |          call
firstThickness.RemoveFaceWithDifferentThickness(face)(face)

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
                |     Set support of Thickness feature.

        :param Reference i_volume_support:
        :return: None
        """
        return self.com_object.SetVolumeSupport(i_volume_support.com_object)

    def withdraw_face_to_thicken(self, i_face_to_withdraw: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub WithdrawFaceToThicken(Reference iFaceToWithdraw)
                |     Withdraws an existing thickened face.
                | 
                |     Parameters:
                | 
                |         iFaceToWithdraw
                |             The face to withdraw
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example withdraws the existing face thickened face from
                |         the thickness firstThickness:
                | 
                |          call firstThickness.WithdrawFaceToThicken(face)

        :param Reference i_face_to_withdraw:
        :return: None
        """
        return self.com_object.WithdrawFaceToThicken(i_face_to_withdraw.com_object)

    def __repr__(self):
        return f'Thickness(name="{ self.name }")'
