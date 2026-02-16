"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.opns_measure.measures import Measures

from pycatia3dx.interfaces.editor import Editor
from pycatia3dx.mmr_automation_interfaces.part import Part
from pycatia3dx.plm_validation.markers import Markers
from pycatia3dx.system.any_object import AnyObject


class Section(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Section
                | 
                | Interface representing a section.
                | set or get the position of section plane, set or get the clipping mode and
                | export it as 3DShape & PLMDrawing
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def behavior(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Behavior() As CatSectionBehavior
                |     Returns or sets the general behavior of the section: Freeze, Automatic
                |     update, manual update
                | 
                |     The behavior value are defined in CatSectionBehavior.
                | 
                |     Example:
                | 
                |             The first example retrieves the behavior of NewSection
                |             Section.
                |             
                | 
                |             Dim SectionBehavior As CatSectionBehavior
                |             Behavior = NewSection.Behavior
                |             
                | 
                | 
                |             
                | 
                |                 The second example sets the behavior of NewSection
                |                 Section.
                |                 
                | 
                |                 NewSection.Behavior = catSectionBehaviorAutomatic

        :return: CatSectionBehavior
        """

        return self.com_object.Behavior

    @behavior.setter
    def behavior(self, value: int):
        """
        :param int value:
        """

        self.com_object.Behavior = value

    @property
    def height(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Height(double iHeight)
                |     Returns or sets the height of the section.
                | 
                |     The height value must be greater than 0.
                | 
                |     Example:
                | 
                |             The first example retrieves the height of NewSection
                |             Section.
                |             
                | 
                |             Dim SectionHeight As double
                |             SectionHeight = NewSection.Height
                |             
                | 
                | 
                |             
                | 
                |                 The second example sets the height value of NewSection
                |                 Section.
                |                 
                | 
                |                 NewSection.Height = 100.

        :return: float
        """

        return self.com_object.Height

    @height.setter
    def height(self, value: float):
        """
        :param float value:
        """

        self.com_object.Height = value

    @property
    def markers(self) -> Markers:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Markers() As Markers (Read Only)
                |     Returns the Markers collection of the section.
                | 
                |     Example:
                | 
                |             This example retrieves the Markers collection of TheSection  
                |             Section.
                |             
                | 
                |             Dim TheMarkersList As Markers
                |             Set TheMarkersList = TheSection.Markers

        :return: Markers
        """

        return Markers(self.com_object.Markers)

    @property
    def measures(self) -> Measures:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Measures() As Measures (Read Only)
                |     Returns the Measures collection of the section.
                | 
                |     Example:
                | 
                |             This example retrieves the Measures collection of TheSection  
                |             Section.
                |             
                | 
                |             Dim TheMeasureList As Measures
                |             Set TheMeasureList = TheSection.Measures

        :return: Measures
        """

        return Measures(self.com_object.Measures)

    @property
    def scene_render(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SceneRender(long iMode)
                |     Returns or sets the Scene Render Mode of the section.
                |     Role: Returns or sets the mode of scene render (1 for clipping, 0
                |     otherwise).

        :return: int
        """

        return self.com_object.SceneRender

    @scene_render.setter
    def scene_render(self, value: int):
        """
        :param int value:
        """

        self.com_object.SceneRender = value

    @property
    def thickness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Thickness(double iThickness)
                |     Returns or sets the Thickness of the section for type slice &
                |     box.
                | 
                |     The Thickness value must be greater than 0.
                | 
                |     Example:
                | 
                |             The first example retrieves the Thickness of NewSection
                |             Section.
                |             
                | 
                |             Dim SectionWidth As double
                |             SectionThickness = NewSection.Thickness
                |
                |                 The second example sets the width value of NewSection
                |                 Section.
                |
                |                 NewSection.Thickness = 100.

        :return: float
        """

        return self.com_object.Thickness

    @thickness.setter
    def thickness(self, value: float):
        """
        :param float value:
        """

        self.com_object.Thickness = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type(CatSectionType iType)
                |     Returns or sets the type of the section.
                | 
                |     The type value are defined in CatSectionType.
                | 
                |     Example:
                | 
                |             The first example retrieves the type of NewSection
                |             Section.
                |
                |             Dim SectionType As CatSectionType
                |             SectionType = NewSection.Type
                |
                |                 The second example sets the type of NewSection
                |                 Section.
                |
                |                 NewSection.Type = catSectionTypeSlice

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    @property
    def width(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Width(double iWidth)
                |     Returns or sets the width of the section.
                | 
                |     The width value must be greater than 0.
                | 
                |     Example:
                | 
                |             The first example retrieves the width of NewSection
                |             Section.
                |             
                |             Dim SectionWidth As double
                |             SectionWidth = NewSection.Width
                |
                |                 The second example sets the width value of NewSection
                |                 Section.
                |
                |                 NewSection.Width = 100.

        :return: float
        """

        return self.com_object.Width

    @width.setter
    def width(self, value: float):
        """
        :param float value:
        """

        self.com_object.Width = value

    def export(self, io_part: Part) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Export(Part ioPart)
                |     Exports the sections curves of the section in a 3DShape representation this
                |     method assumes that you have created the Part in which you want to do the
                |     export
                | 
                |     Returns:
                |         The 3DShape Representation 
                |     Example:
                | 
                |             
                | 
                |              Dim  MyOpenEditor  As  Editor 
                |              Set myNewService = CATIA.GetSessionService("PLMNewService")
                |              myNewService.PLMCreate "3DShape", myOpenEditor
                |              Dim myPart As Part
                |              Set myPart = CATIA.ActiveEditor.ActiveObject
                |              mySection.Export myPart

        :param Part io_part:
        :return: None
        """
        return self.com_object.Export(io_part.com_object)

    def export_as_drawing(self, io_my_editor: Editor) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ExportAsDrawing(Editor ioMyEditor)
                |     Exports the section curves in a new 2D Drawing Representation. This method
                |     assumes that you have created the drawing in which you want to do the
                |     export.
                | 
                |     Returns:
                |         The Editor corresponding to drawing Representation with section curves
                |         exported under it. 
                |     Example:
                | 
                |             
                | 
                |              Dim  MyOpenEditor As Editor 
                |              Set myNewService = CATIA.GetSessionService("PLMNewService")
                |              myNewService.PLMCreate "Drawing", myOpenEditor
                |              mySection.ExportAsDrawing MyOpenEditor

        :param Editor io_my_editor:
        :return: None
        """
        return self.com_object.ExportAsDrawing(io_my_editor.com_object)

    def export_to(self, i_format: str, i_save_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ExportTo(CATBSTR iFormat,CATBSTR iSavePath)
                |     Exports the section into dxf/dwg formats. It takes inputs as type to which
                |     you want to export as "dxf" or "dwg" and path where you want to save exported
                |     file(without extension).
                | 
                |     Example:
                | 
                |             
                | 
                |              mySection.ExportTo "dxf", "c:\\ExportDxf" (For export as
                |              dxf)
                |              mySection.ExportTo "dwg", "c:\\ExportDwg" (For export as
                |              dwg)

        :param str i_format:
        :param str i_save_path:
        :return: None
        """
        return self.com_object.ExportTo(i_format, i_save_path)

    def export_to_existing(self, io_part: Part) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ExportToExisting(Part ioPart)
                |     Export the result of the section in an existing
                |     Product/Part.
                |     The input part should be created by user as a new part under existing
                |     product or user can supply an existing part from assembly.
                |     For exporting to existing Product representation, user should create a new
                |     3D Shape Representation under product & supply it as input
                |     here.
                |     Else user can supply an exising 3D Shape Representation from assembly
                |     directly. Here it is assumed that this 3D Shape Representation is in design
                |     mode.
                |     Also note that in either cases, this input part should be
                |     editable.
                | 
                |     Parameters:
                | 
                |         ioPart
                |             The part in which the geometry of section will be
                |             exported.
                | 
                |     Returns:
                |         S_OK if export is successful else E_FAIL.

        :param Part io_part:
        :return: None
        """
        return self.com_object.ExportToExisting(io_part.com_object)

    def get_position(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetPosition(CATSafeArrayVariant iComponents)
                |     Get the current position of the section.
                |
                |     Parameters:
                |
                |         iComponents
                |             The position of the section with respect to the absolute coordinate
                |             system
                |
                |                 iComponents( 0) is the X component of the
                |                 X-axis
                |                 iComponents( 1) is the Y component of the
                |                 X-axis
                |                 iComponents( 2) is the Z component of the
                |                 X-axis
                |                 iComponents( 3) is the X component of the
                |                 Y-axis
                |                 iComponents( 4) is the Y component of the
                |                 Y-axis
                |                 iComponents( 5) is the Z component of the
                |                 Y-axis
                |                 iComponents( 6) is the X component of the
                |                 Z-axis
                |                 iComponents( 7) is the Y component of the
                |                 Z-axis
                |                 iComponents( 8) is the Z component of the
                |                 Z-axis
                |                 iComponents( 9) is the X component of the
                |                 origin
                |                 iComponents(10) is the Y component of the
                |                 origin
                |                 iComponents(11) is the Z component of the origin
                |
                |
                |     Example:
                |
                |             This example gets the position of NewSection
                |             Section.
                |
                |
                |             Dim MatrixPos (11) As Double
                |             NewSection.GetPosition MatrixPos

        :return: tuple
        """
        return self.com_object.GetPosition()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_position'
        # vba_code = """
        # Public Function get_position(section)
        #     Dim iComponents (2)
        #     section.GetPosition iComponents
        #     get_position = iComponents
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def is_empty(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsEmpty() As long
                |     Indicates whether the section is empty.
                | 
                |     The indicator value is 0 if the section is empty or 1 if the section
                |     comprise at least one segment.
                | 
                |     Example:
                | 
                |             This example retrieves the information on NewSection
                |             Section.
                |             
                | 
                |             Dim Indicator
                |             Indicator = NewSection.IsEmpty

        :return: int
        """
        return self.com_object.IsEmpty()

    def set_position(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetPosition(CATSafeArrayVariant iComponents)
                |     Set the position of the section.
                |
                |     Parameters:
                |
                |         iComponents
                |             The position of the section with respect to the absolute coordinate
                |             system
                |
                |                 iComponents( 0) is the X component of the
                |                 X-axis
                |                 iComponents( 1) is the Y component of the
                |                 X-axis
                |                 iComponents( 2) is the Z component of the
                |                 X-axis
                |                 iComponents( 3) is the X component of the
                |                 Y-axis
                |                 iComponents( 4) is the Y component of the
                |                 Y-axis
                |                 iComponents( 5) is the Z component of the
                |                 Y-axis
                |                 iComponents( 6) is the X component of the
                |                 Z-axis
                |                 iComponents( 7) is the Y component of the
                |                 Z-axis
                |                 iComponents( 8) is the Z component of the
                |                 Z-axis
                |                 iComponents( 9) is the X component of the
                |                 origin
                |                 iComponents(10) is the Y component of the
                |                 origin
                |                 iComponents(11) is the Z component of the origin
                |
                |
                |     Example:
                |
                |             This example sets the position of NewSection
                |             Section.
                |
                |
                |             Dim MatrixPos (11) As Double
                |             MatrixPos( 0) = 1.0
                |             MatrixPos( 1) = 0.0
                |             MatrixPos( 2) = 0.0
                |             MatrixPos( 3) = 0.0
                |             MatrixPos( 4) = 1.0
                |             MatrixPos( 5) = 0.0
                |             MatrixPos( 6) = 0.0
                |             MatrixPos( 7) = 0.0
                |             MatrixPos( 8) = 1.0
                |             MatrixPos( 9) = 1000.0
                |             MatrixPos(10) = 0.0
                |             MatrixPos(11) = 0.0
                |             NewSection.SetPosition MatrixPos

        :return: tuple
        """
        return self.com_object.SetPosition()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_position'
        # vba_code = """
        # Public Function set_position(section)
        #     Dim iComponents (2)
        #     section.SetPosition iComponents
        #     set_position = iComponents
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Section(name="{self.name}")'
