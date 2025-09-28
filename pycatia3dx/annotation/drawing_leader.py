"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.annotation.drawing_leaders import DrawingLeaders
from pycatia3dx.system.any_object import AnyObject


class DrawingLeader(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingLeader
                | 
                | Represents a drawing leader in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def all_around(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllAround() As boolean
                |     Returns or sets the status of all around.
                | 
                |     Example:
                |         This example retrieves the status of all around on MyLeader drawing
                |         leader.
                | 
                |          oSymbol = MyLeader.AllAround

        :return: bool
        """

        return self.com_object.AllAround

    @all_around.setter
    def all_around(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AllAround = value

    @property
    def anchor_point(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnchorPoint() As long
                |     Returns or sets anchor point.
                | 
                |     Example:
                |         This example retrieves the anchor point on MyLeader drawing
                |         leader.
                | 
                |          oAnchorPoint = MyLeader.AnchorPoint

        :return: int
        """

        return self.com_object.AnchorPoint

    @anchor_point.setter
    def anchor_point(self, value: int):
        """
        :param int value:
        """

        self.com_object.AnchorPoint = value

    @property
    def anchor_symbol(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnchorSymbol() As long
                |     Returns or sets the anchor symbol of the drawing leader. AnchorSymbol 0 : No anchor symbol 1 : All-Around style (circle) - For GDT, Text, Table 2 : All-Over (2 concentric circles) - For GDT, Text, Table 3 : AllAboutWithHorLine (square with an horizontal line) - For GDT, Text, Table 4 : AllAboutWithVerLine (square with a vertical line) - For GDT, Text, Table 5 : AllAroundPartial (half circle) - For GDT, Text, Table 6 : AllOverPartial (2 half concentric circles) - For GDT, Text, Table 7 : AllAboutWithHorLinePartial (half square with an horizontal line) - For GDT, Text, Table 8 : AllAboutWithVerLinePartial (half square with an vertical line) - For GDT, Text, Table 9 : Flag (Flag) - For welding annotation only 10 : FlagAndAllAround (Flag And AllAround) - For welding annotation only

        :return: int
        """

        return self.com_object.AnchorSymbol

    @anchor_symbol.setter
    def anchor_symbol(self, value: int):
        """
        :param int value:
        """

        self.com_object.AnchorSymbol = value

    @property
    def head_symbol(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HeadSymbol() As CatSymbolType
                |     Returns or sets symbol type of head side.
                | 
                |     Example:
                |         This example retrieves the symbol type of head side on MyLeader drawing
                |         leader.
                | 
                |          oSymbol = MyLeader.HeadSymbol

        :return: int
        """

        return self.com_object.HeadSymbol

    @head_symbol.setter
    def head_symbol(self, value: int):
        """
        :param int value:
        """

        self.com_object.HeadSymbol = value

    @property
    def head_target(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HeadTarget() As CATBaseDispatch
                |     Returns or sets target element of head side.
                | 
                |     Example:
                |         This example retrieves the target element of head side on MyLeader
                |         drawing leader.
                | 
                |          oTarget = MyLeader.HeadTarget

        :return: AnyObject
        """

        return AnyObject(self.com_object.HeadTarget)

    @head_target.setter
    def head_target(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.HeadTarget = value

    @property
    def leaders(self) -> DrawingLeaders:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Leaders() As DrawingLeaders (Read Only)
                |     Returns the drawing leader collection of the drawing
                |     leader.
                | 
                |     Example:
                |         This example retrieves in LeaderCollection the collection of leaders of
                |         the Myleader drawing leader.
                | 
                |          Dim LeaderCollection As DrawingLeaders
                |          Set LeaderCollection = MyLeader.Leaders

        :return: DrawingLeaders
        """

        return DrawingLeaders(self.com_object.Leaders)

    @property
    def nb_interruption(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NbInterruption() As long (Read Only)
                |     Returns the number of interruptions of leader path.
                | 
                |     Example:
                |         This example retrieves the number of interruptions on MyLeader drawing
                |         leader.
                | 
                |          oNbInterruption = MyLeader.NbInterruption

        :return: int
        """

        return self.com_object.NbInterruption

    @property
    def nb_point(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NbPoint() As long (Read Only)
                |     Returns the number of points of leader path.
                | 
                |     Example:
                |         This example retrieves the number of points on MyLeader drawing
                |         leader.
                | 
                |          oNbPoint = MyLeader.NbPoint

        :return: int
        """

        return self.com_object.NbPoint

    def add_interruption(self, i_first_point_x: float, i_first_point_y: float, i_second_point_x: float, i_second_point_y: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub AddInterruption(double iFirstPointX,double iFirstPointY,double
                | iSecondPointX,double iSecondPointY)
                |     Add an interruption to an leader.
                | 
                |     Parameters:
                | 
                |         iFirstPointX
                |             X coordinates of first point. 
                |         iFirstPointY
                |             Y coordinates of first point. 
                |         iSecondPointX
                |             X coordinates of second point. 
                |         iSecondPointY
                |             Y coordinates of second point. 
                |         Example:
                |             This example adds an interruption to MyLeader.
                | 
                |              iFirstPointX = 10.
                |              iFirstPointY = 20.
                |              iSecondPointX = 20.
                |              iSecondPointY = 20.
                |              MyLeader.AddInterruption iFirstPointX, iFirstPointY,
                |              iSecondPointX, iSecondPointY

        :param float i_first_point_x:
        :param float i_first_point_y:
        :param float i_second_point_x:
        :param float i_second_point_y:
        :return: None
        """
        return self.com_object.AddInterruption(i_first_point_x, i_first_point_y, i_second_point_x, i_second_point_y)

    def add_point(self, i_num: int, i_x: float, i_y: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub AddPoint(long iNum,double iX,double iY)
                |     Add a point to an leader.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Point number. Point will be inserted at iNum+1 position.
                |             
                |         iX
                |             X coordinates of point to add. 
                |         iY
                |             Y coordinates of point to add. 
                |         Example:
                |             This example adds a point to MyLeader.
                | 
                |              iNum = 1
                |              iX = 10.
                |              iY = 20.
                |              MyLeader.AddPoint iNum, iX, iY

        :param int i_num:
        :param float i_x:
        :param float i_y:
        :return: None
        """
        return self.com_object.AddPoint(i_num, i_x, i_y)

    def get_interruptions(self, o_interruptions: tuple) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetInterruptions(CATSafeArrayVariant oInterruptions) As
                | long
                |     Get leader path.
                | 
                |     Parameters:
                | 
                |         oInterruptions
                |             List of interruptions coordinates (X1,Y1,X2,Y2,.....Xn,Yn).
                |             
                | 
                |     Returns:
                |         oNbInterruptions Number of interruptions. 
                |     Example:
                |         This example gets interruptions of MyLeader path.
                | 
                |          oNbInterruptions = MyLeader.GetInterruptions(oInterruptions)

        :param tuple o_interruptions:
        :return: int
        """
        return self.com_object.GetInterruptions(o_interruptions)

    def get_point(self, i_num: int, o_x: float, o_y: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetPoint(long iNum,double oX,double oY)
                |     Get leader point coordinates.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Point number. 
                |         oX
                |             X coordinates of point. 
                |         oY
                |             Y coordinates of point. 
                |         Example:
                |             This example gets a point to MyLeader.
                | 
                |              iNum = 1
                |              MyLeader.GetPoint(iNum, oX, oY)

        :param int i_num:
        :param float o_x:
        :param float o_y:
        :return: None
        """
        return self.com_object.GetPoint(i_num, o_x, o_y)

    def get_points(self, o_points: tuple) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetPoints(CATSafeArrayVariant oPoints) As long
                |     Get leader path.
                | 
                |     Parameters:
                | 
                |         oPoints
                |             List of points coordinates (X1,Y1,X2,Y2,.....Xn,Yn).
                |             
                | 
                |     Returns:
                |         oNbPoints Number of points. 
                |     Example:
                |         This example gets points of MyLeader path.
                | 
                |          oNbPoints = MyLeader.GetPoints(oPoints)

        :param tuple o_points:
        :return: int
        """
        return self.com_object.GetPoints(o_points)

    def modify_point(self, i_num: int, i_x: float, i_y: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub ModifyPoint(long iNum,double iX,double iY)
                |     Modify a point of an leader.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Point number to modify. 
                |         iX
                |             X coordinates of new point. 
                |         iY
                |             Y coordinates of new point. 
                |         Example:
                |             This example modifys a point to MyLeader.
                | 
                |              iNum = 1
                |              iX = -10.
                |              iY = -20.
                |              MyLeader.ModifyPoint iNum, iX, iY

        :param int i_num:
        :param float i_x:
        :param float i_y:
        :return: None
        """
        return self.com_object.ModifyPoint(i_num, i_x, i_y)

    def remove_interruption(self, i_num: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub RemoveInterruption(long iNum)
                |     Remove an interruption to an leader.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Interruption number to delete. 
                |             - If iNum equals to 0, all interruptions will be removed.
                |             
                |         Example:
                |             This example removes an interruption from
                |             MyLeader.
                | 
                |              iNum = 2
                |              MyLeader.RemoveInterruption iNum

        :param int i_num:
        :return: None
        """
        return self.com_object.RemoveInterruption(i_num)

    def remove_point(self, i_num: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub RemovePoint(long iNum)
                |     Remove a point from an leader.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Point number to delete. 
                |         Example:
                |             This example removes a point from MyLeader.
                | 
                |              iNum = 2
                |              MyLeader.RemovePoint iNum

        :param int i_num:
        :return: None
        """
        return self.com_object.RemovePoint(i_num)

    def __repr__(self):
        return f'DrawingLeader(name="{ self.name }")'
