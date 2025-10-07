"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.setting_controller import SettingController


class SectioningSettingAtt(SettingController):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         SectioningSettingAtt
                | 
                | The interface to access a CATIASectioningSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_export_mode(self, o_export_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetExportMode(long oExportMode)
                |     Returns the export mode.
                | 
                |     Parameters:
                | 
                |         oExportMode
                |             the export mode
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int o_export_mode:
        :return: None
        """
        return self.com_object.GetExportMode(o_export_mode)

    def get_only_plane_dyn_mode(self, o_only_plane_dyn_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetOnlyPlaneDynMode(long oOnlyPlaneDynMode)
                |     Returns the plane dynamic mode.
                | 
                |     Parameters:
                | 
                |         oOnlyPlaneDynMode
                |             the plane dynamic mode
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int o_only_plane_dyn_mode:
        :return: None
        """
        return self.com_object.GetOnlyPlaneDynMode(o_only_plane_dyn_mode)

    def get_plane_color(self, o_r: int, o_g: int, o_b: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPlaneColor(long oR,long oG,long oB)
                |     Returns the PlaneColor parameter.
                | 
                |     Parameters:
                | 
                |         oR
                |             the red component of the color. 
                |         oG
                |             the green component of the color. 
                |         oB
                |             the blue component of the color.
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int o_r:
        :param int o_g:
        :param int o_b:
        :return: None
        """
        return self.com_object.GetPlaneColor(o_r, o_g, o_b)

    def get_plane_transparency(self, o_plane_transparency: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPlaneTransparency(long oPlaneTransparency)
                |     Returns the PlaneTransperency parameter.
                | 
                |     Parameters:
                | 
                |         oPlaneTransparency
                |             the transperency
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int o_plane_transparency:
        :return: None
        """
        return self.com_object.GetPlaneTransparency(o_plane_transparency)

    def get_section_contour_color(self, o_r: int, o_g: int, o_b: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSectionContourColor(long oR,long oG,long oB)
                |     Returns the Section Contour Color parameter.
                | 
                |     Parameters:
                | 
                |         oR
                |             the red component of the color. 
                |         oG
                |             the green component of the color. 
                |         oB
                |             the blue component of the color.
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int o_r:
        :param int o_g:
        :param int o_b:
        :return: None
        """
        return self.com_object.GetSectionContourColor(o_r, o_g, o_b)

    def get_section_contour_dominant_status(self, o_contour_dominant_status: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSectionContourDominantStatus(long
                | oContourDominantStatus)
                |     Returns the Contour Dominant Status parameter.
                | 
                |     Parameters:
                | 
                |         oContourDominantStatus
                |             the Contour Dominant Status
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int o_contour_dominant_status:
        :return: None
        """
        return self.com_object.GetSectionContourDominantStatus(o_contour_dominant_status)

    def get_section_info_disp_mode(self, o_section_info_disp_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSectionInfoDispMode(long oSectionInfoDispMode)
                |     Returns the Section Plane Info Display parameter.
                | 
                |     Parameters:
                | 
                |         oSectionInfoDispMode
                |             the Section Plane Info Display
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int o_section_info_disp_mode:
        :return: None
        """
        return self.com_object.GetSectionInfoDispMode(o_section_info_disp_mode)

    def get_section_mode(self, o_grid_view: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSectionMode(CATSectioningMode oGridView)
                |     Returns the Sectioning Mode.
                | 
                |     Parameters:
                | 
                |         oGridView
                |             the Section Mode
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int o_grid_view:
        :return: None
        """
        return self.com_object.GetSectionMode(o_grid_view)

    def get_section_plane_visu_mode(self, o_plane_visu_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSectionPlaneVisuMode(CATSectioningPlaneVisuMode
                | oPlaneVisuMode)
                |     Returns the Plane visu mode parameter.
                | 
                |     Parameters:
                | 
                |         oPlaneVisuMode
                |             the plane visu mode
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int o_plane_visu_mode:
        :return: None
        """
        return self.com_object.GetSectionPlaneVisuMode(o_plane_visu_mode)

    def get_section_update_mode(self, o_section_update_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSectionUpdateMode(long oSectionUpdateMode)
                |     Returns the Section Update Mode parameter.
                | 
                |     Parameters:
                | 
                |         oSectionUpdateMode
                |             Section Update Mode
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int o_section_update_mode:
        :return: None
        """
        return self.com_object.GetSectionUpdateMode(o_section_update_mode)

    def get_thickness_line(self, o_thickness_line: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetThicknessLine(long oThicknessLine)
                |     Returns the Thickness Line.
                | 
                |     Parameters:
                | 
                |         oThicknessLine
                |             the thickness
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int o_thickness_line:
        :return: None
        """
        return self.com_object.GetThicknessLine(o_thickness_line)

    def set_export_mode(self, i_export_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetExportMode(long iExportMode)
                |     Sets the export mode.
                | 
                |     Parameters:
                | 
                |         iExportMode
                |             the export mode
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int i_export_mode:
        :return: None
        """
        return self.com_object.SetExportMode(i_export_mode)

    def set_only_plane_dyn_mode(self, i_only_plane_dyn_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOnlyPlaneDynMode(long iOnlyPlaneDynMode)
                |     Sets the plane dynamic mode.
                | 
                |     Parameters:
                | 
                |         iOnlyPlaneDynMode
                |             the plane dynamic mode
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int i_only_plane_dyn_mode:
        :return: None
        """
        return self.com_object.SetOnlyPlaneDynMode(i_only_plane_dyn_mode)

    def set_plane_color(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPlaneColor(long iR,long iG,long iB)
                |     Sets the PlaneColor parameter.
                | 
                |     Parameters:
                | 
                |         iR
                |             the red component of the color. 
                |         iG
                |             the green component of the color. 
                |         iB
                |             the blue component of the color.
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :return: None
        """
        return self.com_object.SetPlaneColor(i_r, i_g, i_b)

    def set_plane_transparency(self, i_plane_transparency: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPlaneTransparency(long iPlaneTransparency)
                |     Sets the PlaneTransperency parameter.
                | 
                |     Parameters:
                | 
                |         iPlaneTransparency
                |             the transperency
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int i_plane_transparency:
        :return: None
        """
        return self.com_object.SetPlaneTransparency(i_plane_transparency)

    def set_section_contour_color(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSectionContourColor(long iR,long iG,long iB)
                |     Sets the Section Contour Color parameter.
                | 
                |     Parameters:
                | 
                |         iR
                |             the red component of the color. 
                |         iG
                |             the green component of the color. 
                |         iB
                |             the blue component of the color.
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :return: None
        """
        return self.com_object.SetSectionContourColor(i_r, i_g, i_b)

    def set_section_contour_dominant_status(self, i_contour_dominant_status: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSectionContourDominantStatus(long
                | iContourDominantStatus)
                |     Sets the Contour Dominant Status parameter.
                | 
                |     Parameters:
                | 
                |         iContourDominantStatus
                |             the Contour Dominant Status
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int i_contour_dominant_status:
        :return: None
        """
        return self.com_object.SetSectionContourDominantStatus(i_contour_dominant_status)

    def set_section_info_disp_mode(self, i_section_info_disp_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSectionInfoDispMode(long iSectionInfoDispMode)
                |     Sets the Section Plane Info Display parameter.
                | 
                |     Parameters:
                | 
                |         iSectionInfoDispMode
                |             the Section Plane Info Display
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int i_section_info_disp_mode:
        :return: None
        """
        return self.com_object.SetSectionInfoDispMode(i_section_info_disp_mode)

    def set_section_mode(self, i_section_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSectionMode(CATSectioningMode iSectionMode)
                |     Sets the Sectioning Mode.
                | 
                |     Parameters:
                | 
                |         iSectionMode
                |             the Section Mode
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int i_section_mode:
        :return: None
        """
        return self.com_object.SetSectionMode(i_section_mode)

    def set_section_plane_visu_mode(self, i_plane_visu_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSectionPlaneVisuMode(CATSectioningPlaneVisuMode
                | iPlaneVisuMode)
                |     Sets the Plane visu mode parameter.
                | 
                |     Parameters:
                | 
                |         iPlaneVisuMode
                |             the plane visu mode
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int i_plane_visu_mode:
        :return: None
        """
        return self.com_object.SetSectionPlaneVisuMode(i_plane_visu_mode)

    def set_section_update_mode(self, i_section_update_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSectionUpdateMode(long iSectionUpdateMode)
                |     Sets the Section Update Mode parameter.
                | 
                |     Parameters:
                | 
                |         iSectionUpdateMode
                |             Section Update Mode
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int i_section_update_mode:
        :return: None
        """
        return self.com_object.SetSectionUpdateMode(i_section_update_mode)

    def set_thickness_line(self, i_thickness_line: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetThicknessLine(long iThicknessLine)
                |     Sets the thickness parameter.
                | 
                |     Parameters:
                | 
                |         iThicknessLine
                |             the thickness
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated. 

        :param int i_thickness_line:
        :return: None
        """
        return self.com_object.SetThicknessLine(i_thickness_line)

    def __repr__(self):
        return f'SectioningSettingAtt(name="{ self.name }")'
