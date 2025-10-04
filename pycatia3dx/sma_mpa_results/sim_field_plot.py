"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_results.sim_display_group import SimDisplayGroup
from pycatia3dx.sma_mpa_results.sim_legend import SimLegend


class SimFieldPlot(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimFieldPlot
                | 
                | The field plots shows the display field output data.
                | 
                |  
                | Example:
                | 
                |  Given a SimResultsAnalysisCase object, you can create a SimFieldPlot object as
                |  following.
                |  
                | 
                |  Dim oFieldPlot As SimFieldPlot
                |  Dim PlotID As String
                |  PlotID = "Contour_Stress_Tresca"
                |  Set oFieldPlot = myResultsAnalysisCase.CreateFieldPlotByID(PlotID, True)
                |  
                | 
                | See also:
                |     SimResultsAnalysisCase
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activation_status(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ActivationStatus() As boolean
                |     Returns or sets the activation status of this Data
                |     Display.
                |     When activated a Data Display is displayed in the 3D view.
                |     When deactivated a Data Display is not displayed in the 3D view and its
                |     scene graph memory is freed.

        :return: bool
        """

        return self.com_object.ActivationStatus

    @activation_status.setter
    def activation_status(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ActivationStatus = value

    @property
    def computed_deformation_scale_factor(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ComputedDeformationScaleFactor() As double (Read
                | Only)
                |     Returns the computed default deformation scale factor of this Data
                |     Display.
                |     The deformation scale factor will be used to deformed the 3D representation
                |     of the Data Display along each axis.
                |     This is the default value which is automaticaly computed .
                | 
                |     See also:
                |         SetDeformationScaleFactors, ResetDeformationScaleFactors,
                |         AreScaleFactorsImposed

        :return: float
        """

        return self.com_object.ComputedDeformationScaleFactor

    @property
    def current_frame(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CurrentFrame(long inFrame) (Write Only)
                |     Sets the specified frame as current frame for this Data
                |     Display.
                |     Indicates which result frame to take as reference when displaying or
                |     querying related data from a Data Display.
                | 
                |     See also:
                |         GetCurrentFrame

        :return: bool
        """

        return self.com_object.CurrentFrame

    @current_frame.setter
    def current_frame(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CurrentFrame = value

    @property
    def deformation_status(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DeformationStatus() As boolean
                |     Returns or sets the deformation status of this Data Display. TRUE if the
                |     Data Display is displayed deformed.

        :return: bool
        """

        return self.com_object.DeformationStatus

    @deformation_status.setter
    def deformation_status(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DeformationStatus = value

    @property
    def display_group(self) -> SimDisplayGroup:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DisplayGroup() As SimDisplayGroup
                |     Gets/Sets the display group to the plot.

        :return: SimDisplayGroup
        """

        return SimDisplayGroup(self.com_object.DisplayGroup)

    @display_group.setter
    def display_group(self, value: SimDisplayGroup):
        """
        :param SimDisplayGroup value:
        """

        self.com_object.DisplayGroup = value

    @property
    def field_defination(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FieldDefination() As CATBaseDispatch
                |     Sets the Field Defination to the plot.
                |     The ospDefination will be an SimFieldDefination Interface where the user
                |     can Get/Set all the definations such as variable, quantity, axis
                |     etc.

        :return: AnyObject
        """

        return AnyObject(self.com_object.FieldDefination)

    @field_defination.setter
    def field_defination(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.FieldDefination = value

    @property
    def legend(self) -> SimLegend:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Legend() As SimLegend (Read Only)
                |     Returns the Legend pointing at this Data Display.
                |     The Legend pointing at a Data Display own some of its display
                |     parameters.
                | 
                |     See also:
                |         SimLegend

        :return: SimLegend
        """

        return SimLegend(self.com_object.Legend)

    @property
    def max_deformation_scale_factor(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaxDeformationScaleFactor() As double (Read Only)
                |     Returns the maximum deformation scale factor of this Data
                |     Display.
                |     This setting is dependent on the size and position of the model and the
                |     biggest displacement value.
                |     Setting a larger scale could generate a floating point
                |     exception.
                | 
                |     See also:
                |         SetDeformationScaleFactors, ResetDeformationScaleFactors,
                |         GetComputedDeformationScaleFactor

        :return: float
        """

        return self.com_object.MaxDeformationScaleFactor

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As SimFieldPlotTypes (Read Only)
                |     Returns the plot type.

        :return: int
        """

        return int(self.com_object.Type)

    def are_scale_factors_imposed(self, ib_ignore_anim: bool) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AreScaleFactorsImposed(boolean ibIgnoreAnim) As boolean
                |     Specifies whether the deformation scale factors are imposed or
                |     not.
                | 
                |     Parameters:
                | 
                |         ibIgnoreAnim
                |             If FALSE (default) allow oAreScaleFactorsImposed to be returned as
                |             TRUE even if
                |             the scale was imposed internally for a time-history animation
                |             
                | 
                |     Returns:
                |         The scale factor status. TRUE if they are imposed. 
                |     See also:
                |         GetDeformationScaleFactors, SetDeformationScaleFactors,
                |         ResetDeformationScaleFactors

        :param bool ib_ignore_anim:
        :return: bool
        """
        return self.com_object.AreScaleFactorsImposed(ib_ignore_anim)

    def get_current_frame(self, ib_normalize: bool) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCurrentFrame(boolean ibNormalize) As long
                |     Gets the current frame for this Data Display.
                |     Indicates which result frame will be referenced when displaying or querying
                |     related data from a Data Display.
                | 
                |     Parameters:
                | 
                |         ibNormalize
                |             If TRUE, the default, a negative frame number will be converted to
                |             positive. If FALSE, a negative frame number can be returned. A negative frame
                |             number is always handled internally as counting from the end so -1 is the last
                |             frame in the step. 
                | 
                |     Returns:
                |         The frame number

        :param bool ib_normalize:
        :return: int
        """
        return self.com_object.GetCurrentFrame(ib_normalize)

    def get_deformation_scale_factors(self, o_x_deformation_scale_factor: float, o_y_deformation_scale_factor: float, o_z_deformation_scale_factor: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDeformationScaleFactors(double oXDeformationScaleFactor,double
                | oYDeformationScaleFactor,double oZDeformationScaleFactor)
                |     Gets the deformation scale factors of this Data Display.
                |     The deformation scale factors will be used to deformed the 3D
                |     representation of the Data Display along each axis.
                |     Default values are automaticaly computed but the factors may be
                |     imposed.
                | 
                |     Parameters:
                | 
                |         oXDeformationScaleFactor
                |             The deformation scale factor along X axis 
                |         oYDeformationScaleFactor
                |             The deformation scale factor along Y axis 
                |         oZDeformationScaleFactor
                |             The deformation scale factor along Z axis 
                | 
                |     See also:
                |         SetDeformationScaleFactors, ResetDeformationScaleFactors,
                |         AreScaleFactorsImposed

        :param float o_x_deformation_scale_factor:
        :param float o_y_deformation_scale_factor:
        :param float o_z_deformation_scale_factor:
        :return: None
        """
        return self.com_object.GetDeformationScaleFactors(o_x_deformation_scale_factor, o_y_deformation_scale_factor, o_z_deformation_scale_factor)

    def get_identifier(self, o_field_plot_id: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetIdentifier(CATBSTR oFieldPlotID)
                |     Returns the ID of the field plot as defined in the plot defination XML
                |     file.

        :param str o_field_plot_id:
        :return: None
        """
        return self.com_object.GetIdentifier(o_field_plot_id)

    def get_step_and_frame(self, ocs_step: str, on_frame: int, on_load_case: int, ib_normalize: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetStepAndFrame(CATBSTR ocsStep,long onFrame,long onLoadCase,boolean
                | ibNormalize)
                |     Gets the current step and frame for this Data Display.
                |     Indicates which result output step and frame will be referenced when
                |     displaying or querying related data from a Data Display.
                | 
                |     Parameters:
                | 
                |         ocsStep
                |             The step SIM Persistent ID 
                |         onFrame
                |             The frame within the step 
                |         onLoadCase
                |             The loadcase within the step 
                |         ibNormalize
                |             If TRUE, the default, a negative frame number will be converted to
                |             positive
                |             If FALSE, a negative frame number can be returned. A negative frame
                |             number is always
                |             handled internally as counting from the end so -1 is the last frame
                |             in the step. 
                | 
                |     See also:
                |         SetStepAndFrame

        :param str ocs_step:
        :param int on_frame:
        :param int on_load_case:
        :param bool ib_normalize:
        :return: None
        """
        return self.com_object.GetStepAndFrame(ocs_step, on_frame, on_load_case, ib_normalize)

    def refresh(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Refresh()
                |     Refreshes the Data Display.
                |     This can be called to refresh the plot after properties have been changed
                |     such as in SetCurrentFrame.

        :return: None
        """
        return self.com_object.Refresh()

    def reset_deformation_scale_factors(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ResetDeformationScaleFactors()
                |     Sets the deformation scale factors of this Data Display to their default,
                |     automatically computed, values.
                |     The deformation scale factors will be used to deformed the 3D
                |     representation of the Data Display along each axis.
                | 
                |     See also:
                |         GetDeformationScaleFactors, SetDeformationScaleFactors,
                |         AreScaleFactorsImposed

        :return: None
        """
        return self.com_object.ResetDeformationScaleFactors()

    def set_deformation_scale_factors(self, i_x_deformation_scale_factor: float, i_y_deformation_scale_factor: float, i_z_deformation_scale_factor: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDeformationScaleFactors(double iXDeformationScaleFactor,double
                | iYDeformationScaleFactor,double iZDeformationScaleFactor)
                |     Sets the deformation scale factors of this Data Display.
                |     The deformation scale factors will be used to deformed the 3D
                |     representation of the Data Display along each axis.
                |     To go back to the default values call
                |     ResetDeformationScaleFactors.
                | 
                |     Parameters:
                | 
                |         iXDeformationScaleFactor
                |             The deformation scale factor along X axis 
                |         iYDeformationScaleFactor
                |             The deformation scale factor along Y axis 
                |         iZDeformationScaleFactor
                |             The deformation scale factor along Z axis 
                | 
                |     See also:
                |         GetDeformationScaleFactors, ResetDeformationScaleFactors,
                |         AreScaleFactorsImposed

        :param float i_x_deformation_scale_factor:
        :param float i_y_deformation_scale_factor:
        :param float i_z_deformation_scale_factor:
        :return: None
        """
        return self.com_object.SetDeformationScaleFactors(i_x_deformation_scale_factor, i_y_deformation_scale_factor, i_z_deformation_scale_factor)

    def set_step_and_frame(self, ics_step: str, in_frame: int, in_load_case: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStepAndFrame(CATBSTR icsStep,long inFrame,long
                | inLoadCase)
                |     Sets the current step, frame and load case for this Data
                |     Display.
                |     Indicates which result output step frame and laod case to take as reference
                |     when displaying or querying related data from a Data
                |     Display.
                | 
                |     Parameters:
                | 
                |         icsStep
                |             The step SIM Persistent ID 
                |         inFrame
                |             The frame within the step 
                |         inLoadCase
                |             The loadcase within the step 
                | 
                |     See also:
                |         GetStepAndFrame

        :param str ics_step:
        :param int in_frame:
        :param int in_load_case:
        :return: None
        """
        return self.com_object.SetStepAndFrame(ics_step, in_frame, in_load_case)

    def __repr__(self):
        return f'SimFieldPlot(name="{ self.name }")'
