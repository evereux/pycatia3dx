"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DrawingDimLine(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingDimLine
                | 
                | Manages dimension line of a dimension in drawing view.
                | 
                | This interface is obtained from DrawingDimension.GetDimLine
                | method.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def color(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Color() As long
                |     Returns or sets color of dimension line.
                | 
                |     Example:
                |         This example retrieves color of dimension line MyDimLine drawing
                |         dimension.
                | 
                |          oColorDimLine = MyDimLine.Color

        :return: int
        """

        return self.com_object.Color

    @color.setter
    def color(self, value: int):
        """
        :param int value:
        """

        self.com_object.Color = value

    @property
    def dim_line_graph_rep(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DimLineGraphRep() As CatDimLineGraphRep
                |     Returns or graphic representation of dimension line.
                | 
                |     Example:
                |         This example retrieves graphic representation of dimension line
                |         MyDimLine drawing dimension.
                | 
                |          odimLineGraphRep = MyDimLine.DimLineGraphRep

        :return: int
        """

        return self.com_object.DimLineGraphRep

    @dim_line_graph_rep.setter
    def dim_line_graph_rep(self, value: int):
        """
        :param int value:
        """

        self.com_object.DimLineGraphRep = value

    @property
    def dim_line_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DimLineOrientation() As CatDimOrientation
                |     Returns or orientation of dimension line.
                | 
                |     Example:
                |         This example retrieves orientation of dimension line MyDimLine drawing
                |         dimension.
                | 
                |          odimLineOrient = MyDimLine.DimLineOrientation

        :return: int
        """

        return self.com_object.DimLineOrientation

    @dim_line_orientation.setter
    def dim_line_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.DimLineOrientation = value

    @property
    def dim_line_reference(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DimLineReference() As CatDimReference
                |     Returns or reference of dimension line.
                | 
                |     Example:
                |         This example retrieves reference of dimension line MyDimLine drawing
                |         dimension.
                | 
                |          odimLineRef = MyDimLine.DimLineReference

        :return: int
        """

        return self.com_object.DimLineReference

    @dim_line_reference.setter
    def dim_line_reference(self, value: int):
        """
        :param int value:
        """

        self.com_object.DimLineReference = value

    @property
    def dim_line_rep(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DimLineRep() As CatDimLineRep (Read Only)
                |     Returns or representation of dimension line.
                | 
                |     Example:
                |         This example retrieves representation of dimension line MyDimLine
                |         drawing dimension.
                | 
                |          odimLineRep = MyDimLine.DimLineRep

        :return: int
        """

        return self.com_object.DimLineRep

    @property
    def dim_line_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DimLineType() As long (Read Only)
                |     Returns type of dimension line.
                | 
                |     Example:
                |         This example retrieves type of dimension line MyDimLine drawing
                |         dimension.
                | 
                |          odimLineType = MyDimLine.DimLineType

        :return: int
        """

        return self.com_object.DimLineType

    @property
    def thickness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Thickness() As double
                |     Returns or sets thickness of dimension line.
                | 
                |     Example:
                |         This example retrieves thickness of dimension line MyDimLine drawing
                |         dimension.
                | 
                |          oThickDimLine = MyDimLine.Thickness

        :return: float
        """

        return self.com_object.Thickness

    @thickness.setter
    def thickness(self, value: float):
        """
        :param float value:
        """

        self.com_object.Thickness = value

    def get_dim_line_dir(self, o_dir_x: float, o_dir_y: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDimLineDir(double oDirX,double oDirY)
                |     Returns direction of a dimension line in case of a catDimUserDefined
                |     representation mode. To retrieve the representation mode:
                |     DrawingDimLine.get_DimLineRep.
                | 
                |     Parameters:
                | 
                |         oDirX,oDirY
                |             The components of the direction vector 
                |         Example:
                |             This example retrieves the direction vector of a dimension line
                |             MyDimLine drawing dimension.
                | 
                |              MyDimLine.GetDimLineDir oDirX, oDirY

        :param float o_dir_x:
        :param float o_dir_y:
        :return: None
        """
        return self.com_object.GetDimLineDir(o_dir_x, o_dir_y)

    def get_geom_info(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetGeomInfo(CATSafeArrayVariant oGeomInfos)
                |     Get geometrical infomation of dimension line.
                | 
                |     Parameters:
                | 
                |         oGeomInfos
                |             geometrical information. 
                |         Example:
                |             This example gets geometrical infomation of MyDimLine
                |             path.
                | 
                |              MyDimLine.GetGeomInfo(oGeomInfos)

        :return: tuple
        """
        # todo: check this method, does it require system service?
        return self.com_object.GetGeomInfo()
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise, completely remove all this.
        # # vba_function_name = 'get_geom_info'
        # # vba_code = """
        # # Public Function get_geom_info(drawing_dim_line)
        # #     Dim oGeomInfos (2)
        # #     drawing_dim_line.GetGeomInfo oGeomInfos
        # #     get_geom_info = oGeomInfos
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_symb_color(self, index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSymbColor(long Index) As long
                |     Get symbol color of dimension line.
                | 
                |     Parameters:
                | 
                |         Index
                |             1:first symbol 2:second symbol 3:leader symbol 
                |         oColorSymb
                |             symbol color. 
                |         Example:
                |             This example gets symbol color of MyDimLine path.
                | 
                |              ColorSymb = MyDimLine.GetSymbColor(Index)

        :param int index:
        :return: int
        """
        return self.com_object.GetSymbColor(index)

    def get_symb_thickness(self, index: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSymbThickness(long Index) As double
                |     Get symbol thickness of dimension line.
                | 
                |     Parameters:
                | 
                |         Index
                |             1:first symbol 2:second symbol 3:leader symbol 
                |         oThickSymb
                |             symbol thickness. 
                |         Example:
                |             This example gets symbol thickness of MyDimLine
                |             path.
                | 
                |              ThickSymb = MyDimLine.GetSymbThickness(Index)

        :param int index:
        :return: float
        """
        return self.com_object.GetSymbThickness(index)

    def get_symb_type(self, index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSymbType(long Index) As CatDimSymbols
                |     Get symbol type of dimension line.
                | 
                |     Parameters:
                | 
                |         Index
                |             1:first symbol 2:second symbol 3:leader symbol 
                |         oTypeSymb
                |             symbol type. 
                |         Example:
                |             This example gets symbol type of MyDimLine path.
                | 
                |              typeSymb = MyDimLine.GetSymbType(Index)

        :param int index:
        :return: int
        """
        return self.com_object.GetSymbType(index)

    def set_symb_color(self, index: int, i_color_symb: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSymbColor(long Index,long iColorSymb)
                |     Set symbol color of dimension line.
                | 
                |     Parameters:
                | 
                |         Index
                |             1:first symbol 2:second symbol 3:leader symbol 
                |         oColorSymb
                |             symbol color. 
                |         Example:
                |             This example sets symbol color of MyDimLine path.
                | 
                |              MyDimLine.SetSymbColor(Index, iColorSymb)

        :param int index:
        :param int i_color_symb:
        :return: None
        """
        return self.com_object.SetSymbColor(index, i_color_symb)

    def set_symb_thickness(self, index: int, i_thick_symb: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSymbThickness(long Index,double iThickSymb)
                |     Set symbol thickness of dimension line.
                | 
                |     Parameters:
                | 
                |         Index
                |             1:first symbol 2:second symbol 3:leader symbol 
                |         oThickSymb
                |             symbol thickness. 
                |         Example:
                |             This example sets symbol thickness of MyDimLine
                |             path.
                | 
                |              MyDimLine.GetSymbThickness(Index, iThickSymb)

        :param int index:
        :param float i_thick_symb:
        :return: None
        """
        return self.com_object.SetSymbThickness(index, i_thick_symb)

    def set_symb_type(self, index: int, i_symb_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSymbType(long Index,CatDimSymbols iSymbType)
                |     Set symbol type of dimension line.
                | 
                |     Parameters:
                | 
                |         Index
                |             1:first symbol 2:second symbol 3:leader symbol 
                |         iSymbType
                |             symbol type. 
                |         Example:
                |             This example sets symbol type of MyDimLine path.
                | 
                |              MyDimLine.SetSymbType(Index, iSymbType)

        :param int index:
        :param int i_symb_type:
        :return: None
        """
        return self.com_object.SetSymbType(index, i_symb_type)

    def __repr__(self):
        return f'DrawingDimLine(name="{self.name}")'
