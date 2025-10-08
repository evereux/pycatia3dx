"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class StrSectionMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrSectionMngt
                | 
                | Object to manage Structure Functional Modeler section applied to a
                | Profile.
                | Role: To access section parameters of Structure profile.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def anchor_point(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnchorPoint() As CATBSTR
                |     Returns or Sets the anchor point of this Profile.
                |     Legal Values:
                |     catStrBottomCenter
                |     catStrBottomLeft
                |     catStrBottomRight
                |     catStrGravity
                |     catStrTopCenter
                |     catStrTopLeft
                |     catStrTopRight
                |     catStrCenterCenter
                |     catStrCenterLeft
                |     catStrCenterRight
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the anchor point of the
                |              Profile.
                |              
                | 
                |               Dim ObjStrSectionMngt As StrSectionMngt
                |               Set ObjStrSectionMngt = ObjSfdStiffener.StrSectionMngt
                |               AnchorPoint = ObjStrSectionMngt.AnchorPoint

        :return: str
        """

        return self.com_object.AnchorPoint

    @anchor_point.setter
    def anchor_point(self, value: str):
        """
        :param str value:
        """

        self.com_object.AnchorPoint = value

    @property
    def angle_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AngleMode() As long
                |     Returns or Sets the angle mode of this stiffener function.
                |     Legal values :
                |     -1 : undefined mode
                |     1 : normal to plate
                |     0 : along plane
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the angle mode of this
                |              Profile.
                |              
                | 
                |               AngleMode = ObjStrSectionMngt.AngleMode

        :return: int
        """

        return self.com_object.AngleMode

    @angle_mode.setter
    def angle_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.AngleMode = value

    @property
    def flange_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FlangeOrientation() As long
                |     Returns or Sets the Flange orientation of the positioned section of this
                |     Profile.
                |     Legal values :
                |     -1 : Invert
                |     1 : Normal
                |     0 : Unknown orientation
                | 
                |     Example:
                | 
                | 
                |              This example retrieves flange orientation of the section of the
                |              profile.
                |              
                | 
                |               FlangeOrientation = ObjStrSectionMngt.FlangeOrientation

        :return: int
        """

        return self.com_object.FlangeOrientation

    @flange_orientation.setter
    def flange_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.FlangeOrientation = value

    @property
    def ref_element_for_angle(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RefElementForAngle() As Reference
                |     Returns or Sets the reference element used in "AlongPlane" mode for this
                |     Profile.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves reference element for the
                |              profile.
                |              
                | 
                |               RefElement = ObjStrSectionMngt.RefElementForAngle

        :return: Reference
        """

        return Reference(self.com_object.RefElementForAngle)

    @ref_element_for_angle.setter
    def ref_element_for_angle(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.RefElementForAngle = value

    @property
    def web_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WebOrientation() As long
                |     Returns or Sets the Web orientation of the positioned section of this
                |     Profile.
                |     Legal values :
                |     -1 : Invert
                |     1 : Normal
                |     0 : Unknown orientation
                | 
                |     Example:
                | 
                | 
                |              This example retrieves web orientation of the section of the
                |              profile.
                |              
                | 
                |               WebOrientation = ObjStrSectionMngt.WebOrientation

        :return: int
        """

        return self.com_object.WebOrientation

    @web_orientation.setter
    def web_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.WebOrientation = value

    def get_angle(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAngle() As Parameter
                |     Returns the section's angle for this Profile.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the section's angle for the
                |              profile.
                |              
                | 
                |               Dim ParmAngle As Parameter
                |               Set ParmAngle = ObjStrSectionMngt.GetAngle

        :return: Parameter
        """
        return Parameter(self.com_object.GetAngle())

    def get_flange_anchor_point_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFlangeAnchorPointOffset() As Parameter
                |     Returns the Flange Anchor Point Offset parameter.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the flange anchor point
                |              offset.
                |              
                | 
                |               Dim ParamFlangeAnchorPointOffset As Parameter
                |               Set ParamFlangeAnchorPointOffset = ObjStrSectionMngt.GetFlangeAnchorPointOffset

        :return: Parameter
        """
        return Parameter(self.com_object.GetFlangeAnchorPointOffset())

    def get_parameter(self, i_name: str) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameter(CATBSTR iName) As Parameter
                |     Returns a KWE parameter in the section document.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the parameter in the section
                |              document.
                |              
                | 
                |               Set Param = ObjStrSectionMngt.GetParameter "ParamName"

        :param str i_name:
        :return: Parameter
        """
        return Parameter(self.com_object.GetParameter(i_name))

    def get_placed_section_axis(self, i_lambda: float, o_first_dir: tuple, o_second_dir: tuple, o_third_dir: tuple, o_origin: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPlacedSectionAxis(double iLambda,CATSafeArrayVariant
                | oFirstDir,CATSafeArrayVariant oSecondDir,CATSafeArrayVariant
                | oThirdDir,CATSafeArrayVariant oOrigin)
                |     Computes the axis used to place the section on the guide
                |     curve.
                | 
                |     Parameters:
                | 
                |         iLambda
                |             Curvilinear abscide on the specified domain. Value in [0. , 1.].
                |             
                |         oFirstDir
                |             FirstAxis. 
                |         oSecondDir
                |             SecondAxis. 
                |         oThirdDir
                |             ThirdAxis. 
                |         oOrigin
                |             OriginAxis. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the section's angle for the
                |              profile.
                |              
                | 
                |               Dim FirstDir() As Variant
                |               Dim SecondDir() As Variant
                |               Dim ThirdDir() As Variant
                |               Dim Origin() As Variant
                |               ObjStrSectionMngt.GetPlacedSectionAxis 0.5, FirstDir, SecondDir,
                |               ThirdDir, Origin

        :param float i_lambda:
        :param tuple o_first_dir:
        :param tuple o_second_dir:
        :param tuple o_third_dir:
        :param tuple o_origin:
        :return: tuple
        """
        return self.com_object.GetPlacedSectionAxis(i_lambda, o_first_dir, o_second_dir, o_third_dir, o_origin)

    def get_section_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSectionName() As CATBSTR
                |     Returns the section name of the section used by this
                |     Profile.
                | 
                |     Example:
                | 
                | 
                |              This example gets the section name of the
                |              profile.
                |              
                | 
                |               SectionName = ObjStrSectionMngt.GetSectionName

        :return: str
        """
        return self.com_object.GetSectionName()

    def get_web_anchor_point_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetWebAnchorPointOffset() As Parameter
                |     Returns the Web Anchor Point offset parameter.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the web anchor point
                |              offset.
                |              
                | 
                |               Dim WebAnchorPointOffset As Parameter
                |               Set WebAnchorPointOffset = ObjStrSectionMngt.GetWebAnchorPointOffset

        :return: Parameter
        """
        return Parameter(self.com_object.GetWebAnchorPointOffset())

    def invert_flange_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InvertFlangeOrientation()
                |     Inverts the Flange orientation of the positioned section of this Profile.
                |     It is equivalent a XFlip.

        :return: None
        """
        return self.com_object.InvertFlangeOrientation()

    def invert_web_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InvertWebOrientation()
                |     Inverts the Web orientation of the positioned section of this Profile. It
                |     is equivalent to a YFlip.

        :return: None
        """
        return self.com_object.InvertWebOrientation()

    def set_section_name(self, i_section_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSectionName(CATBSTR iSectionName)
                |     Sets the section name on this Profile.
                | 
                |     Parameters:
                | 
                |         iSectionName
                |             Section name. 
                | 
                |     Example:
                | 
                | 
                |              This example sets the section name of the
                |              profile.
                |              
                | 
                |               ObjStrSectionMngt.SetSectionName "SectionName"

        :param str i_section_name:
        :return: None
        """
        return self.com_object.SetSectionName(i_section_name)

    def __repr__(self):
        return f'StrSectionMngt(name="{ self.name }")'
