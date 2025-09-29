"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.setting_controller import SettingController


class MeasureSettingAtt(SettingController):
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
                |                         MeasureSettingAtt
                | 
                | The interface to access a CATIAMeasureSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_auto_attach_move_status(self, o_auto_update_in_prd: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAutoAttachMoveStatus(long oAutoUpdateInPrd)
                |
                |        Gets the Status whether Automatic update of Measure on the Product is
                |        enabled.
                |
                |      Parameters:
                |          oAutoUpdateInPart
                |               true: Update Enabled
                |               false: Update Disabled
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure
                |          
                |          virtual int MyFunction (int Arg1) = 0;

        :param int o_auto_update_in_prd:
        :return: None
        """
        return self.com_object.GetAutoAttachMoveStatus(o_auto_update_in_prd)

    def get_border_color(self, o_r: int, o_g: int, o_b: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetBorderColor(long oR,long oG,long oB)
                |
                |        Get the the Measure Border Color.
                |
                |      Parameters:
                |          oR
                |             the red component of the color.
                |          oG
                |             the green component of the color.
                |          oB
                |             the blue component of the color.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int o_r:
        :param int o_g:
        :param int o_b:
        :return: None
        """
        return self.com_object.GetBorderColor(o_r, o_g, o_b)

    def get_border_status(self, ochk_border: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetBorderStatus(long ochkBorder)
                |
                |        Gets the Status whether Border of Measure is enabled.
                |
                |      Parameters:
                |          ochkBorder
                |               1: Update Enabled
                |               0: Update Disabled
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int ochk_border:
        :return: None
        """
        return self.com_object.GetBorderStatus(ochk_border)

    def get_fill_status(self, ochk_fill: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetFillStatus(long ochkFill)
                |
                |        Gets the Status whether Fill of Measure is enabled.
                |
                |      Parameters:
                |          ochkFill
                |               1: Update Enabled
                |               0: Update Disabled
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int ochk_fill:
        :return: None
        """
        return self.com_object.GetFillStatus(ochk_fill)

    def get_fill_style(self, o_fill_style: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetFillStyle(long oFillStyle)
                |
                |        get the Fill Style of Measure 
                |
                |      Parameters:
                |          oFillStyle
                |               1: Solid Fill
                |               2: Gradient Left To Right
                |               3: Gradient Right To Left
                |               4: Gradient Top to Bottom
                |               5 : Gradient Bottom to Top
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int o_fill_style:
        :return: None
        """
        return self.com_object.GetFillStyle(o_fill_style)

    def get_line_color(self, o_r: int, o_g: int, o_b: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetLineColor(long oR,long oG,long oB)
                |
                |        Get the Textbox color for Measure. 
                |
                |      Parameters:
                |          oR
                |             the red component of the color.
                |          oG
                |             the green component of the color.
                |          oB
                |             the blue component of the color.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int o_r:
        :param int o_g:
        :param int o_b:
        :return: None
        """
        return self.com_object.GetLineColor(o_r, o_g, o_b)

    def get_line_width(self, o_line_width: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetLineWidth(long oLineWidth)
                |
                |        Get the Line width for Measure
                |
                |      Parameters:
                |          oLineWidth
                |               Line Width.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int o_line_width:
        :return: None
        """
        return self.com_object.GetLineWidth(o_line_width)

    def get_measure_only_shown_elements_status(self, ochk_status: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMeasureOnlyShownElementsStatus(long ochkStatus)
                |
                |        Gets the Status whether Measure Only Shown Elements for Measure is
                |        enabled.
                |
                |      Parameters:
                |          ochkStatus
                |               1: Update Enabled
                |               0: Update Disabled
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int ochk_status:
        :return: None
        """
        return self.com_object.GetMeasureOnlyShownElementsStatus(ochk_status)

    def get_product_update_status(self, o_auto_update_in_prd: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetProductUpdateStatus(long oAutoUpdateInPrd)
                |
                |        Gets the Status whether Automatic update of Measure on the Product is
                |        enabled.
                |
                |      Parameters:
                |          oAutoUpdateInPart
                |               1: Update Enabled
                |               0: Update Disabled
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int o_auto_update_in_prd:
        :return: None
        """
        return self.com_object.GetProductUpdateStatus(o_auto_update_in_prd)

    def get_text_box_color(self, o_r: int, o_g: int, o_b: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTextBoxColor(long oR,long oG,long oB)
                |
                |        Get the Textbox color for Measure. 
                |
                |      Parameters:
                |          oR
                |             the red component of the color.
                |          oG
                |             the green component of the color.
                |          oB
                |             the blue component of the color.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int o_r:
        :param int o_g:
        :param int o_b:
        :return: None
        """
        return self.com_object.GetTextBoxColor(o_r, o_g, o_b)

    def get_text_box_transparency(self, o_transparency: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTextBoxTransparency(long oTransparency)
                |
                |        Get the Measure Text box Tranparency.
                |
                |      Parameters:
                |          oTransparency
                |               Transparency Value.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int o_transparency:
        :return: None
        """
        return self.com_object.GetTextBoxTransparency(o_transparency)

    def get_text_color(self, o_r: int, o_g: int, o_b: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTextColor(long oR,long oG,long oB)
                |
                |        Get the Measure Text Color.
                |
                |      Parameters:
                |          oR
                |             the red component of the color.
                |          oG
                |             the green component of the color.
                |          oB
                |             the blue component of the color.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int o_r:
        :param int o_g:
        :param int o_b:
        :return: None
        """
        return self.com_object.GetTextColor(o_r, o_g, o_b)

    def get_text_font(self, o_string: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTextFont(CATBSTR oString)
                |        Get the Measure Text Font.
                |
                |      Parameters:
                |          oString
                |               Font Name.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param str o_string:
        :return: None
        """
        return self.com_object.GetTextFont(o_string)

    def get_text_font_index(self, o_text_font_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTextFontIndex(long oTextFontIndex)
                |
                |        Get the Measure Text Font Index.
                |
                |      Parameters:
                |          oTextFontIndex
                |               Font Index.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int o_text_font_index:
        :return: None
        """
        return self.com_object.GetTextFontIndex(o_text_font_index)

    def get_text_size(self, o_text_size: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTextSize(float oTextSize)
                |
                |        Get the Measure Text Size.
                |
                |      Parameters:
                |          oTextSize
                |               Text size.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param float o_text_size:
        :return: None
        """
        return self.com_object.GetTextSize(o_text_size)

    def get_tilde_shown_status(self, o_tilde_status: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTildeShownStatus(long oTildeStatus)
                |
                |        Gets the Status whether Tilde Shown for Measure is
                |        enabled.
                |
                |      Parameters:
                |          oTildeStatus
                |               1: Update Enabled
                |               0: Update Disabled
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int o_tilde_status:
        :return: None
        """
        return self.com_object.GetTildeShownStatus(o_tilde_status)

    def set_auto_attach_move_status(self, i_auto_update_in_prd: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAutoAttachMoveStatus(long iAutoUpdateInPrd)
                |
                |        Sets the Status whether Automatic update of Measure on the Product is
                |        enabled.
                |
                |      Parameters:
                |          iAutoUpdateInPart
                |               1: Update Enabled
                |               0: Update Disabled
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int i_auto_update_in_prd:
        :return: None
        """
        return self.com_object.SetAutoAttachMoveStatus(i_auto_update_in_prd)

    def set_border_color(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBorderColor(long iR,long iG,long iB)
                |
                |        Set the Measure Border Color.
                |
                |      Parameters:
                |          iR
                |             the red component of the color.
                |          iG
                |             the green component of the color.
                |          iB
                |             the blue component of the color.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :return: None
        """
        return self.com_object.SetBorderColor(i_r, i_g, i_b)

    def set_border_status(self, ichk_border: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBorderStatus(long ichkBorder)
                |
                |        Sets the Status whether Border of Measure is enabled.
                |
                |      Parameters:
                |          ichkBorder
                |               1: Update Enabled
                |               0: Update Disabled
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int ichk_border:
        :return: None
        """
        return self.com_object.SetBorderStatus(ichk_border)

    def set_fill_status(self, ichk_fill: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFillStatus(long ichkFill)
                |
                |        Sets the Status whether Fill of Measure is enabled.
                |
                |      Parameters:
                |          ichkFill
                |               1: Update Enabled
                |               0: Update Disabled
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int ichk_fill:
        :return: None
        """
        return self.com_object.SetFillStatus(ichk_fill)

    def set_fill_style(self, i_fill_style: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFillStyle(long iFillStyle)
                |
                |        Sets the Fill Style of Measure
                |
                |      Parameters:
                |          iFillStyle
                |               1: Solid Fill
                |               2: Gradient Left To Right
                |               3: Gradient Right To Left
                |               4: Gradient Top to Bottom
                |               5 : Gradient Bottom to Top
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int i_fill_style:
        :return: None
        """
        return self.com_object.SetFillStyle(i_fill_style)

    def set_line_color(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetLineColor(long iR,long iG,long iB)
                |
                |        Set the Line color for Measure. 
                |
                |      Parameters:
                |          iR
                |             the red component of the color.
                |          iG
                |             the green component of the color.
                |          iB
                |             the blue component of the color.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :return: None
        """
        return self.com_object.SetLineColor(i_r, i_g, i_b)

    def set_line_width(self, i_line_width: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetLineWidth(long iLineWidth)
                |
                |        Set the Line width for Measure
                |
                |      Parameters:
                |          iLineWidth
                |               Line Width.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure
                |          
                |          long MyFunction (long Arg1);

        :param int i_line_width:
        :return: None
        """
        return self.com_object.SetLineWidth(i_line_width)

    def set_measure_only_shown_elements_status(self, ichk_status: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMeasureOnlyShownElementsStatus(long ichkStatus)
                |
                |        Sets the Status whether Measure Only Shown Elements for Measure is
                |        enabled.
                |
                |      Parameters:
                |          ichkStatus
                |               1: Update Enabled
                |               0: Update Disabled
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int ichk_status:
        :return: None
        """
        return self.com_object.SetMeasureOnlyShownElementsStatus(ichk_status)

    def set_product_update_status(self, i_auto_update_in_prd: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetProductUpdateStatus(long iAutoUpdateInPrd)
                |
                |        Sets the Status whether Automatic update of Measure on the Product is
                |        enabled.
                |
                |      Parameters:
                |          iAutoUpdateInPart
                |               1: Update Enabled
                |               0: Update Disabled
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int i_auto_update_in_prd:
        :return: None
        """
        return self.com_object.SetProductUpdateStatus(i_auto_update_in_prd)

    def set_text_box_color(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTextBoxColor(long iR,long iG,long iB)
                |
                |        Set the Textbox color for Measure. 
                |
                |      Parameters:
                |          oR
                |             the red component of the color.
                |          oG
                |             the green component of the color.
                |          oB
                |             the blue component of the color.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :return: None
        """
        return self.com_object.SetTextBoxColor(i_r, i_g, i_b)

    def set_text_box_transparency(self, i_transparency: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTextBoxTransparency(long iTransparency)
                |
                |        Set the Measure Text box Tranparency.
                |
                |      Parameters:
                |          iTransparency
                |               Transparency Value.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int i_transparency:
        :return: None
        """
        return self.com_object.SetTextBoxTransparency(i_transparency)

    def set_text_color(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTextColor(long iR,long iG,long iB)
                |
                |        Set the Measure Text Color.
                |
                |      Parameters:
                |          iR
                |             the red component of the color.
                |          iG
                |             the green component of the color.
                |          iB
                |             the blue component of the color.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :return: None
        """
        return self.com_object.SetTextColor(i_r, i_g, i_b)

    def set_text_font(self, i_string: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTextFont(CATBSTR iString)
                |
                |        Set the Measure Text Font.
                |
                |      Parameters:
                |          iString
                |               Font Name.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param str i_string:
        :return: None
        """
        return self.com_object.SetTextFont(i_string)

    def set_text_font_index(self, i_text_font_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTextFontIndex(long iTextFontIndex)
                |
                |        Set the Measure Text Font Index.
                |
                |      Parameters:
                |          oTextFontIndex
                |               Font Index.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param int i_text_font_index:
        :return: None
        """
        return self.com_object.SetTextFontIndex(i_text_font_index)

    def set_text_size(self, i_text_size: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTextSize(float iTextSize)
                |
                |        Set the Measure Text Size.
                |
                |      Pyarameters:
                |          iTextSize
                |               Text size.
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure

        :param float i_text_size:
        :return: None
        """
        return self.com_object.SetTextSize(i_text_size)

    def set_tilde_shown_status(self, i_tilde_status: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTildeShownStatus(long iTildeStatus)
                |
                |        Sets the Status whether Tilde Shown for Measure is
                |        enabled.
                |
                |      Parameters:
                |          iTildeStatus
                |               1: Update Enabled
                |               0: Update Disabled
                |      Returns:
                |           S_OK: Success
                |           E_FAIL: Failure
        :param int i_tilde_status:
        :return: None
        """
        return self.com_object.SetTildeShownStatus(i_tilde_status)

    def __repr__(self):
        return f'MeasureSettingAtt(name="{self.name}")'
