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


class SimMathPlane(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMathPlane
                | 
                | Represents the Math Plane object.
                | The SimMathPlane object is composed of normalized in-plane direction vectors
                | and an origin position. These form a valid plane definition with no zero length
                | or co-linear vectors.
                | 
                | Given a SimMeshedBolt object with an attribute Plane of type SimMathPlane, you
                | can retrieve SimMathPlane object as following:
                | Example:
                | 
                |      Dim MyMeshedBolt As SimMeshedBolt
                |      ...
                |      Dim MyMathPlane As SimMathPlane
                |      Set MyMathPlane = MyMeshedBolt.Plane
                |      
                | 
                | Example in Python:
                | 
                |      ...
                |      myMathPlane = myMeshedBolt.Plane
                |      
                | 
                | You can return values by chaining properties. Given a feature SimMeshedBolt
                | with an attribute Plane of type SimMathPlane, you can chain properties as
                | following:
                | Example:
                | 
                |      Dim MyMeshedBolt As SimMeshedBolt
                |      ...
                |      MyX = MyMeshedBolt.Plane.FirstDirection.X
                |      
                | 
                | Example in Python:
                | 
                |      ...
                |      MyX = MyMeshedBolt.Plane.FirstDirection.X
                |      
                | 
                | You must use assignment to set values, and cannot set values by chaining
                | properties. Given a feature SimMeshedBolt with an attribute Plane of type
                | SimMathPlane, you can set values as following:
                | Example:
                | 
                |      Dim MyMeshedBolt As SimMeshedBolt
                |      ...
                |      Dim MyMathPlane As SimMathPlane
                |      Set MyMathPlane = MyMeshedBolt.Plane
                |      Dim MyDirection As SimMathVector
                |      Set MyDirection = MyMathPlane.FirstDirection
                |      MyDirection.X = 0.5
                |      ...
                |      MyMathPlane.FirstDirection = MyDirection
                |      MyMeshedBolt.Plane = MyMathPlane
                |      
                | 
                | Example in Python:
                | 
                |      ...
                |      MyMathPlane = MyMeshedBolt.Plane
                |      MyDirection = MyMathPlane.FirstDirection
                |      MyDirection.X = 0.5
                |      ...
                |      MyMathPlane.FirstDirection = MyDirection
                |      MyMeshedBolt.Plane = MyMathPlane
                |      
                | 
                | See also:
                |     SimMeshedBolt, SimMathVector, SimMathPoint
    
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
                |     Returns or sets the first direction of the plane.

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
                |     Returns or sets the origin of the plane.

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
                |     Returns or sets the second direction of the plane. 

        :return: SimMathVector
        """

        return SimMathVector(self.com_object.SecondDirection)

    @second_direction.setter
    def second_direction(self, value: SimMathVector):
        """
        :param SimMathVector value:
        """

        self.com_object.SecondDirection = value

    def __repr__(self):
        return f'SimMathPlane(name="{ self.name }")'
