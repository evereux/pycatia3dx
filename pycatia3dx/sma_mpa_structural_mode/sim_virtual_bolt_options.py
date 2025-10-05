"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class SimVirtualBoltOptions(CATBaseDispatch):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimVirtualBoltOptions
                | 
                | Represents the Virtual Bolt object.
                | 
                | Example:
                |     Given a SimMCXProperties object, you can create a SimVirtualBolt as
                |     following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyVirtualBolt As SimVirtualBolt
                |      Set MyVirtualBolt = MyMCXProperties.Add("SimVirtualBolt")
                |      
                | 
                |     Given a SimMCXProperties object, you can retrieve a SimVirtualBolt named
                |     "Virtual Bolt.1" as following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyVirtualBolt As SimVirtualBolt
                |      Set MyVirtualBolt = MyMCXProperties.Item("Virtual Bolt.1")
                |      
                | 
                | Given a SimVirtualBolt object myVirtualBolt, you can retrieve a
                | SimVirtualBoltOptions as following:
                | 
                |  ...
                |  Dim myVirtualBoltOptions As SimVirtualBoltOptions
                |  Set myVirtualBoltOptions = myVirtualBolt.GetItem("SimVirtualBoltOptions")
                |  
                | 
                | Example in Python:
                |     Given a SimMCXProperties object myMCXProperties, you can create a
                |     SimVirtualBolt as following:
                | 
                |      ...
                |      myVirtualBolt = myMCXProperties.Add("SimVirtualBolt")
                |      
                | 
                |     Given a SimMCXProperties object myMCXProperties, you can retrieve a
                |     SimVirtualBolt named "Virtual Bolt.1" as following:
                | 
                |      ...
                |      myVirtualBolt = myMCXProperties.Item("Virtual Bolt.1")
                |      
                | 
                | Given a SimVirtualBolt object myVirtualBolt, you can retrieve a
                | SimVirtualBoltOptions as following:
                | 
                |  ...
                |  Set myVirtualBoltOptions = myVirtualBolt.GetItem("SimVirtualBoltOptions")
                |  
                | 
                | See also:
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def advanced_coupling_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AdvancedCouplingType() As
                | SimVirtualBoltAdvancedCouplingType
                |     Returns or sets the coupling type.

        :return: int
        """

        return self.com_object.AdvancedCouplingType

    @advanced_coupling_type.setter
    def advanced_coupling_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.AdvancedCouplingType = value

    @property
    def allow_preload_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllowPreloadFlag() As boolean
                |     Returns or sets the allow preload flag.

        :return: bool
        """

        return self.com_object.AllowPreloadFlag

    @allow_preload_flag.setter
    def allow_preload_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AllowPreloadFlag = value

    @property
    def bending_stiffness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BendingStiffness() As double
                |     Returns or sets the Bending stiffness.

        :return: float
        """

        return self.com_object.BendingStiffness

    @bending_stiffness.setter
    def bending_stiffness(self, value: float):
        """
        :param float value:
        """

        self.com_object.BendingStiffness = value

    @property
    def connect_other_end_of_solid_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConnectOtherEndOfSolidFlag() As boolean
                |     Returns or sets the Connect Other end of solid flag (Applicable only for
                |     beam mechanical behavior).

        :return: bool
        """

        return self.com_object.ConnectOtherEndOfSolidFlag

    @connect_other_end_of_solid_flag.setter
    def connect_other_end_of_solid_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ConnectOtherEndOfSolidFlag = value

    @property
    def connector_behavior(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConnectorBehavior() As
                | SimVirtualBoltMechanicalBehavior
                |     Returns or sets the bolt mechanical behavior (construct).

        :return: int
        """

        return self.com_object.ConnectorBehavior

    @connector_behavior.setter
    def connector_behavior(self, value: int):
        """
        :param int value:
        """

        self.com_object.ConnectorBehavior = value

    @property
    def head_coupled_surface_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HeadCoupledSurfaceType() As
                | SimVirtualBoltCoupledSurfaceType
                |     Returns or sets the bolt head coupled surface type.

        :return: int
        """

        return self.com_object.HeadCoupledSurfaceType

    @head_coupled_surface_type.setter
    def head_coupled_surface_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.HeadCoupledSurfaceType = value

    @property
    def head_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HeadType() As SimVirtualBolt_BoltType
                |     Returns or sets the head type for bolt.

        :return: int
        """

        return self.com_object.HeadType

    @head_type.setter
    def head_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.HeadType = value

    @property
    def interface_coupled_surface_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InterfaceCoupledSurfaceType() As
                | SimVirtualBoltCoupledSurfaceType
                |     Returns or sets the bolt interface coupled surface type(Applicable only for
                |     beam mechanical behavior).

        :return: int
        """

        return self.com_object.InterfaceCoupledSurfaceType

    @interface_coupled_surface_type.setter
    def interface_coupled_surface_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.InterfaceCoupledSurfaceType = value

    @property
    def interface_washer_diameter(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InterfaceWasherDiameter() As double
                |     Returns or sets the bolt interface washer diameter value(Applicable only
                |     for beam mechanical behavior).

        :return: float
        """

        return self.com_object.InterfaceWasherDiameter

    @interface_washer_diameter.setter
    def interface_washer_diameter(self, value: float):
        """
        :param float value:
        """

        self.com_object.InterfaceWasherDiameter = value

    @property
    def intermediate_coupled_surface_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IntermediateCoupledSurfaceType() As
                | SimVirtualBoltCoupledSurfaceType
                |     Returns or sets the intermediate coupled surface type.

        :return: int
        """

        return self.com_object.IntermediateCoupledSurfaceType

    @intermediate_coupled_surface_type.setter
    def intermediate_coupled_surface_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.IntermediateCoupledSurfaceType = value

    @property
    def intermediate_coupling_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IntermediateCouplingType() As
                | SimVirtualBoltIntermediateCouplingType
                |     Returns or sets the coupling type.

        :return: int
        """

        return self.com_object.IntermediateCouplingType

    @intermediate_coupling_type.setter
    def intermediate_coupling_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.IntermediateCouplingType = value

    @property
    def intermediate_washer_diameter(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IntermediateWasherDiameter() As double
                |     Returns or sets the bolt intermediate washer diameter value.

        :return: float
        """

        return self.com_object.IntermediateWasherDiameter

    @intermediate_washer_diameter.setter
    def intermediate_washer_diameter(self, value: float):
        """
        :param float value:
        """

        self.com_object.IntermediateWasherDiameter = value

    @property
    def number_of_head_node_rings(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfHeadNodeRings() As long
                |     Returns or sets the number of head node rings.

        :return: int
        """

        return self.com_object.NumberOfHeadNodeRings

    @number_of_head_node_rings.setter
    def number_of_head_node_rings(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfHeadNodeRings = value

    @property
    def number_of_interface_node_rings(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfInterfaceNodeRings() As long
                |     Returns or sets the number of interface node rings(Applicable only for beam
                |     mechanical behavior).

        :return: int
        """

        return self.com_object.NumberOfInterfaceNodeRings

    @number_of_interface_node_rings.setter
    def number_of_interface_node_rings(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfInterfaceNodeRings = value

    @property
    def number_of_intermediate_node_rings(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfIntermediateNodeRings() As long
                |     Returns or sets the number of intermediate node rings(Applicable only for
                |     beam mechanical behavior).

        :return: int
        """

        return self.com_object.NumberOfIntermediateNodeRings

    @number_of_intermediate_node_rings.setter
    def number_of_intermediate_node_rings(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfIntermediateNodeRings = value

    @property
    def number_of_nut_node_rings(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfNutNodeRings() As long
                |     Returns or sets the number of nut node rings.

        :return: int
        """

        return self.com_object.NumberOfNutNodeRings

    @number_of_nut_node_rings.setter
    def number_of_nut_node_rings(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfNutNodeRings = value

    @property
    def nut_coupled_surface_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NutCoupledSurfaceType() As
                | SimVirtualBoltCoupledSurfaceType
                |     Returns or sets the bolt nut coupled surface type.

        :return: int
        """

        return self.com_object.NutCoupledSurfaceType

    @nut_coupled_surface_type.setter
    def nut_coupled_surface_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.NutCoupledSurfaceType = value

    @property
    def nut_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NutType() As SimVirtualBolt_BoltType
                |     Returns or sets the nut type for bolt.

        :return: int
        """

        return self.com_object.NutType

    @nut_type.setter
    def nut_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.NutType = value

    @property
    def solid_solid_connection_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SolidSolidConnectionType() As
                | SimVirtualBoltSolidSolidConnectionType
                |     Returns or sets the Solid Solid interface connection type.(Applicable only
                |     for beam mechanical behavior).

        :return: int
        """

        return self.com_object.SolidSolidConnectionType

    @solid_solid_connection_type.setter
    def solid_solid_connection_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SolidSolidConnectionType = value

    @property
    def torsional_stiffness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TorsionalStiffness() As double
                |     Returns or sets the Torsional stiffness. 

        :return: float
        """

        return self.com_object.TorsionalStiffness

    @torsional_stiffness.setter
    def torsional_stiffness(self, value: float):
        """
        :param float value:
        """

        self.com_object.TorsionalStiffness = value

    def __repr__(self):
        return f'SimVirtualBoltOptions()'
