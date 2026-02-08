"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DrawingDimExtLine(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingDimExtLine
                | 
                | Manages extension lines of a dimension in drawing view.
                | 
                | This interface is obtained from DrawingDimension.GetExtLine
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
                |     Returns or sets color of extension line.
                | 
                |     Example:
                |         This example retrieves color of extension line MyExtLine drawing
                |         dimension.
                | 
                |          oColorExtLine = MyExtLine.Color

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
    def ext_line_slant(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ExtLineSlant() As double
                |     Returns or sets slant angle of extension line.
                | 
                |     Example:
                |         This example retrieves slant angle of extension line MyExtLine drawing
                |         dimension.
                | 
                |          oExtLineSlant = MyExtLine.ExtLineSlant

        :return: float
        """

        return self.com_object.ExtLineSlant

    @ext_line_slant.setter
    def ext_line_slant(self, value: float):
        """
        :param float value:
        """

        self.com_object.ExtLineSlant = value

    @property
    def ext_line_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ExtLineType() As long (Read Only)
                |     Returns extension line type of dimension.
                | 
                |     Example:
                |         This example retrieves extension line type of dimension MyExtLine
                |         drawing dimension.
                | 
                |          oExtLineType = MyExtLine.ExtLineType

        :return: int
        """

        return self.com_object.ExtLineType

    @property
    def thickness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Thickness() As double
                |     Returns or sets thickness of extension line.
                | 
                |     Example:
                |         This example retrieves thickness of extension line MyExtLine drawing
                |         dimension.
                | 
                |          oThickExtLine = MyExtLine.Thickness

        :return: float
        """

        return self.com_object.Thickness

    @thickness.setter
    def thickness(self, value: float):
        """
        :param float value:
        """

        self.com_object.Thickness = value

    def add_interrupt(self, i_index: int, i_two_points: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddInterrupt(long iIndex,CATSafeArrayVariant iTwoPoints)
                |     Add an interrupt to an extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         iTwoPoints
                |             Defines the first and second point of the gap to create.
                |             
                |         Example:
                |             This example adds an interrupt to MyExtLine path.
                | 
                |              MyExtLine.AddInterrupt(iIndex, iTwoPoints)

        :param int i_index:
        :param tuple i_two_points:
        :return: None
        """
        return self.com_object.AddInterrupt(i_index, i_two_points)

    def get_funnel(self, i_index: int, o_mode: int, o_angle: float, o_height: float, o_width: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetFunnel(long iIndex,long oMode,double oAngle,double oHeight,double
                | oWidth)
                |     Get funnel infomation of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         oMode
                |             funnel inside/outside mode. 
                |         oAngle
                |             funnel angle. 
                |         oHeight
                |             funnel height. 
                |         oWidth
                |             funnel width. 
                |         Example:
                |             This example gets funnel infomation of MyExtLine
                |             path.
                | 
                |              MyExtLine.GetFunnel(iIndex, oMode, oAngle, oHeight,
                |              oWidth)

        :param int i_index:
        :param int o_mode:
        :param float o_angle:
        :param float o_height:
        :param float o_width:
        :return: None
        """
        return self.com_object.GetFunnel(i_index, o_mode, o_angle, o_height, o_width)

    def get_gap(self, i_index: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGap(long iIndex) As double
                |     Get gap of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         oGap
                |             Gap. 
                |         Example:
                |             This example gets gap of MyExtLine path.
                | 
                |              Gap = MyExtLine.GetGap(iIndex)

        :param int i_index:
        :return: float
        """
        return self.com_object.GetGap(i_index)

    def get_geom_info(self, i_index: int, o_geom_infos: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetGeomInfo(long iIndex,CATSafeArrayVariant oGeomInfos)
                |     Get geometrical infomation of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         oGeomInfos
                |             List of geometric coordinates (X1,Y1,X2,Y2,X3,Y3).
                |             
                |         Example:
                |             This example gets geometrical infomation of MyExtLine
                |             path.
                | 
                |              MyExtLine.GetGeomInfo(iIndex, oGeomInfos)

        :param int i_index:
        :param tuple o_geom_infos:
        :return: None
        """
        # todo: check this method, does it require system service?
        return self.com_object.GetGeomInfo(i_index, o_geom_infos)

    def get_interrupt(self, i_index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInterrupt(long iIndex) As long
                |     Get the number of interruptions stored in each extension
                |     lines.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         oNbIntOnExtLine
                |             The number of interruptions. 
                |         Example:
                |             This example gets the number of interruptions of MyExtLine
                |             path.
                | 
                |              NbIntOnExtLine = MyExtLine.GetInterrupt(iIndex)

        :param int i_index:
        :return: int
        """
        return self.com_object.GetInterrupt(i_index)

    def get_overrun(self, i_index: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOverrun(long iIndex) As double
                |     Get overrun of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         oOverrun
                |             Overrun 
                |         Example:
                |             This example gets overrun of MyExtLine path.
                | 
                |              Overrun = MyExtLine.GetOverrun(iIndex)

        :param int i_index:
        :return: float
        """
        return self.com_object.GetOverrun(i_index)

    def get_visibility(self, i_index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetVisibility(long iIndex) As long
                |     Get visivility of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         oGap
                |             Gap. 
                |         Example:
                |             This example gets visivility of MyExtLine path.
                | 
                |              ExtlineVisibility = MyExtLine.GetVisibility(iIndex)

        :param int i_index:
        :return: int
        """
        return self.com_object.GetVisibility(i_index)

    def remove_interrupt(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveInterrupt(long iIndex)
                |     Remove interruption on extension lines.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         Example:
                |             This example Remove interruption on MyExtLine
                |             path.
                | 
                |              MyExtLine.RemoveInterrupt(iIndex)

        :param int i_index:
        :return: None
        """
        return self.com_object.RemoveInterrupt(i_index)

    def set_funnel(self, i_index: int, i_mode: int, i_angle: float, i_height: float, i_width: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFunnel(long iIndex,long iMode,double iAngle,double iHeight,double
                | iWidth)
                |     Set funnel infomation of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         iMode
                |             funnel inside/outside mode. 
                |         iAngle
                |             funnel angle. 
                |         iHeight
                |             funnel height. 
                |         iWidth
                |             funnel width. 
                |         Example:
                |             This example sets funnel infomation of MyExtLine
                |             path.
                | 
                |              MyExtLine.SetFunnel(iIndex, iMode, iAngle, iHeight,
                |              iWidth)

        :param int i_index:
        :param int i_mode:
        :param float i_angle:
        :param float i_height:
        :param float i_width:
        :return: None
        """
        return self.com_object.SetFunnel(i_index, i_mode, i_angle, i_height, i_width)

    def set_gap(self, i_index: int, i_gap: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGap(long iIndex,double iGap)
                |     Set gap of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         iGap
                |             gap 
                |         Example:
                |             This example sets gap of MyExtLine path.
                | 
                |              MyExtLine.SetGap(iIndex, iGap)

        :param int i_index:
        :param float i_gap:
        :return: None
        """
        return self.com_object.SetGap(i_index, i_gap)

    def set_overrun(self, i_index: int, i_overrun: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOverrun(long iIndex,double iOverrun)
                |     Set overrun of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         iOverrun
                |             Overrun 
                |         Example:
                |             This example sets overrun of MyExtLine path.
                | 
                |              MyExtLine.SetOverrun(iIndex, iOverrun)

        :param int i_index:
        :param float i_overrun:
        :return: None
        """
        return self.com_object.SetOverrun(i_index, i_overrun)

    def set_visibility(self, i_index: int, i_extline_visibility: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetVisibility(long iIndex,long iExtlineVisibility)
                |     Set visivility of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         iExtlineVisibility
                |             visivility 
                |         Example:
                |             This example sets visivility of MyExtLine path.
                | 
                |              MyExtLine.SetVisibility(iIndex,
                |              iExtlineVisibility)

        :param int i_index:
        :param int i_extline_visibility:
        :return: None
        """
        return self.com_object.SetVisibility(i_index, i_extline_visibility)

    def __repr__(self):
        return f'DrawingDimExtLine(name="{self.name}")'
