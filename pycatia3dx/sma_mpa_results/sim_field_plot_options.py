"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_results.sim_field_plot import SimFieldPlot


class SimFieldPlotOptions(SimFieldPlot):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SMAMpaResultsIDLItf.SimFieldPlot
                |                         SimFieldPlotOptions
                | 
                | Represents the field plot rendering options.
                | Role:After creating the field plot, one can set the various options provided in
                | this interface.
                | The Update method needs to be called at the end after setting all the
                | options.
                | Example:
                | 
                |  Given a field plot object, you can set the various options.
                |  
                | 
                |  Dim oFieldPlotOptions As SimFieldPlotOptions
                |  Set oFieldPlotOptions = oFieldPlot.GetItem("SimFieldPlotOptions")
                |  oFieldPlotOptions.Transparency = False
                |  oFieldPlotOptions.SetShowLabels False, False
                |  oFieldPlotOptions.Update
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def exterior_render_style(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ExteriorRenderStyle(SimRenderStyle ieStyle) (Write
                | Only)
                |     Sets the exterior render style for the model. The SimRenderStyle enum can
                |     be found in SMAIAMpaFieldPlotEnums file

        :return: bool
        """

        return self.com_object.ExteriorRenderStyle

    @exterior_render_style.setter
    def exterior_render_style(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ExteriorRenderStyle = value

    @property
    def exterior_symbols(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ExteriorSymbols(boolean ibExtSymbol) (Write Only)
                |     Sets the exterior symbols to the field plot. Set True to show the exterior
                |     symbol.

        :return: bool
        """

        return self.com_object.ExteriorSymbols

    @exterior_symbols.setter
    def exterior_symbols(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ExteriorSymbols = value

    @property
    def hide_model(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HideModel(boolean ibHideModel) (Write Only)
                |     Hides the model and only shows the symbols.

        :return: bool
        """

        return self.com_object.HideModel

    @hide_model.setter
    def hide_model(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.HideModel = value

    @property
    def isocontour_render_style(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsocontourRenderStyle(SimRenderStyle ieStyle) (Write
                | Only)
                |     Sets the iso-contour render style. The SimRenderStyle enum can be found in
                |     SMAIAMpaFieldPlotEnums file

        :return: bool
        """

        return self.com_object.IsocontourRenderStyle

    @isocontour_render_style.setter
    def isocontour_render_style(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IsocontourRenderStyle = value

    @property
    def model_render_style(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ModelRenderStyle(SimRenderStyle ieStyle) (Write Only)
                |     Sets the render style for the model. The SimRenderStyle enum can be found
                |     in SMAIAMpaFieldPlotEnums file

        :return: bool
        """

        return self.com_object.ModelRenderStyle

    @model_render_style.setter
    def model_render_style(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ModelRenderStyle = value

    @property
    def section_points_location(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SectionPointsLocation(SimSectionPointLocation ieLocation) (Write
                | Only)
                |     Specifies the section point location. The SimSectionPointLocation enum can
                |     be found in SMAIAMpaFieldPlotEnums file.

        :return: bool
        """

        return self.com_object.SectionPointsLocation

    @section_points_location.setter
    def section_points_location(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SectionPointsLocation = value

    @property
    def show_isocontour_edges(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ShowIsocontourEdges(boolean ibShowEdges) (Write Only)
                |     Displays the isocontour edges.

        :return: bool
        """

        return self.com_object.ShowIsocontourEdges

    @show_isocontour_edges.setter
    def show_isocontour_edges(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ShowIsocontourEdges = value

    @property
    def symbol_density(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SymbolDensity(double idValue) (Write Only)
                |     Sets the symbol density to the field plot. The value ranges from 1 to
                |     100.

        :return: bool
        """

        return self.com_object.SymbolDensity

    @symbol_density.setter
    def symbol_density(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SymbolDensity = value

    @property
    def transparency(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Transparency(boolean ibTransperency) (Write Only)
                |     Sets the transparency to the field plot. Set True to make it
                |     transparent.

        :return: bool
        """

        return self.com_object.Transparency

    @transparency.setter
    def transparency(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Transparency = value

    @property
    def transparent_isocontours(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TransparentIsocontours(boolean ibTransparency) (Write
                | Only)
                |     Sets the transparency of the iso-contours.

        :return: bool
        """

        return self.com_object.TransparentIsocontours

    @transparent_isocontours.setter
    def transparent_isocontours(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.TransparentIsocontours = value

    def set_node_symbol_attributes(self, ie_symbol_type: int, id_value: float, ib_use_depth_effect: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetNodeSymbolAttributes(SimNodeSymbolType ieSymbolType,double
                | idValue,boolean ibUseDepthEffect)
                |     Sets the node symbol attributes. The value ranges from 1 to
                |     100.
                | 
                |     Parameters:
                | 
                |         SimNodeSymbolType
                |             Specifies the symbol type. See SimNodeSymbolType for more options
                |             
                |         ibUseDepthEffect
                |             Set True to show the depth effect.

        :param int ie_symbol_type:
        :param float id_value:
        :param bool ib_use_depth_effect:
        :return: None
        """
        return self.com_object.SetNodeSymbolAttributes(ie_symbol_type, id_value, ib_use_depth_effect)

    def set_shell_style(self, ie_shell_style: int, ie_source_type: int, id_scale_factor: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetShellStyle(SimShellStyle ieShellStyle,SimThicknessDataSourceType
                | ieSourceType,double idScaleFactor)
                |     Specifies the shell styles options.
                | 
                |     Parameters:
                | 
                |         ieShellStyle
                |             Specifies the shell style. The SimShellStyles enum can be found in
                |             SMAIAMpaFieldPlotEnums file. 
                |         ieSourceType
                |             Specify the thickness data source for the rendering thickness. The
                |             SimThicknessDataSourceType enum can be found in SMAIAMpaFieldPlotEnums file.
                |             
                |         idScaleFactor
                |             Specifies the Thickness Scale Factor, expressed as a multiplier, to
                |             enhance visibility.

        :param int ie_shell_style:
        :param int ie_source_type:
        :param float id_scale_factor:
        :return: None
        """
        return self.com_object.SetShellStyle(ie_shell_style, ie_source_type, id_scale_factor)

    def set_show_labels(self, ib_node_labels: bool, ib_element_labels: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetShowLabels(boolean ibNodeLabels,boolean
                | ibElementLabels)
                |     Displays the node and element and labels.
                | 
                |     Parameters:
                | 
                |         ibNodeLabels
                |             Set true to show the node labels. 
                |         ibElementLabels
                |             Set true to show the element labels.

        :param bool ib_node_labels:
        :param bool ib_element_labels:
        :return: None
        """
        return self.com_object.SetShowLabels(ib_node_labels, ib_element_labels)

    def set_show_sph_display(self, ib_show_particles: bool, ib_show_surface: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetShowSPHDisplay(boolean ibShowParticles,boolean
                | ibShowSurface)
                |     Specifies the SPH display options. If both the options are set True, the
                |     SPH particle as well as SPH surface will be shown.
                | 
                |     Parameters:
                | 
                |         ibShowParticles
                |             Set True to show the SPH particles. 
                |         ibShowSurface
                |             Set True to show the SPH surface.

        :param bool ib_show_particles:
        :param bool ib_show_surface:
        :return: None
        """
        return self.com_object.SetShowSPHDisplay(ib_show_particles, ib_show_surface)

    def set_threshold(self, ie_threshold_type: int, id_value: float, ib_show_extrema: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetThreshold(SimThresholdType ieThresholdType,double idValue,boolean
                | ibShowExtrema)
                |     Specifies the threshold type to set the measurement criteria. It also
                |     displays the minimum and maximum values in the plot.
                | 
                |     Parameters:
                | 
                |         ieThresholdType
                |             Specifies the threshold type. The SimThresholdType enum can be
                |             found in SMAIAMpaFieldPlotEnums file. 
                |         idValue
                |             Specifies the upper or the lower limit depending on the threshold
                |             type. 
                |         ibShowExtrema
                |             True to display the extrema on the plot.

        :param int ie_threshold_type:
        :param float id_value:
        :param bool ib_show_extrema:
        :return: None
        """
        return self.com_object.SetThreshold(ie_threshold_type, id_value, ib_show_extrema)

    def set_visible_edges(self, ie_edge_type: int, id_edge_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetVisibleEdges(SimVisibleEdges ieEdgeType,double
                | idEdgeAngle)
                |     Specifies the way in which the edges will be displayed.
                | 
                |     Parameters:
                | 
                |         ieEdgeType
                |             Set the type of edge option. The SimVisibleEdges enum can be found
                |             in SMAIAMpaFieldPlotEnums file. 
                |         idEdgeAngle
                |             This option is valid only for SimOutline option only. The edge
                |             angle is the minimum angle between adjoining element faces in order for an edge
                |             to be shown in the display. The edge angle must be greater than zero and less
                |             than or equal to 90°.

        :param int ie_edge_type:
        :param float id_edge_angle:
        :return: None
        """
        return self.com_object.SetVisibleEdges(ie_edge_type, id_edge_angle)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update()
                |     Updates the field plot. This method should be called at the end after
                |     setting all the above attributes.

        :return: None
        """
        return self.com_object.Update()

    def __repr__(self):
        return f'SimFieldPlotOptions(name="{ self.name }")'
