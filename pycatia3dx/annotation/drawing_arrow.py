"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DrawingArrow(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingArrow
                | 
                | Represents a drawing arrow in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

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
                |         This example retrieves the symbol type of head side on MyArrow drawing
                |         arrow.
                | 
                |          oSymbol = MyArrow.HeadSymbol

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
                |         This example retrieves the target element of head side on MyArrow
                |         drawing arrow.
                | 
                |          oTarget = MyArrow.HeadTarget

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
    def nb_interruption(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NbInterruption() As long (Read Only)
                |     Returns the number of interruptions of arrow path.
                | 
                |     Example:
                |         This example retrieves the number of interruptions on MyArrow drawing
                |         arrow.
                | 
                |          oNbInterruption = MyArrow.NbInterruption

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
                |     Returns the number of points of arrow path.
                | 
                |     Example:
                |         This example retrieves the number of points on MyArrow drawing
                |         arrow.
                | 
                |          oNbPoint = MyArrow.NbPoint

        :return: int
        """

        return self.com_object.NbPoint

    @property
    def scale_on_extremities(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScaleOnExtremities() As boolean
                |     Returns or sets the scale on extremities mode.
                | 
                |     Example:
                |         This example retrieves the target element of head side on MyArrow
                |         drawing arrow.
                | 
                |          oScaleOnExtremities = MyArrow.ScaleOnExtremities

        :return: bool
        """

        return self.com_object.ScaleOnExtremities

    @scale_on_extremities.setter
    def scale_on_extremities(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ScaleOnExtremities = value

    @property
    def tail_symbol(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TailSymbol() As CatSymbolType
                |     Returns or sets symbol type of tail side.
                | 
                |     Example:
                |         This example retrieves the symbol type of tail side on MyArrow drawing
                |         arrow.
                | 
                |          oSymbol = MyArrow.TailSymbol

        :return: int
        """

        return self.com_object.TailSymbol

    @tail_symbol.setter
    def tail_symbol(self, value: int):
        """
        :param int value:
        """

        self.com_object.TailSymbol = value

    @property
    def tail_target(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TailTarget() As CATBaseDispatch
                |     Returns or sets target element of tail side.
                | 
                |     Example:
                |         This example retrieves the target element of tail side on MyArrow
                |         drawing arrow.
                | 
                |          oTarget = MyArrow.TailTarget

        :return: AnyObject
        """

        return AnyObject(self.com_object.TailTarget)

    @tail_target.setter
    def tail_target(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.TailTarget = value

    def add_interruption(self, i_first_point_x: float, i_first_point_y: float, i_second_point_x: float,
                         i_second_point_y: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddInterruption(double iFirstPointX,double iFirstPointY,double
                | iSecondPointX,double iSecondPointY)
                |     Add an interruption to an arrow.
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
                |             This example adds an interruption to MyArrow.
                | 
                |              iFirstPointX = 10.
                |              iFirstPointY = 20.
                |              iSecondPointX = 20.
                |              iSecondPointY = 20.
                |              MyArrow.AddInterruption iFirstPointX, iFirstPointY, iSecondPointX,
                |              iSecondPointY

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

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddPoint(long iNum,double iX,double iY)
                |     Add a point to an arrow.
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
                |             This example adds a point to MyArrow.
                | 
                |              iNum = 1
                |              iX = 10.
                |              iY = 20.
                |              MyArrow.AddPoint iNum, iX, iY

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

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInterruptions(CATSafeArrayVariant oInterruptions) As
                | long
                |     Get arrow path.
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
                |         This example gets interruptions of MyArrow path.
                | 
                |          oNbInterruptions = MyArrow.GetInterruptions(oInterruptions)

        :param tuple o_interruptions:
        :return: int
        """
        return self.com_object.GetInterruptions(o_interruptions)

    def get_point(self, i_num: int, o_x: float, o_y: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPoint(long iNum,double oX,double oY)
                |     Get arrow point coordinates.
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
                |             This example gets a point to MyArrow.
                | 
                |              iNum = 1
                |              MyArrow.GetPoint(iNum, oX, oY)

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

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPoints(CATSafeArrayVariant oPoints) As long
                |     Get arrow path.
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
                |         This example gets points of MyArrow path.
                | 
                |          oNbPoints = MyArrow.GetPoints(oPoints)

        :param tuple o_points:
        :return: int
        """
        return self.com_object.GetPoints(o_points)

    def modify_point(self, i_num: int, i_x: float, i_y: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ModifyPoint(long iNum,double iX,double iY)
                |     Modify a point of an Arrow.
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
                |             This example modifys a point to MyArrow.
                | 
                |              iNum = 1
                |              iX = -10.
                |              iY = -20.
                |              MyArrow.ModifyPoint iNum, iX, iY

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

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveInterruption(long iNum)
                |     Remove an interruption to an arrow.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Interruption number to delete. 
                |             - If iNum equals to 0, all interruptions will be removed.
                |             
                |         Example:
                |             This example removes an interruption from MyArrow.
                | 
                |              iNum = 2
                |              MyArrow.RemoveInterruption iNum

        :param int i_num:
        :return: None
        """
        return self.com_object.RemoveInterruption(i_num)

    def remove_point(self, i_num: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemovePoint(long iNum)
                |     Remove a point from an arrow.
                | 
                |     Parameters:
                | 
                |         iNum
                |             Point number to delete. 
                |         Example:
                |             This example removes a point from MyArrow.
                | 
                |              iNum = 2
                |              MyArrow.RemovePoint iNum

        :param int i_num:
        :return: None
        """
        return self.com_object.RemovePoint(i_num)

    def __repr__(self):
        return f'DrawingArrow(name="{self.name}")'
