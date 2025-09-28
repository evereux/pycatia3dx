"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeDirection(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapeDirection
                | 
                | Represents the hybrid shape direction feature object.
                | Role: To access the data of the hybrid shape direction feature object. A
                | direction can be specified using:
                | 
                |     A line: the direction is tangent to the line
                |     A plane: the direction is normal to the plane
                |     Its components
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeDirection
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def object(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Object() As Reference
                |     Returns or sets the object that specifies the direction.
                |     This object can be a line or a plane.
                | 
                |     Parameters:
                | 
                |         oObject
                |             The object (a line or a plane) that specifies the
                |             direction
                | 
                |             Sub-element(s) supported (see Boundary object):
                |             RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge or
                |             RectilinearMonoDimFeatEdge.

        :return: Reference
        """

        return Reference(self.com_object.Object)

    @object.setter
    def object(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Object = value

    @property
    def ref_axis_system(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RefAxisSystem() As Reference
                |     Returns or Sets the reference Axis System for Direction
                |     feature.
                |     This data is not mandatory, if element is null, the absolute axis system is
                |     taken.
                |     When an element is given, X, Y and Z are considered in this Axis system.
                |     
                | Example
                | :
                |     This example retrieves in oRefAxis the reference Axis System for Direction
                |     feature.
                | 
                |      Dim oRefAxis As CATIAReference
                |      Set oRefAxis  = Direction.RefAxisSystem

        :return: Reference
        """

        return Reference(self.com_object.RefAxisSystem)

    @ref_axis_system.setter
    def ref_axis_system(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.RefAxisSystem = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Type() As long (Read Only)
                |     Returns the direction type.
                |     Legal value: The direction type can be:
                | 
                |     0
                |         The direction is specified using an object (a line or a plane). In the
                |         case of a plane, the direction is the normal to the
                |         plane
                |     1
                |         The direction is specified using its components

        :return: int
        """

        return self.com_object.Type

    def direction_specification(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func DirectionSpecification() As long
                |     Queries the direction specification status.
                | 
                |     Parameters:
                | 
                |         oDir
                |             direction specification = 0 : Direction is not specified. = 1 : Direction is specified and is valid. = -1 : Direction is specified but is not valid.

        :return: int
        """
        return self.com_object.DirectionSpecification()

    def get_x(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetX() As RealParam
                |     Returns the direction X component. This method succeeds only when direction
                |     is specified using components. It fails when direction is specified using a
                |     geometrical element i.e Line, Plane. In such cases use GetXVal method
                |     instead.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The direction X component

        :return: RealParam
        """
        return RealParam(self.com_object.GetX())

    def get_x_val(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetXVal() As double
                |     Returns the direction X component as Double. This method succeeds
                |     irrespective of the way direction is specified.
                | 
                |     Parameters:
                | 
                |         oX
                |             The direction X component

        :return: float
        """
        return self.com_object.GetXVal()

    def get_y(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetY() As RealParam
                |     Returns the direction Y component. This method succeeds only when direction
                |     is specified using components. It fails when direction is specified using a
                |     geometrical element i.e Line, Plane. In such cases use GetYVal method
                |     instead.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The direction Y component

        :return: RealParam
        """
        return RealParam(self.com_object.GetY())

    def get_y_val(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetYVal() As double
                |     Returns the direction Y component as Double.This method succeeds
                |     irrespective of the way direction is specified.
                | 
                |     Parameters:
                | 
                |         oY
                |             The direction Y component

        :return: float
        """
        return self.com_object.GetYVal()

    def get_z(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetZ() As RealParam
                |     Returns the direction Z component. This method succeeds only when direction
                |     is specified using components. It fails when direction is specified using a
                |     geometrical element i.e Line, Plane. In such cases use GetZVal method
                |     instead.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The direction Z component

        :return: RealParam
        """
        return RealParam(self.com_object.GetZ())

    def get_z_val(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetZVal() As double
                |     Returns the direction Z component as Double.This method succeeds
                |     irrespective of the way direction is specified.
                | 
                |     Parameters:
                | 
                |         oZ
                |             The direction Z component.

        :return: float
        """
        return self.com_object.GetZVal()

    def __repr__(self):
        return f'HybridShapeDirection(name="{ self.name }")'
