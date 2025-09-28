"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeLawDistProj(HybridShape):

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
                |                         HybridShapeLawDistProj
                | 
                | Interface to law feature.
                | Role: Allows you to access data of a law feature created by using a reference
                | line and a definition curve.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def applied_unit_symbol(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AppliedUnitSymbol(CATBSTR iSymbol) (Write Only)
                |     Returns or sets the applied unit symbol for heterogeneous law.

        :return: bool
        """

        return self.com_object.AppliedUnitSymbol

    @applied_unit_symbol.setter
    def applied_unit_symbol(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AppliedUnitSymbol = value

    @property
    def definition(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Definition() As Reference
                |     Returns or sets the definition curve of the law.
                |     Sub-element(s) supported (see Boundary object): see TriDimFeatEdge or
                |     BiDimFeatEdge.

        :return: Reference
        """

        return Reference(self.com_object.Definition)

    @definition.setter
    def definition(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Definition = value

    @property
    def measure_unit_symbol(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property MeasureUnitSymbol(CATBSTR iSymbol) (Write Only)
                |     Returns or sets the measure unit symbol for heterogeneous law.

        :return: bool
        """

        return self.com_object.MeasureUnitSymbol

    @measure_unit_symbol.setter
    def measure_unit_symbol(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MeasureUnitSymbol = value

    @property
    def parameter_on_definition(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ParameterOnDefinition() As boolean
                |     Queries whether evolution parameter is on reference curve (default) or on definition curve,or sets evolution parameter on reference curve or on definition curve. Possible values of ParameterOnDefinition = TRUE : Parameter on definition curve. = FALSE : Parameter on reference curve. 
                | 
                | Example:
                |     This example retrieves in ParOnDef the ParameterOnDefinition status of the
                |     hybridShapeLawDist hybrid shape law feature.
                | 
                |      Dim ParOnDef As boolean
                |      ParOnDef = hybridShapeLawDist.ParameterOnDefinition

        :return: bool
        """

        return self.com_object.ParameterOnDefinition

    @parameter_on_definition.setter
    def parameter_on_definition(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ParameterOnDefinition = value

    @property
    def positive_direction_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PositiveDirectionOrientation() As long
                |     Returns or sets the positive value direction.

        :return: int
        """

        return self.com_object.PositiveDirectionOrientation

    @positive_direction_orientation.setter
    def positive_direction_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.PositiveDirectionOrientation = value

    @property
    def reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Reference() As Reference
                |     Returns or sets the reference line of the law.
                |     Sub-element(s) supported (see Boundary object): see
                |     RectilinearTriDimFeatEdge or RectilinearBiDimFeatEdge.

        :return: Reference
        """

        return Reference(self.com_object.Reference)

    @reference.setter
    def reference(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Reference = value

    @property
    def scaling(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Scaling() As double
                |     Returns or sets the scaling ratio of the law.

        :return: float
        """

        return self.com_object.Scaling

    @scaling.setter
    def scaling(self, value: float):
        """
        :param float value:
        """

        self.com_object.Scaling = value

    def get_applied_unit_symbol(self, o_symbol: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetAppliedUnitSymbol(CATBSTR oSymbol)
                |     Returns the applied unit symbol.
                | 
                |     Parameters:
                | 
                |         oSymbol
                |             The symbol of applied unit 
                | 
                |     Example:
                |         This example retrieves in oSymbol the applied unit symbol of the
                |         hybridShapeLawDist hybrid shape law feature.
                | 
                |          Dim oSymbol
                |          hybridShapeLawDist.GetAppliedUnitSymboloSymbol

        :param str o_symbol:
        :return: None
        """
        return self.com_object.GetAppliedUnitSymbol(o_symbol)

    def get_measure_unit_symbol(self, o_symbol: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetMeasureUnitSymbol(CATBSTR oSymbol)
                |     Returns the measure unit symbol.
                | 
                |     Parameters:
                | 
                |         oSymbol
                |             The symbol of measure unit 
                | 
                |     Example:
                |         This example retrieves in oSymbol the measure unit symbol of the
                |         hybridShapeLawDist hybrid shape law feature.
                | 
                |          Dim oSymbol
                |          hybridShapeLawDist.GetMeasureUnitSymboloSymbol

        :param str o_symbol:
        :return: None
        """
        return self.com_object.GetMeasureUnitSymbol(o_symbol)

    def get_plane_normal(self, o_normal: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetPlaneNormal(CATSafeArrayVariant oNormal)
                |     Retrieves the support plane normal.
                | 
                |     Parameters:
                | 
                |         oNormal
                |             The support plane normal

        :param tuple o_normal:
        :return: None
        """
        return self.com_object.GetPlaneNormal(o_normal)

    def is_heterogeneous_law(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func IsHeterogeneousLaw() As boolean
                |     Queries whether Heterogeneous Law mode is active or not.
                | 
                |     Parameters:
                | 
                |         oHeterogeneousLaw
                |             heterogeneous law mode = TRUE : Heterogeneous Law mode is active. = FALSE : Heterogeneous Law mode is inactive.

        :return: bool
        """
        return self.com_object.IsHeterogeneousLaw()

    def put_plane_normal(self, i_normal: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub PutPlaneNormal(CATSafeArrayVariant iNormal)
                |     Sets the support plane normal.
                | 
                |     Parameters:
                | 
                |         iNormal
                |             The support plane normal

        :param tuple i_normal:
        :return: None
        """
        return self.com_object.PutPlaneNormal(i_normal)

    def __repr__(self):
        return f'HybridShapeLawDistProj(name="{ self.name }")'
