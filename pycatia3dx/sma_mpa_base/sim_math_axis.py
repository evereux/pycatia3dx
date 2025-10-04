"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_base.sim_math_point import SimMathPoint
from pycatia3dx.sma_mpa_base.sim_math_vector import SimMathVector


class SimMathAxis(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMathAxis
                | 
                | Represents the Math Axis object.
                | The SimMathAxis object is composed of normalized direction vectors and an
                | origin position. These form a valid axis with no zero length or co-linear
                | vectors.
                | 
                | Given a feature MyAxisSytem with an attribute AxisSystem of type SimMathAxis,
                | you can retrieve SimMathAxis object as following:
                | Example:
                | 
                |      Dim MyAxisSystem As SimAxisSystem
                |      ...
                |      Dim MyAxis As SimMathAxis
                |      Set MyAxis = MyAxisSystem.AxisSystem
                |      
                | 
                | Example in Python:
                | 
                |      ...
                |      myAxis = myAxisSystem.AxisSystem
                |      
                | 
                | You can return values by chaining properties. Given a feature MyAxisSytem with
                | an attribute AxisSystem of type SimMathAxis, you can chain properties as
                | following:
                | Example:
                | 
                |      Dim MyAxisSystem As SimAxisSystem
                |      ...
                |      MyX = MyAxisSystem.AxisSystem.FirstDirection.X
                |      
                | 
                | Example in Python:
                | 
                |      ...
                |      MyX = MyAxisSystem.AxisSystem.FirstDirection.X
                |      
                | 
                | You must use assignment to set values, and cannot set values by chaining
                | properties. Given a feature MyAxisSytem with an attribute AxisSystem of type
                | SimMathAxis, you can set values as following:
                | Example:
                | 
                |      Dim MyAxisSystem As SimAxisSystem
                |      ...
                |      Dim MyAxis As SimMathAxis
                |      Set MyAxis = MyAxisSystem.AxisSystem
                |      Dim MyDirection As SimMathVector
                |      Set MyDirection = MyAxis.FirstDirection
                |      MyDirection.X = 0.5
                |      ...
                |      MyAxis.FirstDirection = MyDirection
                |      MyAxisSystem.AxisSystem = MyAxis
                |      
                | 
                | Example in Python:
                | 
                |      ...
                |      MyAxis = MyAxisSystem.AxisSystem
                |      MyDirection = MyAxis.FirstDirection
                |      MyDirection.X = 0.5
                |      ...
                |      MyAxis.FirstDirection = MyDirection
                |      MyAxisSystem.AxisSystem = MyAxis
                |      
                | 
                | See also:
                |     SimAxisSystem, SimMathVector, SimMathPoint
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def first_direction(self) -> SimMathVector:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FirstDirection() As SimMathVector
                |     Returns or sets the first direction of the axis system.

        :return: SimMathVector
        """

        return SimMathVector(self.com_object.FirstDirection)

    @first_direction.setter
    def first_direction(self, value: SimMathVector):
        """
        :param SimMathVector value:
        """

        self.com_object.FirstDirection = value

    @property
    def origin(self) -> SimMathPoint:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Origin() As SimMathPoint
                |     Returns or sets the origin of the axis system.

        :return: SimMathPoint
        """

        return SimMathPoint(self.com_object.Origin)

    @origin.setter
    def origin(self, value: SimMathPoint):
        """
        :param SimMathPoint value:
        """

        self.com_object.Origin = value

    @property
    def second_direction(self) -> SimMathVector:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondDirection() As SimMathVector
                |     Returns or sets the second direction of the axis system.

        :return: SimMathVector
        """

        return SimMathVector(self.com_object.SecondDirection)

    @second_direction.setter
    def second_direction(self, value: SimMathVector):
        """
        :param SimMathVector value:
        """

        self.com_object.SecondDirection = value

    @property
    def third_direction(self) -> SimMathVector:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThirdDirection() As SimMathVector
                |     Returns or Sets the third direction of the axis system. 

        :return: SimMathVector
        """

        return SimMathVector(self.com_object.ThirdDirection)

    @third_direction.setter
    def third_direction(self, value: SimMathVector):
        """
        :param SimMathVector value:
        """

        self.com_object.ThirdDirection = value

    def __repr__(self):
        return f'SimMathAxis(name="{ self.name }")'
