"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class DrawingGenViewProperties(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 DrawingGenViewProperties
                | 
                | Represents the generative properties of a drawing generative
                | view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def ann_callout_generation_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnnCalloutGenerationMode() As boolean
                |     Returns or sets the Annotation Callout Generation mode for the
                |     View.
                | 
                |     Example:
                | 
                |          This example sets the Annotation Callout Generation mode of the
                |          MyViewProp
                |          generative view properties to indicate that Annotation Callout must be
                |          generated.
                |          
                | 
                |          MyViewProp.AnnCalloutGenerationMode = true

        :return: bool
        """

        return self.com_object.AnnCalloutGenerationMode

    @ann_callout_generation_mode.setter
    def ann_callout_generation_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AnnCalloutGenerationMode = value

    @property
    def approximate_parameter(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ApproximateParameter() As short
                |     Returns or sets the level of detail for views generated as approximated
                |     view.
                | 
                |     Example:
                | 
                |          This example sets the level of detail of the
                |          MyViewProp
                |          generative view properties to 6.
                |          
                | 
                |          MyViewProp.ApproximateParameter = 6

        :return: int
        """

        return self.com_object.ApproximateParameter

    @approximate_parameter.setter
    def approximate_parameter(self, value: int):
        """
        :param int value:
        """

        self.com_object.ApproximateParameter = value

    @property
    def auto_hidden_line_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AutoHiddenLineMode() As boolean
                |     Returns or sets the Auto hidden line mode. The auto hidden line mode
                |     indicates whether to draw the auto hidden lines.
                | 
                |     Example:
                | 
                |          This example sets the auto hidden line mode of the
                |          MyViewProp
                |          generative view properties to indicate that auto hidden lines must
                |          not
                |          be drawn.
                |          
                | 
                |          MyViewProp.AutoHiddenLineMode = true

        :return: bool
        """

        return self.com_object.AutoHiddenLineMode

    @auto_hidden_line_mode.setter
    def auto_hidden_line_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AutoHiddenLineMode = value

    @property
    def axis_line_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisLineMode() As boolean
                |     Returns or sets the view axisline mode. The axisline mode indicates whether
                |     to draw the axislines.
                | 
                |     Example:
                | 
                |          This example sets the view axisline mode of the
                |          MyViewProp
                |          generative view properties to indicate that axislines must be
                |          drawn.
                |          
                | 
                |          MyViewProp.AxisLineMode = true

        :return: bool
        """

        return self.com_object.AxisLineMode

    @axis_line_mode.setter
    def axis_line_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AxisLineMode = value

    @property
    def centerline_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CenterlineMode() As boolean
                |     Returns or sets the view centerline mode. The centerline mode indicates
                |     whether to draw the centerlines.
                | 
                |     Example:
                | 
                |          This example sets the view centerline mode of the
                |          MyViewProp
                |          generative view properties to indicate that centerlines must be
                |          drawn.
                |          
                | 
                |          MyViewProp.CenterlineMode = true

        :return: bool
        """

        return self.com_object.CenterlineMode

    @centerline_mode.setter
    def centerline_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CenterlineMode = value

    @property
    def clash_detection_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ClashDetectionMode() As boolean
                |     Returns or sets the view Clash Detection mode. Requiring or not extra
                |     computation to proceed with possible clashes existing in
                |     geometry.
                | 
                |     Example:
                | 
                |          This example sets the view pattern mode of the
                |          MyViewProp
                |          generative view properties to indicate that pattern must be
                |          generated.
                |          
                | 
                |          MyViewProp.ClashDetectionMode = true

        :return: bool
        """

        return self.com_object.ClashDetectionMode

    @clash_detection_mode.setter
    def clash_detection_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ClashDetectionMode = value

    @property
    def color_inheritance_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ColorInheritanceMode() As Cat3DColorInheritanceMode
                |     Returns or sets the view color inheritance mode.
                | 
                |     Example:
                | 
                |          This example sets the view color inheritance mode of the
                |          MyViewProp
                |          generative view properties to cat3DColorInheritanceModeOn to indicate
                |          that
                |          generated items inherit the color of the 3D elements they come
                |          from.
                |          
                | 
                |          MyViewProp.ColorInheritanceMode = cat3DColorInheritanceModeOn

        :return: int
        """

        return self.com_object.ColorInheritanceMode

    @color_inheritance_mode.setter
    def color_inheritance_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.ColorInheritanceMode = value

    @property
    def fillet_representation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FilletRepresentation() As CatFilletRepresentation
                |     Returns or sets the view fillet representation mode. The fillet
                |     representation mode indicates how to draw the 3D fillet.
                | 
                |     Example:
                | 
                |          This example sets the view fillet representation mode of the
                |          MyViewProp
                |          generative view properties to catFilletRepSymbolic to indicate that
                |          fillet must
                |          be drawn as symbolic.
                |          
                | 
                |          MyViewProp.FilletRepresentation = catFilletRepSymbolic

        :return: int
        """

        return self.com_object.FilletRepresentation

    @fillet_representation.setter
    def fillet_representation(self, value: int):
        """
        :param int value:
        """

        self.com_object.FilletRepresentation = value

    @property
    def hidden_line_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HiddenLineMode() As CatHiddenLineMode
                |     Returns or sets the view hidden line drawing mode. The hidden line drawing
                |     mode indicates whether to draw the hidden lines.
                | 
                |     Example:
                | 
                |          This example sets the view hidden line drawing mode of the
                |          MyViewProp
                |          generative view properties to catHLRModeOn to indicate that hidden
                |          lines must not
                |          be drawn.
                |          
                | 
                |          MyViewProp.HiddenLineMode = catHLRModeOn

        :return: int
        """

        return self.com_object.HiddenLineMode

    @hidden_line_mode.setter
    def hidden_line_mode(self, value: int):
        """
        :param CatHiddenLineMode value:
        """

        self.com_object.HiddenLineMode = value

    @property
    def image_print_precision_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ImagePrintPrecisionMode() As RasterLevelOfDetail
                |     Returns or sets the print precision mode for views generated as pixel image
                |     (DPI). see ImageViewMode
                | 
                |     Example:
                | 
                |          This example sets the print precision mode of the
                |          MyViewProp
                |          generative view properties to HighQuality.
                |          
                | 
                |          MyViewProp.ImagePrintPrecisionMode = HighQuality

        :return: int
        """

        return self.com_object.ImagePrintPrecisionMode

    @image_print_precision_mode.setter
    def image_print_precision_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.ImagePrintPrecisionMode = value

    @property
    def image_view_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ImageViewMode() As CatGenViewRasterMode
                |     Returns or sets the representation mode for views generated as pixel image.
                |     see RepresentationMode
                | 
                |     Example:
                | 
                |          This example sets the representation mode of the
                |          MyViewProp
                |          generative view properties to catImageShadingEdges to inicate
                |          
                |          that thew view is generated as an image with shading and
                |          edges.
                |          
                | 
                |          MyViewProp.ImageVisuPrecisionMode = catImageShadingEdges

        :return: int
        """

        return self.com_object.ImageViewMode

    @image_view_mode.setter
    def image_view_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.ImageViewMode = value

    @property
    def image_visu_precision_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ImageVisuPrecisionMode() As RasterLevelOfDetail
                |     Returns or sets the visualization precision mode for views generated as
                |     pixel image (DPI). see ImageViewMode
                | 
                |     Example:
                | 
                |          This example sets the visualization precision mode of the
                |          MyViewProp
                |          generative view properties to NormalQuality.
                |          
                | 
                |          MyViewProp.ImageVisuPrecisionMode = NormalQuality

        :return: int
        """

        return self.com_object.ImageVisuPrecisionMode

    @image_visu_precision_mode.setter
    def image_visu_precision_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.ImageVisuPrecisionMode = value

    @property
    def limit_bounding_box(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LimitBoundingBox() As double
                |     Returns or sets the bounding box limits under which a part. will not be
                |     taken into account during view generation. The value 0. means that no part will
                |     be filtered.

        :return: float
        """

        return self.com_object.LimitBoundingBox

    @limit_bounding_box.setter
    def limit_bounding_box(self, value: float):
        """
        :param float value:
        """

        self.com_object.LimitBoundingBox = value

    @property
    def occlusion_culling_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OcclusionCullingMode() As boolean
                |     Returns or sets the view occlusion culling mode. The occlusion culling mode
                |     allows to load only the parts that will be seen in the resulting view
                |     .
                | 
                |     Example:
                | 
                |          This example sets the occlusion culling mode of the
                |          MyViewProp
                |          generative view properties to indicate that the optimization must be
                |          done.
                |          
                | 
                |          MyViewProp.OcclusionCullingMode = true

        :return: bool
        """

        return self.com_object.OcclusionCullingMode

    @occlusion_culling_mode.setter
    def occlusion_culling_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.OcclusionCullingMode = value

    @property
    def pattern_generation_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PatternGenerationMode() As boolean
                |     Returns or sets the view pattern generation. The view pattern generation
                |     mode indicates whether to draw the pattern.
                | 
                |     Example:
                | 
                |          This example sets the view pattern mode of the
                |          MyViewProp
                |          generative view properties to indicate that pattern must be
                |          generated.
                |          
                | 
                |          MyViewProp.PatternGenerationMode = true

        :return: bool
        """

        return self.com_object.PatternGenerationMode

    @pattern_generation_mode.setter
    def pattern_generation_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.PatternGenerationMode = value

    @property
    def points_projection_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PointsProjectionMode() As CatPointsProjectionMode
                |     Returns or sets projection mode for 3D points. This mode indicates whether
                |     to project 3D points.
                | 
                |     Example:
                | 
                |          This example sets the points projection mode of the
                |          MyViewProp
                |          generative view properties to catPointsProjectionModeOn to indicate
                |          that 
                |          3D points must be projected.
                |          
                | 
                |          MyViewProp.PointsProjectionMode = catPointsProjectionModeOn

        :return: CatPointsProjectionMode
        """

        return self.com_object.PointsProjectionMode

    @points_projection_mode.setter
    def points_projection_mode(self, value: int):
        """
        :param CatPointsProjectionMode value:
        """

        self.com_object.PointsProjectionMode = value

    @property
    def points_symbol(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PointsSymbol() As short
                |     Returns or sets symbol for projected points. The 0 value means that
                |     projected points inherit the symbol of 3D points they come from.

        :return: int
        """

        return self.com_object.PointsSymbol

    @points_symbol.setter
    def points_symbol(self, value: int):
        """
        :param int value:
        """

        self.com_object.PointsSymbol = value

    @property
    def polyhedral_data_integration(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PolyhedralDataIntegration() As boolean
                |     Returns or sets the integration of polyhedral data into views in Exact
                |     generation mode. To set or unset Shaded background mode on Exact
                |     view.
                | 
                |     Example:
                | 
                |          This example activates the generation of polyhedral 3d data into the
                |          view MyViewProp.
                |          generative view properties to indicate that Exact view with polyhedral
                |          data must be generated.
                |          
                | 
                |          MyViewProp.PolyhedralDataIntegration = true

        :return: bool
        """

        return self.com_object.PolyhedralDataIntegration

    @polyhedral_data_integration.setter
    def polyhedral_data_integration(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.PolyhedralDataIntegration = value

    @property
    def print_precision(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PrintPrecision() As double
                |     Returns or sets the print precision for views generated as pixel image
                |     (DPI). see ImagePrintPrecisionMode
                | 
                |     Example:
                | 
                |          This example sets the print precision of the
                |          MyViewProp
                |          generative view properties to 200.
                |          
                | 
                |          MyViewProp.PrintPrecision = 200.

        :return: float
        """

        return self.com_object.PrintPrecision

    @print_precision.setter
    def print_precision(self, value: float):
        """
        :param float value:
        """

        self.com_object.PrintPrecision = value

    @property
    def representation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RepresentationMode() As CatGenRepresentationMode
                |     Returns or sets generated geometry representation mode.
                | 
                |     Example:
                | 
                |          This example sets the representation mode of the
                |          MyViewProp
                |          generative view properties to catCGRMode to indicate that
                |          
                |          it is generated from CGR data.
                |          
                | 
                |          MyViewProp.RepresentationMode = catCGRMode

        :return: int
        """

        return self.com_object.RepresentationMode

    @representation_mode.setter
    def representation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.RepresentationMode = value

    @property
    def scan_3d_reps_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Scan3DRepsMode() As CatDftGenRepresentationPolicy
                |     Returns or sets 3D rep instances projection strategy.
                | 
                |     Example:
                | 
                |          This example sets the projection strategy of the
                |          MyViewProp
                |          generative view properties to catDftGenAllDesignRepsPolicy to indicate
                |          that 
                |          all design 3D rep instances of the product structure will be
                |          projected.
                |          
                | 
                |          MyViewProp.Scan3DRepsMode = catDftGenAllDesignRepsPolicy

        :return: int
        """

        return self.com_object.Scan3DRepsMode

    @scan_3d_reps_mode.setter
    def scan_3d_reps_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.Scan3DRepsMode = value

    @property
    def shaded_background_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ShadedBackgroundMode() As boolean
                |     Returns or sets the Shaded background mode. To set or unset Shaded
                |     background mode on Exact view.
                | 
                |     Example:
                | 
                |          This example sets the Shaded background mode on the view
                |          MyViewProp.
                |          generative view properties to indicate that shaded background Exact
                |          view must be generated.
                |          
                | 
                |          MyViewProp.ShadedBackgroundModeMode = true

        :return: bool
        """

        return self.com_object.ShadedBackgroundMode

    @shaded_background_mode.setter
    def shaded_background_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ShadedBackgroundMode = value

    @property
    def smooth_edges_generation_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SmoothEdgesGenerationMode() As boolean
                |     Returns or sets the Smooth Edges Generation mode for the
                |     View.
                | 
                |     Example:
                | 
                |          This example sets the Smooth Edges Generation mode of the
                |          MyViewProp
                |          generative view properties to indicate that smooth edges must be
                |          generated.
                |          
                | 
                |          MyViewProp.SmoothEdgesGenerationMode = true

        :return: bool
        """

        return self.com_object.SmoothEdgesGenerationMode

    @smooth_edges_generation_mode.setter
    def smooth_edges_generation_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SmoothEdgesGenerationMode = value

    @property
    def thread_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThreadMode() As boolean
                |     Returns or sets the view thread mode. The thread mode indicates whether to
                |     draw the threads.
                | 
                |     Example:
                | 
                |          This example sets the view thread mode of the
                |          MyViewProp
                |          generative view properties to indicate that threads must be
                |          drawn.
                |          
                | 
                |          MyViewProp.ThreadMode = true

        :return: bool
        """

        return self.com_object.ThreadMode

    @thread_mode.setter
    def thread_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ThreadMode = value

    @property
    def visu_precision(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VisuPrecision() As double
                |     Returns or sets the visualization precision for views generated as pixel
                |     image (DPI). see ImageVisuPrecisionMode
                | 
                |     Example:
                | 
                |          This example sets the visualization precision of the
                |          MyViewProp
                |          generative view properties to 200.
                |          
                | 
                |          MyViewProp.VisuPrecision = 200.

        :return: float
        """

        return self.com_object.VisuPrecision

    @visu_precision.setter
    def visu_precision(self, value: float):
        """
        :param float value:
        """

        self.com_object.VisuPrecision = value

    @property
    def wireframe_extraction_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WireframeExtractionMode() As CatWireframeMode
                |     Returns or sets projection mode for 3D wireframe. This mode indicates
                |     whether to project 3D wireframe.
                | 
                |     Example:
                | 
                |          This example sets the wireframe projection mode of the
                |          MyViewProp
                |          generative view properties to catGenWFAlwaysVisible to indicate that
                |          
                |          3D wireframe must be projected and always visible.
                |          
                | 
                |          MyViewProp.WireframeExtractionMode = catGenWFAlwaysVisible

        :return: int
        """

        return self.com_object.WireframeExtractionMode

    @wireframe_extraction_mode.setter
    def wireframe_extraction_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.WireframeExtractionMode = value

    def retrieve_bck_color_property_for_op(self, ib_is_color_from_3d: bool, op_rgb_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RetrieveBckColorPropertyForOp(boolean ibIsColorFrom3D,CATSafeArrayVariant
                | opRGBValues)

        :param bool ib_is_color_from_3d:
        :param tuple op_rgb_values:
        :return: None
        """
        return self.com_object.RetrieveBckColorPropertyForOp(ib_is_color_from_3d, op_rgb_values)

    def set_bck_color_property_for_op(self, ib_is_color_from_3d: bool, ip_rgb_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBckColorPropertyForOp(boolean ibIsColorFrom3D,CATSafeArrayVariant
                | ipRGBValues)

        :param bool ib_is_color_from_3d:
        :param tuple ip_rgb_values:
        :return: None
        """
        return self.com_object.SetBckColorPropertyForOp(ib_is_color_from_3d, ip_rgb_values)

    def __repr__(self):
        return f'DrawingGenViewProperties(name="{self.name}")'
