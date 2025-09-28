"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.plane import Plane
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.mode.reference import Reference


class HybridShapePlaneEquation(Plane):

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
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneEquation
                | 
                | Plane define by an equation plane.
                | Role: Allows to access data of the plane feature created by its cartesian equation. Plane equation is Ax+By+Cz = D.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def a(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property A() As RealParam (Read Only)
                |     Gets A coefficient for plane equation.
                | 
                |     Parameters:
                | 
                |         oA
                |             A Coefficient of cartesian plane 
                | 
                |     See also:
                |         RealParam
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: RealParam
        """

        return RealParam(self.com_object.A)

    @property
    def b(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property B() As RealParam (Read Only)
                |     Gets B coefficient for plane equation.
                | 
                |     Parameters:
                | 
                |         oB
                |             B Coefficient of cartesian plane 
                | 
                |     See also:
                |         RealParam
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: RealParam
        """

        return RealParam(self.com_object.B)

    @property
    def c(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property C() As RealParam (Read Only)
                |     Gets C coefficient for plane equation.
                | 
                |     Parameters:
                | 
                |         oC
                |             C Coefficient of cartesian plane return value for CATScript
                |             applications, with (IDLRETVAL) function type 
                | 
                |     See also:
                |         RealParam
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: RealParam
        """

        return RealParam(self.com_object.C)

    @property
    def d(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property D() As Length (Read Only)
                |     Gets D coefficient for plane equation.
                | 
                |     Parameters:
                | 
                |         oD
                |             D Coefficient of cartesian plane 
                | 
                |     See also:
                |         Length
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Length
        """

        return Length(self.com_object.D)

    @property
    def ref_axis_system(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RefAxisSystem() As Reference
                |     Returns or Sets the reference Axis System for PlaneEquation
                |     feature.
                |     This data is not mandatory, if element is null, the absolute axis system is
                |     taken.
                |     When an element is given, X, Y and Z are considered in this Axis
                |     system.
                |     If reference point is not specified, X,Y and Z are measured from origin of
                |     this axis system.
                | 
                |     Example
                |     :
                |         This example retrieves in oRefAxis the reference Axis System for
                |         PlaneEquation feature.
                | 
                |          Dim oRefAxis As CATIAReference
                |          Set oRefAxis  = PlaneEquation.RefAxisSystem

        :return: Reference
        """

        return Reference(self.com_object.RefAxisSystem)

    @ref_axis_system.setter
    def ref_axis_system(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.RefAxisSystem = value

    def get_reference_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetReferencePoint() As Reference
                |     Gets the reference point.
                | 
                |     Parameters:
                | 
                |         oReferencePoint
                |             reference point

        :return: Reference
        """
        return Reference(self.com_object.GetReferencePoint())

    def set_reference_point(self, i_reference_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetReferencePoint(Reference iReferencePoint)
                |     Sets the reference point.
                | 
                |     Parameters:
                | 
                |         iReferencePoint
                |             reference point

        :param Reference i_reference_point:
        :return: None
        """
        return self.com_object.SetReferencePoint(i_reference_point.com_object)

    def __repr__(self):
        return f'HybridShapePlaneEquation(name="{ self.name }")'
