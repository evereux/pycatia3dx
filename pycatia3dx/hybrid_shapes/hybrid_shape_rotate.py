"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeRotate(HybridShape):

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
                |                         HybridShapeRotate
                | 
                | Represents the hybrid shape rotate feature object.
                | Role: To access the data of the hybrid shape rotate feature object. This data
                | includes:
                | 
                |     The element to be rotated
                |     The rotation axis
                |     The angle and its value
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Angle() As Angle (Read Only)
                |     Returns the rotation angle.

        :return: Angle
        """

        return Angle(self.com_object.Angle)

    @property
    def angle_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AngleValue() As double
                |     Returns or sets the rotation angle value.
                | 
                |     Example: This example retrieves in AngleValue the angle value for the
                |     Rotate hybrid shape feature.
                | 
                |      Dim AngleValue As double
                |      Set AngleValue = Rotate.AngleValue

        :return: float
        """

        return self.com_object.AngleValue

    @angle_value.setter
    def angle_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.AngleValue = value

    @property
    def axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Axis() As Reference
                |     Returns or sets the rotation axis.
                |     Sub-element(s) supported (see Boundary object): Edge.
                | 
                |     Example: This example retrieves in RotationAxis the rotation axis for the
                |     Rotate hybrid shape feature.
                | 
                |      Dim RotationAxis As Reference
                |      Set RotationAxis = Rotate.Axis

        :return: Reference
        """

        return Reference(self.com_object.Axis)

    @axis.setter
    def axis(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Axis = value

    @property
    def elem_to_rotate(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ElemToRotate() As Reference
                |     Returns or sets the element to be rotated.
                | 
                |     Example: This example retrieves in Elem the element to be rotated for the
                |     Rotate hybrid shape feature.
                | 
                |      Dim Elem As Reference
                |      Set Elem = Rotate.ElemToRotate

        :return: Reference
        """

        return Reference(self.com_object.ElemToRotate)

    @elem_to_rotate.setter
    def elem_to_rotate(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ElemToRotate = value

    @property
    def first_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstElement() As Reference
                |     Returns or sets the first element defining the rotation angle.

        :return: Reference
        """

        return Reference(self.com_object.FirstElement)

    @first_element.setter
    def first_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstElement = value

    @property
    def first_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstPoint() As Reference
                |     Returns or sets the first point defining the rotation.

        :return: Reference
        """

        return Reference(self.com_object.FirstPoint)

    @first_point.setter
    def first_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstPoint = value

    @property
    def orientation_of_first_element(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property OrientationOfFirstElement() As boolean
                |     Returns or sets the orientation of the first element defining the rotation
                |     angle.
                |     This applies in case of line or plane element.

        :return: bool
        """

        return self.com_object.OrientationOfFirstElement

    @orientation_of_first_element.setter
    def orientation_of_first_element(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.OrientationOfFirstElement = value

    @property
    def orientation_of_second_element(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property OrientationOfSecondElement() As boolean
                |     Returns or sets the orientation of the second element defining the rotation
                |     angle.
                |     This applies in case of line or plane element.

        :return: bool
        """

        return self.com_object.OrientationOfSecondElement

    @orientation_of_second_element.setter
    def orientation_of_second_element(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.OrientationOfSecondElement = value

    @property
    def rotation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RotationType() As long
                |     Returns or sets the type of the rotation definition.
                | 
                |         0= Axis + angle
                |         1= Axis + two elements
                |         2= Three Points
                |         3= Unknown type

        :return: int
        """

        return self.com_object.RotationType

    @rotation_type.setter
    def rotation_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.RotationType = value

    @property
    def second_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondElement() As Reference
                |     Returns or sets the second element defining the rotation angle.

        :return: Reference
        """

        return Reference(self.com_object.SecondElement)

    @second_element.setter
    def second_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondElement = value

    @property
    def second_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondPoint() As Reference
                |     Returns or sets the second point defining the rotation.

        :return: Reference
        """

        return Reference(self.com_object.SecondPoint)

    @second_point.setter
    def second_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondPoint = value

    @property
    def third_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ThirdPoint() As Reference
                |     Returns or sets the third point defining the rotation.

        :return: Reference
        """

        return Reference(self.com_object.ThirdPoint)

    @third_point.setter
    def third_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ThirdPoint = value

    @property
    def volume_result(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property VolumeResult() As boolean
                |     Returns or sets the volume result.
                |     Legal values: True if the result of Rotate is required as volume (option is
                |     effective only in case of volumes,requires GSO License) and False if it is
                |     needed as surface .
                | 
                |     Example:
                | 
                |          This example sets that the result of
                |          the hybShpRotate hybrid shape rotate is volume.
                |          
                | 
                |          hybShpRotate.VolumeResult = True

        :return: bool
        """

        return self.com_object.VolumeResult

    @volume_result.setter
    def volume_result(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.VolumeResult = value

    def get_creation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetCreationMode() As long
                |     Gets the creation mode.
                |     Legal values:
                | 
                |     0
                |         CATGSMTransfoModeUnset. Default behavior: creation mode by default for
                |         all features, modification mode for axis system
                |     1
                |         CATGSMTransfoModeCreation. Creation mode. 
                |     2
                |         CATGSMTransfoModeModification. Modification mode. 
                | 
                | Example:
                |     This example retrieves in oCreation the creation mode for the hybShpRotate
                |     hybrid shape feature.
                | 
                |      oCreation = hybShpRotate.GetCreationMode

        :return: int
        """
        return self.com_object.GetCreationMode()

    def set_creation_mode(self, i_creation: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetCreationMode(boolean iCreation)
                |     Sets the creation mode(creation or modification).
                |     Legal values: True if the result is a creation feature and False if the
                |     result is a modification feature.
                | 
                |     Example:
                | 
                |          This example sets that the mode of
                |          the hybShpRotate hybrid shape rotate to creation
                |          
                | 
                |          hybShpRotate.SetCreationMode True

        :param bool i_creation:
        :return: None
        """
        return self.com_object.SetCreationMode(i_creation)

    def __repr__(self):
        return f'HybridShapeRotate(name="{ self.name }")'
