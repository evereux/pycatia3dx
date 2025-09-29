"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.annotation.drawing_leaders import DrawingLeaders
from pycatia3dx.annotation.drawing_text_properties import DrawingTextProperties
from pycatia3dx.system.any_object import AnyObject


class DrawingText(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingText
                | 
                | Represents a drawing text in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def anchor_position(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnchorPosition() As CatTextAnchorPosition
                |     Returns or sets the anchor position of the drawing text.
                | 
                |     Example:
                |         This example sets the anchor position of the MyText drawing text to top
                |         left position.
                | 
                |          MyText.AnchorPosition = TopLeft

        :return: int
        """

        return self.com_object.AnchorPosition

    @anchor_position.setter
    def anchor_position(self, value: int):
        """
        :param int value:
        """

        self.com_object.AnchorPosition = value

    @property
    def angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Angle() As double
                |     Returns or sets the angle of the drawing text. The angle is measured
                |     between the axis system of the drawing view and the local axis system of the
                |     drawing text. The angle is measured in radians and is counted
                |     counterclockwise.
                | 
                |     Example:
                |         This example sets the angle of the MyText drawing Text to 90 degrees
                |         clockwise. You first need to compute the angle in degrees and set the minus
                |         sign to indicate the rotation is clockwise.
                | 
                |          Angle90Clockwise = -90
                |          MyText.Angle = Angle90Clockwise

        :return: float
        """

        return self.com_object.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.Angle = value

    @property
    def associative_element(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AssociativeElement() As CATBaseDispatch
                |     Returns or sets the associative object of the drawing
                |     text.
                | 
                |     Example:
                |         This example sets an associative line of the MyText drawing text to top
                |         left position.
                | 
                |          MyText.AssociativeElement = line

        :return: AnyObject
        """

        return AnyObject(self.com_object.AssociativeElement)

    @associative_element.setter
    def associative_element(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.AssociativeElement = value

    @property
    def frame_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FrameType() As CatTextFrameType
                |     Returns or sets the frame type of the drawing text.
                | 
                |     Example:
                |         This example sets the frame type of the MyText drawing text to an
                |         ellipse.
                | 
                |          MyText.FrameType = catEllipse

        :return: int
        """

        return self.com_object.FrameType

    @frame_type.setter
    def frame_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.FrameType = value

    @property
    def leaders(self) -> DrawingLeaders:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Leaders() As DrawingLeaders (Read Only)
                |     Returns the drawing leader collection of the drawing text.
                | 
                |     Example:
                |         This example retrieves in LeaderCollection the collection of leaders of
                |         the MyText drawing text.
                | 
                |          Dim LeaderCollection As DrawingLeaders
                |          Set LeaderCollection = MyText.Leaders

        :return: DrawingLeaders
        """

        return DrawingLeaders(self.com_object.Leaders)

    @property
    def lock_edition(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LockEdition() As boolean
                |     Returns or sets the LockEdition property of the text.
                | 
                |     Example:
                |         This example retrieves the x coordinate of the text MyText drawing
                |         text.
                | 
                |          LockEdition = MyText.LockEdition

        :return: bool
        """

        return self.com_object.LockEdition

    @lock_edition.setter
    def lock_edition(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.LockEdition = value

    @property
    def nb_link(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NbLink() As long (Read Only)
                |     Returns the number of attributes link
                | 
                |     Example:
                |         This example gets number of attributes link of MyText drawing
                |         text.
                | 
                |          nbLink = MyText.NbLink

        :return: int
        """

        return self.com_object.NbLink

    @property
    def orientation_reference(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OrientationReference() As long
                |     Returns or sets the orientation reference of the drawing
                |     text.
                |     0 : Sheet orientation
                |     1 : View/Label/2Dcomponent orientation
                | 
                |     Example:
                |         This example sets the orientation reference of MyText drawing text to
                |         sheet orientation
                | 
                |          MyText.OrientationReference = 0

        :return: int
        """

        return self.com_object.OrientationReference

    @orientation_reference.setter
    def orientation_reference(self, value: int):
        """
        :param int value:
        """

        self.com_object.OrientationReference = value

    @property
    def text(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Text() As CATBSTR
                |     Returns or sets character string that makes up the text.
                | 
                |     Example:
                |         This example retrieves in CharString the character string of the MyText
                |         drawing text.
                | 
                |          CharString = MyText.Text

        :return: str
        """

        return self.com_object.Text

    @text.setter
    def text(self, value: str):
        """
        :param str value:
        """

        self.com_object.Text = value

    @property
    def text_properties(self) -> DrawingTextProperties:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TextProperties() As DrawingTextProperties (Read Only)
                |     Returns the text properties of the drawing text. Allows to modify the whole
                |     text properties. To manage a sub part of the text use
                |     GetParameterOnSubString
                | 
                |     Example:
                |         This example retrieves in TextProperties the text properties of the
                |         MyText drawing text.
                | 
                |          Dim TextProperties As DrawingTextProperties
                |          Set TextProperties = MyText.TextProperties

        :return: DrawingTextProperties
        """

        return DrawingTextProperties(self.com_object.TextProperties)

    @property
    def wrapping_width(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WrappingWidth() As double
                |     Returns or sets the wrapping width of the drawing text.
                | 
                |     Example:
                |         This example sets the wrapping width of the MyText drawing text to
                |         50.
                | 
                |          MyText.WrappingWidth = 50.

        :return: float
        """

        return self.com_object.WrappingWidth

    @wrapping_width.setter
    def wrapping_width(self, value: float):
        """
        :param float value:
        """

        self.com_object.WrappingWidth = value

    @property
    def x(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property x() As double
                |     Returns or sets the x coordinate of the text. It is expressed with respect
                |     to the current view coordinate system. This coordinate, like any length, is
                |     measured in meters.
                | 
                |     Example:
                |         This example retrieves the x coordinate of the text MyText drawing
                |         text.
                | 
                |          X = MyText.x

        :return: float
        """

        return self.com_object.x

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.com_object.x = value

    @property
    def y(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property y() As double
                |     Returns or sets the y coordinate of the text. It is expressed with respect
                |     to the view coordinate system. This coordinate, like any length, is measured in
                |     meters.
                | 
                |     Example:
                |         This example sets the y coordinate of the text MyText drawing text to 5
                |         inches. You need first to convert the 5 inches into
                |         meters.
                | 
                |          NewYCoordinate = 5*25.4/1000
                |          MyText.y =  NewYCoordinate

        :return: float
        """

        return self.com_object.y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.com_object.y = value

    def activate_frame(self, itype: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub ActivateFrame(CatTextFrameType itype)
                |     Activates the text frame of the drawing text.
                | 
                |     Example:
                |         This example adds a rectangle frame to MyText drawing
                |         text.
                | 
                |          CatTextFrameType ityp = catRectangle
                |          MyText.ActivateFrame(itype)
                |          
                | 
                |         This example removes the frame to MyText drawing text.
                | 
                |          CatTextFrameType ityp = catNone
                |          MyText.ActivateFrame(itype)

        :param int itype:
        :return: None
        """
        return self.com_object.ActivateFrame(itype)

    def get_font_name(self, i_first: int, inb_character: int) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetFontName(long iFirst,long inbCharacter) As CATBSTR
                |     Returns the font name on a substring of the drawing text.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character to which the property should apply
                |             
                |         inbCharacter
                |             The number of characters to which the property should apply
                |             
                | 
                |     Returns:
                |         oFontName The name of the font 
                |     Example:
                |         This example gets the MyText drawing text font.
                | 
                |          oFontName = MyText.GetFontName(0, 0)

        :param int i_first:
        :param int inb_character:
        :return: str
        """
        return self.com_object.GetFontName(i_first, inb_character)

    def get_font_size(self, i_first: int, inb_character: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetFontSize(long iFirst,long inbCharacter) As double
                |     Returns the font size on a substring of the drawing text.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character to which the property should apply
                |             
                |         inbCharacter
                |             The number of characters to which the property should apply
                |             
                | 
                |     Returns:
                |         oFontSize The size of the font 
                |     Example:
                |         This example gets the MyText font size.
                | 
                |          oFontSize = MyText.GetFontSize(0, 0)

        :param int i_first:
        :param int inb_character:
        :return: float
        """
        return self.com_object.GetFontSize(i_first, inb_character)

    def get_modifiable_in_2d_component_instances(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetModifiableIn2DComponentInstances() As boolean
                |     Returns if the text is modifiable or not in 2D component instances. The
                |     text must own to a 2D component (NOT to a view)
                | 
                |     Example:
                |         This example retrieves if MyText drawing text is modifiable or
                |         not
                | 
                |          IsModifiable = MyText.GetModifiableIn2DComponentInstances

        :return: bool
        """
        return self.com_object.GetModifiableIn2DComponentInstances()

    def get_parameter_link(self, i_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetParameterLink(long iIndex) As CATBaseDispatch
                |     Returns the pointed parameter link
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the pointed parameter link. 1 <= iIndex <=
                |             NbLink
                | 
                |             Example:
                |                 This example gets the first parameter link of MyText drawing
                |                 text.
                | 
                |                  Dim MyParm As Parameter
                |                  MyParm = MyText.GetParameterLink(1)
                |                  If MyParm.Value<>"Front view" Then
                |                    'Do something
                |                  End If

        :param int i_index:
        :return: AnyObject
        """
        return self.com_object.GetParameterLink(i_index)

    def get_parameter_on_sub_string(self, i_param: int, i_first: int, inb_character: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetParameterOnSubString(CatTextProperty iParam,long iFirst,long
                | inbCharacter) As long
                |     Returns a property on a substring of the drawing text.
                | 
                |     Parameters:
                | 
                |         iParam
                |             The drawing text property 
                |         iFirst
                |             The first character to which the property should apply
                |             
                |         inbCharacter
                |             The number of characters to which the property should apply
                |             
                | 
                |     Returns:
                |         oval The value corresponding to the property 
                |     Example:
                |         This example gets the parameter Italic on MyText drawing
                |         text.
                | 
                |          CatTextProperty iParam = catItalic 
                |          iFirst = 0
                |          inbCharacter = 0
                |          oval = MyText.GetParameterOnsubString(iParam, iFirst, inbCharacter)

        :param int i_param:
        :param int i_first:
        :param int inb_character:
        :return: int
        """
        return self.com_object.GetParameterOnSubString(i_param, i_first, inb_character)

    def insert_attribute_link(self, i_first: int, inb_character: int, i_owner_att: AnyObject, i_type_internal_name: str,
                              i_att_internal_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub InsertAttributeLink(long iFirst,long inbCharacter,CATBaseDispatch
                | iOwnerAtt,CATBSTR iTypeInternalName,CATBSTR iAttInternalName)
                |     Replace the given selection by the given attribute value
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character from which the parameter is inserted
                |             
                |         inbCharacter
                |             The number of characters the parameter will replace
                |             
                |         iOwnerAtt
                |             Owner of the attribute 
                |         iTypeInternalName
                |             The internal name of the owner type 
                |         iAttInternalName
                |             The internal name of the attribute

        :param int i_first:
        :param int inb_character:
        :param AnyObject i_owner_att:
        :param str i_type_internal_name:
        :param str i_att_internal_name:
        :return: None
        """
        return self.com_object.InsertAttributeLink(i_first, inb_character, i_owner_att.com_object, i_type_internal_name,
                                                   i_att_internal_name)

    def insert_variable(self, i_first: int, inb_character: int, ibase: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub InsertVariable(long iFirst,long inbCharacter,CATBaseDispatch
                | ibase)
                |     Sets a Parameter in a string of the drawing text.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character from which the parameter is inserted
                |             
                |         inbCharacter
                |             The number of characters the parameter will replace
                |             
                |         iParameter
                |             The parameter to be inserted 
                |         Example:
                |             This example sets a parameter right at the end of MyText drawing
                |             text.
                | 
                |              Dim MyDrawing as DrawingDrawing
                |              Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |              Dim iParameter As Parameter
                |              Set iParameter = MyDrawing.Parameters.Item("Drawing\\Sheet.1\\ViewMakeUp.1\\Scale")
                | 
                |              MyText.InsertVariable 0, 0, iParameter

        :param int i_first:
        :param int inb_character:
        :param AnyObject ibase:
        :return: None
        """
        return self.com_object.InsertVariable(i_first, inb_character, ibase.com_object)

    def set_font_name(self, i_first: int, inb_character: int, i_font_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetFontName(long iFirst,long inbCharacter,CATBSTR
                | iFontName)
                |     Sets the font size on a substring of the drawing text.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character to which the property should apply
                |             
                |         inbCharacter
                |             The number of characters to which the property should apply
                |             
                |         iFontName
                |             The name of the font
                | 
                |             Example:
                |                 This example sets the MyText drawing text font as Courrier 10
                |                 BT.
                | 
                |                  MyText.SetFontName 0,  0, "Courrier 10 BT"

        :param int i_first:
        :param int inb_character:
        :param str i_font_name:
        :return: None
        """
        return self.com_object.SetFontName(i_first, inb_character, i_font_name)

    def set_font_size(self, i_first: int, inb_character: int, i_font_size: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetFontSize(long iFirst,long inbCharacter,double
                | iFontSize)
                |     Sets the font size on a substring of the drawing text.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character to which the property should apply
                |             
                |         inbCharacter
                |             The number of characters to which the property should apply
                |             
                |         iFontSize
                |             The size of the font 
                |         Example:
                |             This example sets the MyText font size to 3.5.
                | 
                |              iFontSize = 3.5
                |              MyText.SetFontSize 0,  0, iFontSize

        :param int i_first:
        :param int inb_character:
        :param float i_font_size:
        :return: None
        """
        return self.com_object.SetFontSize(i_first, inb_character, i_font_size)

    def set_modifiable_in_2d_component_instances(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetModifiableIn2DComponentInstances()
                |     Sets the text as modifiable in 2D component instances.The text must own to
                |     a 2D component (NOT to a view).then ,its content will be modifiable inside
                |     instances of this 2D component.
                | 
                |     Example:
                |         This example sets the MyText drawing text as
                |         modifiable.
                | 
                |          MyText.SetModifiableIn2DComponentInstances

        :return: None
        """
        return self.com_object.SetModifiableIn2DComponentInstances()

    def set_parameter_on_sub_string(self, i_param: int, i_first: int, inb_character: int, i_val: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetParameterOnSubString(CatTextProperty iParam,long iFirst,long
                | inbCharacter,long iVal)
                |     Sets a property on a substring of the drawing text.
                | 
                |     Parameters:
                | 
                |         iParam
                |             The drawing text property 
                |         iFirst
                |             The first character to which the property should apply
                |             
                |         inbCharacter
                |             The number of characters to which the property should apply
                |             
                |         iVal
                |             The value to be applied according to the property 
                |         Example:
                |             This example sets all MyText drawing text in bold
                |             character.
                | 
                |              CatTextProperty iParam = catBold 
                |              iFirst = 0
                |              inbCharacter = 0
                |              ival = 1
                |              MyText.SetParameterOnsubString iParam, iFirst, inbCharacter,
                |              ival

        :param int i_param:
        :param int i_first:
        :param int inb_character:
        :param int i_val:
        :return: None
        """
        return self.com_object.SetParameterOnSubString(i_param, i_first, inb_character, i_val)

    def solve_link(self, ip_obj: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SolveLink(CATBaseDispatch ipObj)
                |     Resolve Link Template of the drawing text.
                | 
                |     Parameters:
                | 
                |         ipObj
                |             The object on wich the link template of the text will be solved.
                |             
                |         Example:
                |             This example solve the link template of MyText drawing
                |             text.
                | 
                |              MyText.SolveLink ipObj

        :param AnyObject ip_obj:
        :return: None
        """
        return self.com_object.SolveLink(ip_obj.com_object)

    def __repr__(self):
        return f'DrawingText(name="{self.name}")'
