"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class StrFlange(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrFlange
                | 
                | Object to manage Flange of a Plate.
                | Role: Allows accessing of Flange's data.
                | 
                | See also:
                |     StrFlanges
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def bending_angle(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BendingAngle() As Parameter (Read Only)
                |     Sets the Bending Angle.
                | 
                |     Example:
                | 
                | 
                |              This example Sets the required bending angle.
                |              
                | 
                |              Dim oBendingAngle As Parameter
                |              Set oBendingAngle = oObjStrFlange.BendingAngle
                |             oBendingAngle.ValuateFromString("120deg")

        :return: Parameter
        """

        return Parameter(self.com_object.BendingAngle)

    @property
    def bending_radius(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BendingRadius() As Parameter (Read Only)
                |     Sets the Bending Radius.
                | 
                |     Example:
                | 
                | 
                |              This example Sets the required bending radius.
                |              
                | 
                |              Dim oBendingRadius As Parameter
                |              Set oBendingRadius = oObjStrFlange.BendingRadius
                |             oBendingRadius.ValuateFromString("8mm")

        :return: Parameter
        """

        return Parameter(self.com_object.BendingRadius)

    @property
    def edge(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Edge() As Reference (Read Only)
                |     Gets the Edge of Plate.
                | 
                |     Parameters:
                | 
                |         oEdgeIndex
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the edge of plate.
                |              
                | 
                |              Dim ObjSfdReferencePlane As Reference
                |              Set ObjSfdReferencePlane = oObjStrFlange.Edge

        :return: Reference
        """

        return Reference(self.com_object.Edge)

    @property
    def end_end_cut_angle(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EndEndCutAngle() As Parameter (Read Only)
                |     Sets End EndCut Angle.
                | 
                |     Example:
                | 
                | 
                |              This example Sets the End EndCut Angle.
                |              
                | 
                |             Dim oEndEndCutAngle As Parameter
                |             Set oEndEndCutAngle = oObjStrFlange.EndEndCutAngle
                |             oEndEndCutAngle.ValuateFromString("60deg")

        :return: Parameter
        """

        return Parameter(self.com_object.EndEndCutAngle)

    @property
    def end_end_cut_distance(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EndEndCutDistance() As Parameter (Read Only)
                |     Sets End EndCut Distance.
                | 
                |     Example:
                | 
                | 
                |              This example Sets the End EndCut Distance.
                |              
                | 
                |             Dim oEndEndCutDistance As Parameter
                |             Set oEndEndCutDistance = oObjStrFlange.EndEndCutDistance
                |             oEndEndCutDistance.ValuateFromString("100mm")

        :return: Parameter
        """

        return Parameter(self.com_object.EndEndCutDistance)

    @property
    def end_end_cut_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EndEndCutOffset() As Parameter (Read Only)
                |     Sets End EndCut Offset.
                | 
                |     Example:
                | 
                | 
                |              This example Sets the End EndCut Offset.
                |              
                | 
                |             Dim oEndEndCutOffset As Parameter
                |             Set oEndEndCutOffset = oObjStrFlange.EndEndCutOffset
                |             oEndEndCutOffset.ValuateFromString("10mm")

        :return: Parameter
        """

        return Parameter(self.com_object.EndEndCutOffset)

    @property
    def end_end_cut_radius(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EndEndCutRadius() As Parameter (Read Only)
                |     Sets End EndCut Radius.
                | 
                |     Example:
                | 
                | 
                |              This example Sets the End EndCut Radius.
                |              
                | 
                |             Dim oEndEndCutRadius As Parameter
                |             Set oEndEndCutRadius = oObjStrFlange.EndEndCutRadius
                |             oEndEndCutRadius.ValuateFromString("50mm")

        :return: Parameter
        """

        return Parameter(self.com_object.EndEndCutRadius)

    @property
    def flange_end_limit(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FlangeEndLimit() As Reference
                | 
                |     Example:
                | 
                | 
                |              put_FlangeEndLimit: Sets FlangeEndLimit
                |              This example Sets the Flange End Limit.
                |              
                | 
                |              Set RefSfdPlane = ObjPart.FindObjectByName("CROSS.40")
                |              Dim ObjSfdReferencePlane As Reference
                |              SFDProdSel.Add RefSfdPlane
                |              Set ObjSfdReferencePlane = SFDProdSel.FindObject("CATIAReference")
                |               oObjStrFlange.FlangeEndLimit = ObjSfdReferencePlane
                |              
                | 
                | 
                |               get_FlangeEndLimit: Gets FlangeEndLimit
                |              This example gets the Flange End Limit.
                |              
                | 
                |              Dim oFlangeEndLimit As Reference
                |              Set oFlangeEndLimit = oObjStrFlange.FlangeEndLimit

        :return: Reference
        """

        return Reference(self.com_object.FlangeEndLimit)

    @flange_end_limit.setter
    def flange_end_limit(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FlangeEndLimit = value

    @property
    def flange_start_limit(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FlangeStartLimit() As Reference
                | 
                |     Example:
                | 
                | 
                |              put_FlangeStartLimit: Sets FlangeStartLimit
                |              This example Sets the Flange Start Limit.
                |              
                | 
                |              Set RefSfdPlane = ObjPart.FindObjectByName("CROSS.40")
                |              Dim ObjSfdReferencePlane As Reference
                |              SFDProdSel.Add RefSfdPlane
                |              Set ObjSfdReferencePlane = SFDProdSel.FindObject("CATIAReference")
                |               oObjStrFlange.FlangeStartLimit = ObjSfdReferencePlane
                |              
                | 
                | 
                |              get_FlangeStartLimit: Gets FlangeStartLimit
                |              This example gets the Flange Start Limit.
                |              
                | 
                |              Dim oFlangeStartLimit As Reference
                |              Set oFlangeStartLimit = oObjStrFlange.FlangeStartLimit

        :return: Reference
        """

        return Reference(self.com_object.FlangeStartLimit)

    @flange_start_limit.setter
    def flange_start_limit(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FlangeStartLimit = value

    @property
    def flange_width(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FlangeWidth() As Parameter (Read Only)
                |     Sets the Flange Width.
                | 
                |     Example:
                | 
                | 
                |              This example Sets the required width.
                |              
                | 
                |              Dim oFlangeWidth As Parameter
                |              Set oFlangeWidth = oObjStrFlange.FlangeWidth
                |             oFlangeWidth.ValuateFromString("500mm")

        :return: Parameter
        """

        return Parameter(self.com_object.FlangeWidth)

    @property
    def operated_plate(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OperatedPlate() As Reference (Read Only)
                |     Returns the reference of Plate object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the reference of Plate
                |              object.
                |              
                | 
                |              Dim ObjSfdPlate As Reference
                |              Set ObjSfdPlate = oObjStrFlange.OperatedPlate

        :return: Reference
        """

        return Reference(self.com_object.OperatedPlate)

    @property
    def start_end_cut_angle(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartEndCutAngle() As Parameter (Read Only)
                |     Sets Start EndCut Angle.
                | 
                |     Example:
                | 
                | 
                |              This example Sets the Start EndCut Angle.
                |              
                | 
                |             Dim oStartEndCutAngle As Parameter
                |             Set oStartEndCutAngle = oObjStrFlange.StartEndCutAngle
                |             oStartEndCutAngle.ValuateFromString("60deg")

        :return: Parameter
        """

        return Parameter(self.com_object.StartEndCutAngle)

    @property
    def start_end_cut_distance(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartEndCutDistance() As Parameter (Read Only)
                |     Sets Start EndCut Distance.
                | 
                |     Example:
                | 
                | 
                |              This example Sets the Start EndCut Distance.
                |              
                | 
                |             Dim oStartEndCutDistance As Parameter
                |             Set oStartEndCutDistance = oObjStrFlange.StartEndCutDistance
                |             oStartEndCutDistance.ValuateFromString("100mm")

        :return: Parameter
        """

        return Parameter(self.com_object.StartEndCutDistance)

    @property
    def start_end_cut_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartEndCutOffset() As Parameter (Read Only)
                |     Sets Start EndCut Offset.
                | 
                |     Example:
                | 
                | 
                |              This example Sets the Start EndCut Offset.
                |              
                | 
                |             Dim oStartEndCutOffset As Parameter
                |             Set oStartEndCutOffset = oObjStrFlange.StartEndCutOffset
                |             oStartEndCutOffset.ValuateFromString("10mm")

        :return: Parameter
        """

        return Parameter(self.com_object.StartEndCutOffset)

    @property
    def start_end_cut_radius(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartEndCutRadius() As Parameter (Read Only)
                |     Sets Start EndCut Radius.
                | 
                |     Example:
                | 
                | 
                |              This example Sets the Start EndCut Radius.
                |              
                | 
                |             Dim oStartEndCutRadius As Parameter
                |             Set oStartEndCutRadius = oObjStrFlange.StartEndCutRadius
                |             oStartEndCutRadius.ValuateFromString("50mm")

        :return: Parameter
        """

        return Parameter(self.com_object.StartEndCutRadius)

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As long
                |     The types of Flange:
                |     - 1 : Centered
                |     - 2 : Tangent
                | 
                |     Example:
                | 
                | 
                |              get_Type: Gets Type.
                |              
                |              
                | 
                |     Parameters:
                | 
                |         oType
                | 
                |              Dim oType As long
                |             oType = oObjStrFlange.Type
                |              
                | 
                |             put_Type: Sets Type. 
                |         iType
                | 
                |              oObjStrFlange.Type = 1

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    @property
    def width_measurement_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WidthMeasurementType() As long
                |     The types of Width Measurement:
                |     - 1 : FlangeWidthToInnerFace
                |     - 2 : FlangeWidthToOuterFace
                |     - 3 : FlangeWidthToNeutralFibre
                | 
                |     Example:
                | 
                | 
                |              get_WidthMeasurementType: Gets Width Measurement
                |              Type.
                |              
                |              
                | 
                |     Parameters:
                | 
                |         oWidthMeasurementType
                | 
                |              Dim oWidthMeasurementType As long
                |              oWidthMeasurementType = oObjStrFlange.WidthMeasurementType
                |              
                | 
                |             put_WidthMeasurementType: Sets Width Measurement Type.
                |             
                |         iWidthMeasurementType
                | 
                |              oObjStrFlange.WidthMeasurementType = 1

        :return: int
        """

        return self.com_object.WidthMeasurementType

    @width_measurement_type.setter
    def width_measurement_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.WidthMeasurementType = value

    def set_edges(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetEdges(CATSafeArrayVariant iListOfEdgesIndex)
                |     Sets the Edges of Plate on which flange to be created.
                |
                |     Parameters:
                |
                |         iListOfEdgesIndex
                |
                |     Example:
                |
                |
                |              This example Sets the Edges on which flange to be
                |              created.
                |
                |
                |              Dim EdgeList(1) As Variant
                |               EdgeList(0) = 4
                |              EdgeList(1) = 3
                |                 oObjStrFlange.SetEdges EdgeList

        :return: tuple
        """
        return self.com_object.SetEdges()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_edges'
        # vba_code = """
        # Public Function set_edges(str_flange)
        #     Dim iListOfEdgesIndex (2)
        #     str_flange.SetEdges iListOfEdgesIndex
        #     set_edges = iListOfEdgesIndex
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'StrFlange(name="{self.name}")'
