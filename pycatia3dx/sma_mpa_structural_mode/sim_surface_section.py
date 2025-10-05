"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_orientation import SimOrientation
from pycatia3dx.sma_mpa_structural_mode.sim_rebar_layers import SimRebarLayers


class SimSurfaceSection(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSurfaceSection
                | 
                | Represents the Surface Section object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def all_rebar_layers(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllRebarLayers() As CATSafeArrayVariant (Read Only)
                |     Returns the Rebar Layers associated with the section.

        :return: tuple
        """

        return self.com_object.AllRebarLayers

    @property
    def density(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Density() As double
                |     Mass density per unit area value. Quantity: SURFACICMASS, units: m_2

        :return: float
        """

        return self.com_object.Density

    @density.setter
    def density(self, value: float):
        """
        :param float value:
        """

        self.com_object.Density = value

    @property
    def rebar_layers_orientation(self) -> SimOrientation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RebarLayersOrientation() As SimOrientation (Read
                | Only)
                |     Returns the Orientation of the Rebar Layers associated with the section.

        :return: SimOrientation
        """

        return SimOrientation(self.com_object.RebarLayersOrientation)

    @property
    def rebars(self) -> SimRebarLayers:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Rebars() As SimRebarLayers (Read Only)
                |     Returns the Rebar Layers associated with the section.

        :return: SimRebarLayers
        """

        return SimRebarLayers(self.com_object.Rebars)

    def add_rebar_layer(self, i_type: str, o_feature: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddRebarLayer(CATBSTR iType,CATBaseDispatch oFeature)
                |     Adds a Rebar Layer to the section. 

        :param str i_type:
        :param AnyObject o_feature:
        :return: None
        """
        return self.com_object.AddRebarLayer(i_type, o_feature.com_object)

    def __repr__(self):
        return f'SimSurfaceSection(name="{ self.name }")'
