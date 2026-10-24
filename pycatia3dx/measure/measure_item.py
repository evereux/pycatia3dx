"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx import CATMeasurableModeOfCalc
from pycatia3dx import CATOpnsMeasureEdgeType
from pycatia3dx import CATOpnsMeasureSurfaceType
from pycatia3dx import CATResultCalcType
from pycatia3dx import CATOpnsMeasureItemType
from pycatia3dx import CATScriptLanguage
from pycatia3dx.system.any_object import AnyObject


class MeasureItem(AnyObject):
    """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MeasureItem
                | 
                | Represents the MeasureItem.
                | The MeasureItem is the measurement of the selections on the
                | object(s).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_angle(self) -> float:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAngle() As double
                |     Retrieves the angle of the circle or the cone.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             The angle 
                | 
                |     Example:
                | 
                |            This example retrieves the Angle of theMeasureItem
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theAngle As Double
                |              theAngle = theMeasureItem.GetAngle

        :return: float
        """
        return self.com_object.GetAngle()

    def get_area(self) -> float:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetArea() As double
                |     Retrieves the wet area of the volume or the surface.
                | 
                |     Parameters:
                | 
                |         oArea
                |             The area 
                | 
                |     Example:
                | 
                |            This example retrieves the wet area of theMeasureItem
                |            measure.
                |            The area unit given by oArea is m²
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theArea As Double
                |              theArea = theMeasureItem.GetArea

        :return: float
        """
        return self.com_object.GetArea()

    def get_axis(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAxis(double oXVector,double oYVector,double oZVector)
                |     Retrieves the axis vector of the cylinder, cone, or
                |     circle.
                | 
                |     Parameters:
                | 
                |         oXVector
                |             The X coordinate of the vector 
                |         oYVector
                |             The Y coordinate of the vector 
                |         oZVector
                |             The Z coordinate of the vector 
                | 
                |     Example:
                | 
                |            This example retrieves the axis vector of theMeasureItem
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theXVector As Double
                |              Dim theYVector As Double
                |              Dim theZVector As Double
                |              theMeasureItem.GetAxis theXVector, theYVector,
                |              theZVector

        :return: tuple
        """
        return self.com_object.GetAxis()

    def get_axis_system_from_measure(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948)
                | Sub GetAxisSystemFromMeasure(CATSafeArrayVariant
                | oAxisPositioning)
                |     Get the position of the axis system of the object with respect to the
                |     absolute axis system. This position corresponds to the product positioning
                |     matrix. All coordinates are internally computed using the axis system of the
                |     object. To provide these coordinates with respect to absolute axis system, it
                |     is required to know the position of the axis system of the
                |     object.
                |
                |     Parameters:
                |
                |         ioAxisPosition
                |             The information of the axis system with respect to the product
                |             coordinate system:
                |
                |                 iAxisPositioning(0) is the X coordinate of the origin of the
                |                 axis system
                |                 iAxisPositioning(1) is the Y coordinate of the origin of the
                |                 axis system
                |                 iAxisPositioning(2) is the Z coordinate of the origin of the
                |                 axis system
                |                 iAxisPositioning(3) is the X coordinate of the first direction
                |                 of the axis system
                |                 iAxisPositioning(4) is the Y coordinate of the first direction
                |                 of the axis system
                |                 iAxisPositioning(5) is the Z coordinate of the first direction
                |                 of the axis system
                |                 iAxisPositioning(6) is the X coordinate of the second direction
                |                 of the axis system
                |                 iAxisPositioning(7) is the Y coordinate of the second direction
                |                 of the axis system
                |                 iAxisPositioning(8) is the Z coordinate of the second direction
                |                 of the axis system
                |                 iAxisPositioning(9) is the X coordinate of the third direction
                |                 of the axis system
                |                 iAxisPositioning(10) is the Y coordinate of the third direction
                |                 of the axis system
                |                 iAxisPositioning(11) is the Z coordinate of the third direction
                |                 of the axis system
                |
                |     Example:
                |
                |            This example get the axis system of theMeasureItem
                |            computation.
                |
                |
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasure(theSelection)
                |              Dim theAxisPositioning(11)
                |              theMeasureItem.GetAxisSystemFromMeasure
                |              theAxisPositioning

        :return: tuple
        """
        # todo: this isn't working - see test_get_axis_system_from_measure
        self.application.logger.warning("Tests at the moment show that this is broken.")
        return self.com_object.GetAxisSystemFromMeasure()
        # vba_function_name = 'get_axis_system_from_measure'
        # vba_code = """
        # Public Function get_axis_system_from_measure(measure_item)
        #     Dim oAxisPositioning (11)
        #     measure_item.GetAxisSystemFromMeasure oAxisPositioning
        #     get_axis_system_from_measure = oAxisPositioning
        # End Function
        # """
        #
        # result = self.application.system_service.evaluate(
        #     vba_code,
        #     CATScriptLanguage.CATVBScriptLanguage,
        #     vba_function_name,
        #     [self.com_object]
        # )
        #
        # return result

    def get_c_of_g(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCOfG(double oXCOfG,double oYCOfG,double oZCOfG)
                |     Retrieves the position of the center of gravity of a
                |     surface.
                | 
                |     Parameters:
                | 
                |         oXCOfG
                |             The X coordinate of the center of gravity 
                |         oYCOfG
                |             The Y coordinate of the center of gravity 
                |         oZCOfG
                |             The Z coordinate of the center of gravity 
                | 
                |     Example:
                | 
                |            This example retrieves the position of the center of gravity of
                |            theMeasureItem measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theXCOfG As Double
                |              Dim theYCOfG As Double
                |              Dim theZCOfG As Double
                |              theMeasureItem.GetCOG theXCOfG, theYCOfG,
                |              theZCOfG

        :return: tuple
        """
        return self.com_object.GetCOfG()

    def get_center(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCenter(double oXCenter,double oYCenter,double oZCenter)
                |     Retrieves the position of the center of the circle or the
                |     sphere.
                | 
                |     Parameters:
                | 
                |         oXCenter
                |             The X coordinate of the center 
                |         oYCenter
                |             The Y coordinate of the center 
                |         oZCenter
                |             The Z coordinate of the center 
                | 
                |     Example:
                | 
                |            This example retrieves the position of the center of theMeasureItem
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theXCenter As Double
                |              Dim theYCenter As Double
                |              Dim theZCenter As Double
                |              theMeasureItem.GetCenter theXCenter, theYCenter,
                |              theZCenter

        :return: tuple
        """
        return self.com_object.GetCenter()

    def get_computation_mode(self) -> CATMeasurableModeOfCalc:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetComputationMode(CATMeasurableModeOfCalc
                | oComputationMode)
                |     Get the mode of computation of the object. The computation mode of the
                |     object can be: Exact, Approximate or ExactElseApprox.
                | 
                |     Parameters:
                | 
                |         oComputationMode
                |             The mode of computation 
                | 
                |     Example:
                | 
                |            This example get the computation mode of
                |            theMeasureItem.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theComputationType As CATMeasurableModeOfCalc
                |              theComputationType = theMeasureItem.GetComputationMode

        :return: CATMeasurableModeOfCalc
        """
        return self.com_object.GetComputationMode()

    def get_curve_points(self) -> tuple | None:
        """
        .. note::

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948)
                | Sub GetCurvePoints(CATSafeArrayVariant ioStartPoint,CATSafeArrayVariant
                | ioMidPoint,CATSafeArrayVariant ioEndPoint)
                |     Retrieves the characteristic points of the curve : the start point, the middle point and the end point.
                |
                |     Parameters:
                |
                |         ioStartPoint
                |             The information of the start point of the curve with respect to the
                |             product coordinate system:
                |
                |                 ioStartPoint(0) is the X coordinate of the startpoint of the
                |                 curve
                |                 ioStartPoint(1) is the Y coordinate of the startpoint of the
                |                 curve
                |                 ioStartPoint(2) is the Z coordinate of the startpoint of the
                |                 curve
                |
                |         ioMidPoint
                |             The information of the middle point of the curve with respect to
                |             the product coordinate system:
                |
                |                 oCoordinates(0) is the X coordinate of the midpoint of the
                |                 curve
                |                 oCoordinates(1) is the Y coordinate of the midpoint of the
                |                 curve
                |                 oCoordinates(2) is the Z coordinate of the midpoint of the
                |                 curve
                |
                |         ioEndPoint
                |             The information of the end point of the curve with respect to the
                |             product coordinate system:
                |
                |                 oCoordinates(0) is the X coordinate of the endpoint of the
                |                 curve
                |                 oCoordinates(1) is the Y coordinate of the endpoint of the
                |                 curve
                |                 oCoordinates(2) is the Z coordinate of the endpoint of the
                |                 curve
                |
                |     Example:
                |
                |            This example retrieves the characteristic points of the curve of
                |            theMeasureItem measure.
                |
                |
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As Measureitem
                |              Set theMeasureItem = theMeasureService.GetMeasure(theSelection)
                |              Dim theStartPoint(2)
                |              Dim theMidPoint(2)
                |              Dim theEndPoint(2)
                |              theMeasureItem.GetPoints theStartPoint, theMidPoint, theEndPoint

        :return: tuple(start_point: tuple, mid_point: tuple, end_point: tuple)
        """
        vba_function_name = 'get_curve_points'
        vba_code = """
        Public Function get_curve_points(measure_item)
            Dim theStartPoint(2)
            Dim theMidPoint(2)
            Dim theEndPoint(2)
            measure_item.GetCurvePoints theStartPoint, theMidPoint, theEndPoint
            Dim CurvePoints(2) 
            CurvePoints(0) = theStartPoint
            CurvePoints(1) = theMidPoint
            CurvePoints(2) = theEndPoint
            get_curve_points = CurvePoints
        End Function
        """

        result = self.application.system_service.evaluate(
            vba_code,
            CATScriptLanguage.CATVBScriptLanguage,
            vba_function_name,
            [self.com_object]
        )
        if isinstance(result, tuple):
            return result
        return None

    def get_direction(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDirection(double oXVector,double oYVector,double
                | oZVector)
                |     Retrieves the direction of the line.
                | 
                |     Parameters:
                | 
                |         oXVector
                |             The X coordinate of the vector 
                |         oYVector
                |             The Y coordinate of the vector 
                |         oZVector
                |             The Z coordinate of the vector 
                | 
                |     Example:
                | 
                |            This example retrieves the direction of the line of theMeasureItem
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theXVector As Double
                |              Dim theYVector As Double
                |              Dim theZVector As Double
                |              theMeasureItem.GetDirection theXVector, theYVector,
                |              theZVector

        :return: tuple
        """
        return self.com_object.GetDirection()

    def get_length(self) -> float:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLength() As double
                |     Retrieves the Length of the curve.
                | 
                |     Parameters:
                | 
                |         oLength
                |             The length 
                | 
                |     Example:
                | 
                |            This example retrieves the Length of theMeasureItem
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theLength As Double
                |              theLength = theMeasureItem.GetLength

        :return: float
        """
        return self.com_object.GetLength()

    def get_measure_edge_type(self) -> CATOpnsMeasureEdgeType:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMeasureEdgeType() As CATOpnsMeasureEdgeType
                |     Get the Measure Edge Type.
                | 
                |     Parameters:
                | 
                |         oEdgeType
                |             The Measure Edge Type The Measure Edge Type can be:
                |             catOpnsLineEdge, catOpnsArcEdge, catOpnsCurveEdge, catOpnsEllipseEdge,
                |             catOpnsParabolaEdge, catOpnsHyperbolaEdge, catOpnsAxisEdge, catOpnsUnknownEdge
                |             @see CATOpnsMeasureEdgeType 
                | 
                |     Example:
                | 
                |            This example get the measure edge type of
                |            theMeasureItem.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theMeasureEdgeType
                |              Set theMeasureEdgeType = GetMeasureEdgeType.GetMeasureEdgeType

        :return: CATOpnsMeasureEdgeType
        """
        return self.com_object.GetMeasureEdgeType()

    def get_measure_item_type(self) -> CATOpnsMeasureItemType:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMeasureItemType(CATOpnsMeasureItemType
                | oMeasureItemType)
                |     Get the Measure Item Type.
                | 
                |     Parameters:
                | 
                |         iMeasureItemType
                |             The Measure Item Type The Measure Item Type can be:
                |             catOpnsPointItem, catOpnsEdgeItem, catOpnsSurfaceItem, catOpnsVolumeItem,
                |             catOpnsComplexItem, catOpnsUnknownItem, catOpnsNotValid, catOpnsThicknessItem,
                |             catOpnsSurface2DItem, catOpnsAngle3PtsItem. @see CATOpnsMeasureItemType
                |             
                | 
                |     Example:
                | 
                |            This example get the measure item type of
                |            theMeasureItem.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theMeasureItemType
                |              Set theMeasureItemType = theMeasureItem.GetMeasureItemType

        :return: CATOpnsMeasureItemType
        """
        return self.com_object.GetMeasureItemType()

    def get_measure_surface_type(self) -> CATOpnsMeasureSurfaceType:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMeasureSurfaceType() As CATOpnsMeasureSurfaceType
                |     Get the Measure Surface Type.
                | 
                |     Parameters:
                | 
                |         oSurfaceType
                |             The Measure Surface Type The Measure Surface Type can be:
                |             catOpnsPlaneSurface, catOpnsCylinderSurface, catOpnsSphereSurface,
                |             catOpnsTorusSurface, catOpnsConeSurface, catOpnsUnknownSurface
                |             
                | 
                |     See also:
                |     Example:
                | 
                |            This example get the measure surface type of
                |            theMeasureItem.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theMeasureSurfaceType
                |              Set theMeasureSurfaceType = GetMeasureSurfaceType.GetMeasureSurfaceType

        :return: CATOpnsMeasureSurfaceType
        """
        return self.com_object.GetMeasureSurfaceType()

    def get_origin(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetOrigin(double oXOrigin,double oYOrigin,double oZOrigin)
                |     Retrieves the position of the origin of the line.
                | 
                |     Parameters:
                | 
                |         oXOrigin
                |             The X coordinate of the origin 
                |         oYOrigin
                |             The Y coordinate of the origin 
                |         oZOrigin
                |             The Z coordinate of the origin 
                | 
                |     Example:
                | 
                |            This example retrieves the position of the origin of theMeasureItem
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theXOrigin As Double
                |              Dim theYOrigin As Double
                |              Dim theZOrigin As Double
                |              theMeasureItem.GetOrigin theXOrigin, theYOrigin,
                |              theZOrigin

        :return: tuple
        """
        # todo: check this method, does it require system service?
        return self.com_object.GetOrigin()

    def get_perimeter(self) -> float:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPerimeter() As double
                |     Retrieves the perimeter of the surface.
                | 
                |     Parameters:
                | 
                |         oPerimeter
                |             The perimeter 
                | 
                |     Example:
                | 
                |            This example retrieves the area of theMeasureItem
                |            measure.
                |            The area unit given by oArea is m²
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim thePerimeter As Double
                |              thePerimeter = theMeasureItem.GetPerimeter

        :return: float
        """
        return self.com_object.GetPerimeter()

    def get_plane(self) -> tuple | None:
        """
        .. note::

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948)
                | Sub GetPlane(CATSafeArrayVariant ioPlane)
                |     Retrieves informations of the plane.
                |
                |     Parameters:
                |
                |         ioPlane
                |             The informations of the plane with respect to the product
                |             coordinate system:
                |
                |                 ioPlane(0) is the X coordinate of the origin
                |                 ioPlane(1) is the Y coordinate of the origin
                |                 ioPlane(2) is the Z coordinate of the origin
                |                 ioPlane(3) is the X coordinate of the first direction of the
                |                 plane
                |                 ioPlane(4) is the Y coordinate of the first direction of the
                |                 plane
                |                 ioPlane(5) is the Z coordinate of the first direction of the
                |                 plane
                |                 ioPlane(6) is the X coordinate of the second direction of the
                |                 plane
                |                 ioPlane(7) is the Y coordinate of the second direction of the
                |                 plane
                |                 ioPlane(8) is the Z coordinate of the second direction of the
                |                 plane
                |
                |     Example:
                |
                |            This example retrieves informations of the plane of theMeasureItem
                |            measure.
                |
                |
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim thePlane(8)
                |              theMeasureItem.GetPlane thePlane

        :return: tuple
        """
        vba_function_name = 'get_plane'
        vba_code = """
        Public Function get_plane(measure_item)
            Dim ioPlane (8)
            measure_item.GetPlane ioPlane
            get_plane = ioPlane
        End Function
        """

        result = self.application.system_service.evaluate(
            vba_code,
            CATScriptLanguage.CATVBScriptLanguage,
            vba_function_name,
            [self.com_object]
        )

        if isinstance(result, tuple):
            return result
        return None

    def get_point(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPoint(double oXPoint,double oYPoint,double oZPoint)
                |     Retrieves the position of the point.
                | 
                |     Parameters:
                | 
                |         oXPoint
                |             The X coordinate of the point 
                |         oYPoint
                |             The Y coordinate of the point 
                |         oZPoint
                |             The Z coordinate of the point 
                | 
                |     Example:
                | 
                |            This example retrieves the position of theMeasureItem
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theXPoint As Double
                |              Dim theYPoint As Double
                |              Dim theZPoint As Double
                |              theMeasureItem.GetPoint theXPoint, theYPoint,
                |              theZPoint

        :return: tuple
        """
        return self.com_object.GetPoint()

    def get_points(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPoints(double oXStartPoint,double oYStartPoint,double
                | oZStartPoint,double oXEndPoint,double oYEndPoint,double
                | oZEndPoint)
                |     Retrieves the position of the two limit points on the axis of the cylinder
                |     or cone. The distance between these points fit with the height of the cylinder
                |     or cone.
                | 
                |     Parameters:
                | 
                |         oXStartPoint
                |             The X coordinate of the start point 
                |         oYStartPoint
                |             The Y coordinate of the start point 
                |         oZStartPoint
                |             The Z coordinate of the start point 
                |         oXEndPoint
                |             The X coordinate of the end point 
                |         oYEndPoint
                |             The Y coordinate of the end point 
                |         oZEndPoint
                |             The Z coordinate of the end point 
                | 
                |     Example:
                | 
                |            This example retrieves the position the two limit points on the axis
                |            of theMeasureItem measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureItem")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theXStartPoint As Double
                |              Dim theYStartPoint As Double
                |              Dim theZStartPoint As Double
                |              Dim theXEndPoint As Double
                |              Dim theYEndPoint As Double
                |              Dim theZEndPoint As Double
                |              theMeasureItem.GetPoints theXStartPoint, theYStartPoint,
                |              theZStartPoint, theXEndPoint, theYEndPoint,
                |              theZEndPoint

        :return: tuple
        """
        # todo: see test_get_points
        self.application.logger.warning('Tests at the moment show that this is broken.')
        return self.com_object.GetPoints()

        # vba_function_name = 'get_points'
        # vba_code = """
        #        Public Function get_points(measure_item)
        #            Dim theXStartPoint As Double
        #            Dim theYStartPoint As Double
        #            Dim theZStartPoint As Double
        #            Dim theXEndPoint As Double
        #            Dim theYEndPoint As Double
        #            Dim theZEndPoint As Double
        #            measure_item.GetPoints theXStartPoint, theYStartPoint, theZStartPoint, theXEndPoint, theYEndPoint, theZEndPoint
        #            ' Dim Points(5)
        #            ' Points(0) = theXStartPoint
        #            ' Points(1) = theYStartPoint
        #            ' Points(2) = theZStartPoint
        #            ' Points(3) = theXEndPoint
        #            ' Points(4) = theYEndPoint
        #            ' Points(5) = theZEndPoint
        #            ' get_points = Points
        #        End Function
        #        """
        #
        # result = self.application.system_service.evaluate(
        #     vba_code,
        #     CATScriptLanguage.CATVBScriptLanguage,
        #     vba_function_name,
        #     [self.com_object]
        # )
        #
        # return result

    def get_radius(self) -> float:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRadius() As double
                |     Retrieves the radius of the circle or the sphere.
                | 
                |     Parameters:
                | 
                |         oRadius
                |             The radius 
                | 
                |     Example:
                | 
                |            This example retrieves the Radius of theMeasureItem
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theRadius As Double
                |              theRadius = theMeasureItem.GetRadius

        :return: float
        """
        return self.com_object.GetRadius()

    def get_result_computation_type(self) -> CATResultCalcType:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetResultComputationType() As CATResultCalcType
                |     Get the resulting type of computation of the object. The resulting type of
                |     the object can be: Exact, Approximate or Mixed.
                | 
                |     Returns:
                |         The resulting type In case of measures item, this method can be called
                |         after GetMeasureItem. 
                |     Example:
                | 
                |            This example get the computation mode of
                |            theMeasureItem.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theComputationType As CATResultCalcType
                |              theComputationType = theMeasureItem.GetResultComputationType

        :return: CATResultCalcType
        """
        # todo: see test_get_result_computation_type
        self.application.logger.warning('Tests at the moment show that this is broken.')
        return self.com_object.GetResultComputationType()

    def get_selection(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948)
                | Sub GetSelection(CATSafeArrayVariant oSelections)
                |     Get the selected objects of the measure Item.
                |
                |     Parameters:
                |
                |         oSelections
                |             The set of the selected objects
                |
                |     Example:
                |
                |            This example get the selected objects of
                |            theMeasureItem.
                |
                |
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theSelection
                |              theSelection = theMeasureItem.GetSelection

        :return: tuple
        """
        # todo: see test_get_selection
        self.application.logger.warning('Tests at the moment show that this is broken.')
        return self.com_object.GetSelection()
        # vba_function_name = 'get_selection'
        # vba_code = """
        # Public Function get_selection(measure_item)
        #     Dim the_selection
        #     the_selection = measure_item.GetSelection
        #     get_selection = the_selection
        # End Function
        # """
        #
        # result = self.application.system_service.evaluate(
        #     vba_code,
        #     CATScriptLanguage.CATVBScriptLanguage,
        #     vba_function_name,
        #     [self.com_object]
        # )
        #
        # return result

    def get_volume(self) -> float:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetVolume() As double
                |     Retrieves the volume.
                | 
                |     Parameters:
                | 
                |         oVolume
                |             The volume 
                | 
                |     Example:
                | 
                |            This example retrieves the volume of theMeasureItem
                |            measure.
                |            The area unit given by oArea is m^3
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theVolume As Double
                |              theVolume = theMeasureItem.GetVolume

        :return: float
        """
        return self.com_object.GetVolume()

    def get_volume_area_c_of_g(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetVolume_Area_COfG(double oVolume,double oArea,double oXCOfG,double
                | oYCOfG,double oZCOfG)
                |     Retrieves the volume, the wet area and the center of gravity of the volume.
                |     All Units are MKS units (mm, m2 and m3)
                | 
                |     Parameters:
                | 
                |         oVolume
                |             The volume 
                |         oArea
                |             The area 
                |         oXCOfG
                |             The X coordinate of the center of gravity 
                |         oYCOfG
                |             The Y coordinate of the center of gravity 
                |         oZCOfG
                |             The Z coordinate of the center of gravity 
                | 
                |     Example:
                | 
                |            This example retrieves the wet area of theMeasureItem
                |            measure.
                |            The area unit given by oVolume is m^3
                |            The area unit given by oArea is m²
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theVolume As Double
                |              Dim theArea As Double
                |              Dim theXCOfG As Double
                |              Dim theYCOfG As Double
                |              Dim theZCOfG As Double
                |              theMeasureItem.GetVolume_Area_COfG theVolume, theArea, theXCOfG,
                |              theYCOfG, theZCOfG

        :return: tuple
        """
        return self.com_object.GetVolume_Area_COfG()

    def set_axis_system_on_measure(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948)
                | Sub SetAxisSystemOnMeasure(CATSafeArrayVariant
                | iAxisPositioning)
                |     Set the position of the axis system of the object with respect to the
                |     absolute axis system. This position corresponds to the product positioning
                |     matrix. All coordinates are internally computed using the axis system of the
                |     object. To provide these coordinates with respect to absolute axis system, it
                |     is required to know the position of the axis system of the
                |     object.
                |
                |     Parameters:
                |
                |         ioAxisPosition
                |             The information of the axis system with respect to the product
                |             coordinate system:
                |
                |                 iAxisPositioning(0) is the X coordinate of the origin of the
                |                 axis system
                |                 iAxisPositioning(1) is the Y coordinate of the origin of the
                |                 axis system
                |                 iAxisPositioning(2) is the Z coordinate of the origin of the
                |                 axis system
                |                 iAxisPositioning(3) is the X coordinate of the first direction
                |                 of the axis system
                |                 iAxisPositioning(4) is the Y coordinate of the first direction
                |                 of the axis system
                |                 iAxisPositioning(5) is the Z coordinate of the first direction
                |                 of the axis system
                |                 iAxisPositioning(6) is the X coordinate of the second direction
                |                 of the axis system
                |                 iAxisPositioning(7) is the Y coordinate of the second direction
                |                 of the axis system
                |                 iAxisPositioning(8) is the Z coordinate of the second direction
                |                 of the axis system
                |                 iAxisPositioning(9) is the X coordinate of the third direction
                |                 of the axis system
                |                 iAxisPositioning(10) is the Y coordinate of the third direction
                |                 of the axis system
                |                 iAxisPositioning(11) is the Z coordinate of the third direction
                |                 of the axis system
                |
                |     Example:
                |
                |            This example set the axis system for theMeasureItem
                |            computation.
                |
                |
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              Dim theAxisPositioning(11)
                |              theAxisPositioning(0) = 0
                |              theAxisPositioning(1) = 0
                |              theAxisPositioning(2) = 0
                |              theAxisPositioning(3) = 1
                |              theAxisPositioning(4) = 0
                |              theAxisPositioning(5) = 0
                |              theAxisPositioning(6) = 0
                |              theAxisPositioning(7) = 1
                |              theAxisPositioning(8) = 0
                |              theAxisPositioning(9) = 0
                |              theAxisPositioning(10) = 0
                |              theAxisPositioning(11) = 1
                |              theMeasureItem.SetAxisSystemOnMeasure
                |              theAxisPositioning

        :return: tuple
        """
        return self.com_object.SetAxisSystemOnMeasure()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_axis_system_on_measure'
        # vba_code = """
        # Public Function set_axis_system_on_measure(measure_item)
        #     Dim iAxisPositioning (2)
        #     measure_item.SetAxisSystemOnMeasure iAxisPositioning
        #     set_axis_system_on_measure = iAxisPositioning
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_computation_mode(self, i_computation_mode: CATMeasurableModeOfCalc) -> None:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetComputationMode(CATMeasurableModeOfCalc
                | iComputationMode)
                |     Set the mode of computation of the object. The computation mode of the
                |     object can be: Exact, Approximate or ExactElseApprox.
                | 
                |     Parameters:
                | 
                |         iComputationMode
                |             The mode of computation 
                | 
                |     Example:
                | 
                |            This example get the computation mode of
                |            theMeasureItem.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              theMeasureItem.SetComputationMode
                |              MeasExactElseApproxCalculation

        :param CATMeasurableModeOfCalc i_computation_mode:
        :return: None
        """
        return self.com_object.SetComputationMode(i_computation_mode)

    def set_measure_item_type(self, i_measure_item_type: CATOpnsMeasureItemType) -> None:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMeasureItemType(CATOpnsMeasureItemType
                | iMeasureItemType)
                |     Set the Measure Item Type.
                | 
                |     Parameters:
                | 
                |         iMeasureItemType
                |             The Measure Item Type The Measure Item Type can be:
                |             catOpnsPointItem, catOpnsEdgeItem, catOpnsSurfaceItem, catOpnsVolumeItem,
                |             catOpnsComplexItem, catOpnsUnknownItem, catOpnsNotValid, catOpnsThicknessItem,
                |             catOpnsSurface2DItem, catOpnsAngle3PtsItem. @see CATOpnsMeasureItemType
                |             
                | 
                |     Example:
                | 
                |            This example set the measure item type of
                |            theMeasureItem.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              theMeasureItem.SetMeasureItemType catOpnsEdgeItem

        :param int i_measure_item_type:
        :return: None
        """
        return self.com_object.SetMeasureItemType(i_measure_item_type)

    def set_selection(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948)
                | Sub SetSelection(CATSafeArrayVariant iSelections)
                |     Set the selected objects of the measure Item.
                |
                |     Parameters:
                |
                |         iSelections
                |             The set of the selected objects
                |
                |     Example:
                |
                |            This example set the selected objects of
                |            theMeasureItem.
                |
                |
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasureItem As MeasureItem
                |              Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)
                |              theMeasureItem.SetSelection theSelections

        :return: tuple
        """
        return self.com_object.SetSelection()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_selection'
        # vba_code = """
        # Public Function set_selection(measure_item)
        #     Dim iSelections (2)
        #     measure_item.SetSelection iSelections
        #     set_selection = iSelections
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MeasureItem(name="{self.name}")'
