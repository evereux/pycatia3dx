"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimMathVector(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMathVector
                | 
                | Represents the Math Vector object.
                | 
                | Example:
                |     Given a SimMathAxis object with an attribute FirstDirection of type
                |     SimMathVector, you can retrieve SimMathVector object as
                |     following:
                | 
                |      Dim MyMathAxis As SimMathAxis
                |      ...
                |      Dim MyMathVector As SimMathVector
                |      Set MyMathVector = MyMathAxis.FirstDirection
                |      
                | 
                | Example in Python:
                |     Given a SimMathAxis object with an attribute FirstDirection of type
                |     SimMathVector, you can retrieve SimMathVector object as
                |     following:
                | 
                |      ...
                |      myMathVector = myMathAxis.FirstDirection
                |      
                | 
                | See also:
                |     SimMathAxis
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def x(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property X() As double
                |     Returns or sets the X value of the vector.

        :return: float
        """

        return self.com_object.X

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.com_object.X = value

    @property
    def y(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Y() As double
                |     Returns or sets the Y value of the vector.

        :return: float
        """

        return self.com_object.Y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.com_object.Y = value

    @property
    def z(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Z() As double
                |     Returns or sets the Z value of the vector. 

        :return: float
        """

        return self.com_object.Z

    @z.setter
    def z(self, value: float):
        """
        :param float value:
        """

        self.com_object.Z = value

    def __repr__(self):
        return f'SimMathVector(name="{ self.name }")'
