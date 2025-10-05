"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimSolutionControls(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSolutionControls
                | 
                | Represents the Solution Controls object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimSolutionControls as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MySolutionControls As SimSolutionControls
                |      Set MySolutionControls = MyFeatures.Add("SimSolutionControls")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimSolutionControls named
                |     "Solution Controls.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MySolutionControls As SimSolutionControls
                |      Set MySolutionControls = MyFeatures.Item("Solution Controls.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimSolutionControls
                |     as following:
                | 
                |      ...
                |      mySolutionControls = myFeatures.Add("SimSolutionControls")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimSolutionControls named "Solution Controls.1" as
                |     following:
                | 
                |      ...
                |      mySolutionControls = myFeatures.Item("Solution Controls.1")
                |      
                | 
                | See also:
                |     SimFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Activated() As boolean
                |     Returns or sets the activation status.

        :return: bool
        """

        return self.com_object.Activated

    @activated.setter
    def activated(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Activated = value

    @property
    def da(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DA() As double
                |     Returns or sets the cutback factor used when the time integration accuracy
                |     tolerance is exceeded.

        :return: float
        """

        return self.com_object.DA

    @da.setter
    def da(self, value: float):
        """
        :param float value:
        """

        self.com_object.DA = value

    @property
    def db(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DB() As double
                |     Returns or sets the cutback factor for the next increment when too many
                |     equilibrium iterations are used in the current increment.

        :return: float
        """

        return self.com_object.DB

    @db.setter
    def db(self, value: float):
        """
        :param float value:
        """

        self.com_object.DB = value

    @property
    def dc(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DC() As double
                |     Returns or sets the cutback factor used when the logarithmic rate of
                |     convergence predicts that too many equilibrium iterations will be needed.

        :return: float
        """

        return self.com_object.DC

    @dc.setter
    def dc(self, value: float):
        """
        :param float value:
        """

        self.com_object.DC = value

    @property
    def dd(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DD() As double
                |     Returns or sets the increase factor when two consecutive increments
                |     converge in a small number of equilibrium iterations.

        :return: float
        """

        return self.com_object.DD

    @dd.setter
    def dd(self, value: float):
        """
        :param float value:
        """

        self.com_object.DD = value

    @property
    def de(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DE() As double
                |     Returns or sets the minimum ratio of proposed next time increment to the
                |     last successful time increment for extrapolation of the solution vector to take
                |     place.

        :return: float
        """

        return self.com_object.DE

    @de.setter
    def de(self, value: float):
        """
        :param float value:
        """

        self.com_object.DE = value

    @property
    def d_fs(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DFs() As double
                |     Returns or sets the fraction of stability limit used as current time
                |     increment when the time increment exceeds the above factor times the
                |     stability
                |     limit. This value cannot exceed 1.0.

        :return: float
        """

        return self.com_object.DFs

    @d_fs.setter
    def d_fs(self, value: float):
        """
        :param float value:
        """

        self.com_object.DFs = value

    @property
    def dg(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DG() As double
                |     Returns or sets the increase factor for the next time increment, as a ratio
                |     of the average integration accuracy measure over IT
                |     increments to the corresponding tolerance, when the time integration
                |     accuracy measure is less than WG of the tolerance during
                |     IT consecutive increments.

        :return: float
        """

        return self.com_object.DG

    @dg.setter
    def dg(self, value: float):
        """
        :param float value:
        """

        self.com_object.DG = value

    @property
    def dh(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DH() As double
                |     Returns or sets the cutback factor used when element calculations have
                |     problems such as excessive distortion in large-displacement problems.

        :return: float
        """

        return self.com_object.DH

    @dh.setter
    def dh(self, value: float):
        """
        :param float value:
        """

        self.com_object.DH = value

    @property
    def dl(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DL() As double
                |     Returns or sets the minimum ratio of proposed next time increment to DM
                |     times the current time increment for the proposed time
                |     increment to be used in a linear transient problem. This parameter is
                |     intended to avoid excessive decomposition of the system
                |     matrix
                |     and should be less than 1.0.

        :return: float
        """

        return self.com_object.DL

    @dl.setter
    def dl(self, value: float):
        """
        :param float value:
        """

        self.com_object.DL = value

    @property
    def dm(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DM() As double
                |     Returns or sets the maximum time increment increase factor for all cases
                |     except dynamic stress analysis and diffusion-dominated processes.

        :return: float
        """

        return self.com_object.DM

    @dm.setter
    def dm(self, value: float):
        """
        :param float value:
        """

        self.com_object.DM = value

    @property
    def d_mdif(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DMdif() As double
                |     Returns or sets the maximum time increment increase factor for
                |     diffusion-dominated processes (creep, transient heat transfer,
                |     soils
                |     consolidation, transient mass diffusion).

        :return: float
        """

        return self.com_object.DMdif

    @d_mdif.setter
    def d_mdif(self, value: float):
        """
        :param float value:
        """

        self.com_object.DMdif = value

    @property
    def d_mdyn(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DMdyn() As double
                |     Returns or sets the maximum time increment increase factor for dynamic
                |     stress analysis.

        :return: float
        """

        return self.com_object.DMdyn

    @d_mdyn.setter
    def d_mdyn(self, value: float):
        """
        :param float value:
        """

        self.com_object.DMdyn = value

    @property
    def dr(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DR() As double
                |     Returns or sets the maximum allowable ratio of time increment to stability
                |     limit for conditionally stable time integration procedures.

        :return: float
        """

        return self.com_object.DR

    @dr.setter
    def dr(self, value: float):
        """
        :param float value:
        """

        self.com_object.DR = value

    @property
    def ds(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DS() As double
                |     Returns or sets the cutback factor used when too many iterations arise
                |     because of severe discontinuities.

        :return: float
        """

        return self.com_object.DS

    @ds.setter
    def ds(self, value: float):
        """
        :param float value:
        """

        self.com_object.DS = value

    @property
    def dt(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DT() As double
                |     Returns or sets the increase factor for the time increment directly before
                |     a time point or end time of a step is reached.
                |     This parameter is used to avoid the small time increment that is sometimes
                |     necessary to hit a time point or to complete
                |     a step and must be greater than or equal to 1.0. If output or restart data are requested at exact times in a step, the default = 1.25;
                |     otherwise, the default = 1.0.

        :return: float
        """

        return self.com_object.DT

    @dt.setter
    def dt(self, value: float):
        """
        :param float value:
        """

        self.com_object.DT = value

    @property
    def definition(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Definition() As SimSolutionControlsDefinition
                |     Returns or sets the solution controls definition.

        :return: SimSolutionControlsDefinition
        """

        return self.com_object.Definition

    @definition.setter
    def definition(self, value: int):
        """
        :param int value:
        """

        self.com_object.Definition = value

    @property
    def df(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Df() As double
                |     Returns or sets cutback factor used when the solution appears to be
                |     diverging.

        :return: float
        """

        return self.com_object.Df

    @df.setter
    def df(self, value: float):
        """
        :param float value:
        """

        self.com_object.Df = value

    @property
    def discontinuous_analysis_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DiscontinuousAnalysisFlag() As boolean
                |     Returns or sets the discontinuous analysis flag.
                |     TRUE: the analysis has discontinuous behavior.
                |     FALSE: the analysis does not have discontinuous behavior.

        :return: bool
        """

        return self.com_object.DiscontinuousAnalysisFlag

    @discontinuous_analysis_flag.setter
    def discontinuous_analysis_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DiscontinuousAnalysisFlag = value

    @property
    def feature_history(self) -> SimFeatureHistory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FeatureHistory() As SimFeatureHistory (Read Only)
                |     Returns the feature history.

        :return: SimFeatureHistory
        """

        return SimFeatureHistory(self.com_object.FeatureHistory)

    @property
    def ia(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IA() As long
                |     Returns or sets the maximum number of attempts allowed for an increment.

        :return: int
        """

        return self.com_object.IA

    @ia.setter
    def ia(self, value: int):
        """
        :param int value:
        """

        self.com_object.IA = value

    @property
    def ic(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IC() As long
                |     Returns or sets the upper limit on the number of consecutive equilibrium
                |     iterations (without severe discontinuities), based on prediction
                |     of
                |     the logarithmic rate of convergence.

        :return: int
        """

        return self.com_object.IC

    @ic.setter
    def ic(self, value: int):
        """
        :param int value:
        """

        self.com_object.IC = value

    @property
    def ica(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ICA() As long
                |     Returns or sets the maximum number of allowed contact augmentations if the
                |     augmented Lagrange contact constraint enforcement method is specified.

        :return: int
        """

        return self.com_object.ICA

    @ica.setter
    def ica(self, value: int):
        """
        :param int value:
        """

        self.com_object.ICA = value

    @property
    def icj(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ICJ() As long
                |     Returns or sets the maximum number of equilibrium and severe discontinuity
                |     iterations allowed in two consecutive increments
                |     for the time increment to be increased if CONVERT SDI=YES. This parameter
                |     is not used if CONVERT SDI=NO.

        :return: int
        """

        return self.com_object.ICJ

    @icj.setter
    def icj(self, value: int):
        """
        :param int value:
        """

        self.com_object.ICJ = value

    @property
    def ics(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ICS() As long
                |     Returns or sets the maximum number of equilibrium and severe discontinuity
                |     iterations allowed in an increment if CONVERT SDI=YES.
                |     This parameter serves only as a protection against failure of the default
                |     convergence criteria and should rarely
                |     needs to be changed. This parameter is not used if CONVERT SDI=NO.

        :return: int
        """

        return self.com_object.ICS

    @ics.setter
    def ics(self, value: int):
        """
        :param int value:
        """

        self.com_object.ICS = value

    @property
    def ig(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IG() As long
                |     Returns or sets the maximum number of consecutive equilibrium iterations
                |     (without severe discontinuities) allowed in consecutive
                |     increments
                |     for the time increment to be increased.

        :return: int
        """

        return self.com_object.IG

    @ig.setter
    def ig(self, value: int):
        """
        :param int value:
        """

        self.com_object.IG = value

    @property
    def ij(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IJ() As long
                |     Returns or sets the maximum number of severe discontinuity iterations
                |     allowed in two consecutive increments for the
                |     time increment to be increased if CONVERT SDI=NO. This parameter is not
                |     used if CONVERT SDI=YES.

        :return: int
        """

        return self.com_object.IJ

    @ij.setter
    def ij(self, value: int):
        """
        :param int value:
        """

        self.com_object.IJ = value

    @property
    def il(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IL() As long
                |     Returns or sets the number of consecutive equilibrium iterations (without
                |     severe discontinuities) above which the size of the next increment will be
                |     reduced.

        :return: int
        """

        return self.com_object.IL

    @il.setter
    def il(self, value: int):
        """
        :param int value:
        """

        self.com_object.IL = value

    @property
    def ip(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IP() As long
                |     Returns or sets the number of consecutive equilibrium iterations (without
                |     severe discontinuities) after which the residual tolerance is used.

        :return: int
        """

        return self.com_object.IP

    @ip.setter
    def ip(self, value: int):
        """
        :param int value:
        """

        self.com_object.IP = value

    @property
    def ir(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IR() As long
                |     Returns or sets the number of consecutive equilibrium iterations (without
                |     severe discontinuities) at which logarithmic rate of convergence check begins.

        :return: int
        """

        return self.com_object.IR

    @ir.setter
    def ir(self, value: int):
        """
        :param int value:
        """

        self.com_object.IR = value

    @property
    def is_(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IS() As long
                |     Returns or sets the maximum number of severe discontinuity iterations
                |     allowed in an increment if CONVERT SDI=NO.
                |     This parameter is not used if CONVERT SDI=YES.

        :return: int
        """

        return self.com_object.IS

    @is_.setter
    def is_(self, value: int):
        """
        :param int value:
        """

        self.com_object.IS = value

    @property
    def it(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IT() As long
                |     Returns or sets the minimum number of consecutive increments in which the
                |     time integration accuracy measure must be satisfied
                |     without any cutbacks to allow a time increment increase.

        :return: int
        """

        return self.com_object.IT

    @it.setter
    def it(self, value: int):
        """
        :param int value:
        """

        self.com_object.IT = value

    @property
    def io(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Io() As long
                |     Returns or sets the number of equilibrium iterations (without severe
                |     discontinuities) after which the check is made whether
                |     the residuals are increasing in two consecutive iterations.

        :return: int
        """

        return self.com_object.Io

    @io.setter
    def io(self, value: int):
        """
        :param int value:
        """

        self.com_object.Io = value

    @property
    def time_values_default_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeValuesDefaultFlag() As boolean (Read Only)
                |     Returns the flag that determines whether the time incrementation values are
                |     default or not.
                |     TRUE: the values are default.
                |     FALSE: the values are not default.

        :return: bool
        """

        return self.com_object.TimeValuesDefaultFlag

    @property
    def wg(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WG() As double
                |     Returns or sets the ratio of average time integration accuracy measure over
                |     increments to the corresponding tolerance for the
                |     next allowable time increment to be increased.

        :return: float
        """

        return self.com_object.WG

    @wg.setter
    def wg(self, value: float):
        """
        :param float value:
        """

        self.com_object.WG = value

    def clear_initial_average_flux_value(self, i_dof_field: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ClearInitialAverageFluxValue(SimSolutionControlsDOFField
                | iDOFField)
                |     Clears the initial average flux value.

        :param int i_dof_field:
        :return: None
        """
        return self.com_object.ClearInitialAverageFluxValue(i_dof_field)

    def clear_total_average_flux_value(self, i_dof_field: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ClearTotalAverageFluxValue(SimSolutionControlsDOFField
                | iDOFField)
                |     Clears the total average flux value.

        :param int i_dof_field:
        :return: None
        """
        return self.com_object.ClearTotalAverageFluxValue(i_dof_field)

    def get_average_flux(self, i_dof_field: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAverageFlux(SimSolutionControlsDOFField iDOFField) As
                | SimSolutionControlsAverageFlux
                |     Retrieves the average flux for the field.
                | 
                |     Parameters:
                | 
                |         iDOFField[in]
                |             The field. 
                |         oAverageFlux[out]
                |             The average flux.

        :param int i_dof_field:
        :return: SimSolutionControlsAverageFlux
        """
        return self.com_object.GetAverageFlux(i_dof_field)

    def get_c_alpha_eps(self, i_dof_field: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCAlphaEps(SimSolutionControlsDOFField iDOFField) As
                | double
                |     Retrieves the convergence criterion for the ratio of the largest solution
                |     correction to the largest corresponding incremental
                |     solution
                |     value when there is zero flux in the model.

        :param int i_dof_field:
        :return: float
        """
        return self.com_object.GetCAlphaEps(i_dof_field)

    def get_c_alpha_n(self, i_dof_field: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCAlphaN(SimSolutionControlsDOFField iDOFField) As
                | double
                |     Retrieves the convergence criterion for the ratio of the largest solution
                |     correction to the largest corresponding incremental solution value.

        :param int i_dof_field:
        :return: float
        """
        return self.com_object.GetCAlphaN(i_dof_field)

    def get_conversion_ratio(self, i_dof_field: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetConversionRatio(SimSolutionControlsDOFField iDOFField) As
                | double
                |     Retrieves the field conversion ratio used in scaling the relationship
                |     between two active fields when one is of negligible magnitude.

        :param int i_dof_field:
        :return: float
        """
        return self.com_object.GetConversionRatio(i_dof_field)

    def get_eps_alpha(self, i_dof_field: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetEpsAlpha(SimSolutionControlsDOFField iDOFField) As
                | double
                |     Retrieves the criterion for zero flux compared to average flux.

        :param int i_dof_field:
        :return: float
        """
        return self.com_object.GetEpsAlpha(i_dof_field)

    def get_eps_alpha_d(self, i_dof_field: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetEpsAlphaD(SimSolutionControlsDOFField iDOFField) As
                | double
                |     Retrieves the criterion for zero displacement increment (and/or zero
                |     penetration if CONVERT SDI=YES) compared to the characteristic
                |     element
                |     length in the model. This item is used only when FIELD=DISPLACEMENT.

        :param int i_dof_field:
        :return: float
        """
        return self.com_object.GetEpsAlphaD(i_dof_field)

    def get_eps_alpha_l(self, i_dof_field: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetEpsAlphaL(SimSolutionControlsDOFField iDOFField) As
                | double
                |     Retrieves the criterion for zero flux compared to the time averaged value
                |     of the largest flux in the model during the current step.

        :param int i_dof_field:
        :return: float
        """
        return self.com_object.GetEpsAlphaL(i_dof_field)

    def get_field_values_default_flag(self, i_dof_field: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFieldValuesDefaultFlag(SimSolutionControlsDOFField iDOFField) As
                | boolean
                |     Retrieves the flag that determines whether the field equation values are
                |     default or not.

        :param int i_dof_field:
        :return: bool
        """
        return self.com_object.GetFieldValuesDefaultFlag(i_dof_field)

    def get_initial_average_flux(self, i_dof_field: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInitialAverageFlux(SimSolutionControlsDOFField iDOFField) As
                | double
                |     Retrieves the initial average flux for the field.
                | 
                |     Parameters:
                | 
                |         iDOFField[in]
                |             The field. 
                |         oInitialAverageFlux[out]
                |             The initial average flux.

        :param int i_dof_field:
        :return: float
        """
        return self.com_object.GetInitialAverageFlux(i_dof_field)

    def get_initial_average_flux_has_value_flag(self, i_dof_field: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInitialAverageFluxHasValueFlag(SimSolutionControlsDOFField iDOFField)
                | As boolean
                |     Retrieves the flag that determines whether the initial average flux has a
                |     value.

        :param int i_dof_field:
        :return: bool
        """
        return self.com_object.GetInitialAverageFluxHasValueFlag(i_dof_field)

    def get_r_alpha_l(self, i_dof_field: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRAlphaL(SimSolutionControlsDOFField iDOFField) As
                | double
                |     Retrieves the convergence criterion for the ratio of the largest (scaled)
                |     residual to the corresponding average flux norm for
                |     convergence
                |     to be accepted in one iteration (that is, for a linear case).

        :param int i_dof_field:
        :return: float
        """
        return self.com_object.GetRAlphaL(i_dof_field)

    def get_r_alpha_n(self, i_dof_field: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRAlphaN(SimSolutionControlsDOFField iDOFField) As
                | double
                |     Retrieves the convergence criterion for the ratio of the largest (scaled)
                |     residual to the corresponding average flux norm for convergence.

        :param int i_dof_field:
        :return: float
        """
        return self.com_object.GetRAlphaN(i_dof_field)

    def get_r_alpha_p(self, i_dof_field: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRAlphaP(SimSolutionControlsDOFField iDOFField) As
                | double
                |     Retrieves the alternative residual convergence criterion to be used after
                |     IP iterations.

        :param int i_dof_field:
        :return: float
        """
        return self.com_object.GetRAlphaP(i_dof_field)

    def get_total_average_flux(self, i_dof_field: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTotalAverageFlux(SimSolutionControlsDOFField iDOFField) As
                | double
                |     Retrieves the total average flux for the field.

        :param int i_dof_field:
        :return: float
        """
        return self.com_object.GetTotalAverageFlux(i_dof_field)

    def get_total_average_flux_has_value_flag(self, i_dof_field: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTotalAverageFluxHasValueFlag(SimSolutionControlsDOFField iDOFField) As
                | boolean
                |     Retrieves the flag that determines whether the total average flux has a
                |     value.

        :param int i_dof_field:
        :return: bool
        """
        return self.com_object.GetTotalAverageFluxHasValueFlag(i_dof_field)

    def propagate_from_previous(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PropagateFromPrevious()
                |     Propagates all the values from the previous solution controls feature into
                |     this feature.

        :return: None
        """
        return self.com_object.PropagateFromPrevious()

    def reset_field_values(self, i_dof_field: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ResetFieldValues(SimSolutionControlsDOFField iDOFField)
                |     Resets all the field equation values to default values.

        :param int i_dof_field:
        :return: None
        """
        return self.com_object.ResetFieldValues(i_dof_field)

    def reset_time_values(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ResetTimeValues()
                |     Resets all the time incrementation values to default values.

        :return: None
        """
        return self.com_object.ResetTimeValues()

    def set_average_flux(self, i_dof_field: int, i_average_flux: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAverageFlux(SimSolutionControlsDOFField
                | iDOFField,SimSolutionControlsAverageFlux iAverageFlux)
                |     Sets the average flux for the field.
                | 
                |     Parameters:
                | 
                |         iDOFField[in]
                |             The field. 
                |         iAverageFlux[in]
                |             The average flux. ... .

        :param int i_dof_field:
        :param int i_average_flux:
        :return: None
        """
        return self.com_object.SetAverageFlux(i_dof_field, i_average_flux)

    def set_c_alpha_eps(self, i_dof_field: int, i_c_alpha_eps: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCAlphaEps(SimSolutionControlsDOFField iDOFField,double
                | iCAlphaEps)
                |     Sets the convergence criterion for the ratio of the largest solution
                |     correction to the largest corresponding incremental
                |     solution
                |     value when there is zero flux in the model.

        :param int i_dof_field:
        :param float i_c_alpha_eps:
        :return: None
        """
        return self.com_object.SetCAlphaEps(i_dof_field, i_c_alpha_eps)

    def set_c_alpha_n(self, i_dof_field: int, i_c_alpha_n: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCAlphaN(SimSolutionControlsDOFField iDOFField,double
                | iCAlphaN)
                |     Sets the convergence criterion for the ratio of the largest solution
                |     correction to the largest corresponding incremental solution value.

        :param int i_dof_field:
        :param float i_c_alpha_n:
        :return: None
        """
        return self.com_object.SetCAlphaN(i_dof_field, i_c_alpha_n)

    def set_conversion_ratio(self, i_dof_field: int, i_conversion_ratio: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetConversionRatio(SimSolutionControlsDOFField iDOFField,double
                | iConversionRatio)
                |     Sets the field conversion ratio used in scaling the relationship between
                |     two active fields when one is of negligible magnitude.

        :param int i_dof_field:
        :param float i_conversion_ratio:
        :return: None
        """
        return self.com_object.SetConversionRatio(i_dof_field, i_conversion_ratio)

    def set_eps_alpha(self, i_dof_field: int, i_eps_alpha: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetEpsAlpha(SimSolutionControlsDOFField iDOFField,double
                | iEpsAlpha)
                |     Sets the criterion for zero flux compared to average flux.

        :param int i_dof_field:
        :param float i_eps_alpha:
        :return: None
        """
        return self.com_object.SetEpsAlpha(i_dof_field, i_eps_alpha)

    def set_eps_alpha_d(self, i_dof_field: int, i_eps_alpha_d: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetEpsAlphaD(SimSolutionControlsDOFField iDOFField,double
                | iEpsAlphaD)
                |     Sets the criterion for zero displacement increment (and/or zero penetration
                |     if CONVERT SDI=YES) compared to the characteristic element
                |     length in the model. This item is used only when FIELD=DISPLACEMENT.

        :param int i_dof_field:
        :param float i_eps_alpha_d:
        :return: None
        """
        return self.com_object.SetEpsAlphaD(i_dof_field, i_eps_alpha_d)

    def set_eps_alpha_l(self, i_dof_field: int, i_eps_alpha_l: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetEpsAlphaL(SimSolutionControlsDOFField iDOFField,double
                | iEpsAlphaL)
                |     Sets the criterion for zero flux compared to the time averaged value of the
                |     largest flux in the model during the current step.

        :param int i_dof_field:
        :param float i_eps_alpha_l:
        :return: None
        """
        return self.com_object.SetEpsAlphaL(i_dof_field, i_eps_alpha_l)

    def set_initial_average_flux(self, i_dof_field: int, i_initial_average_flux: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInitialAverageFlux(SimSolutionControlsDOFField iDOFField,double
                | iInitialAverageFlux)
                |     Sets the initial average flux for the field.
                | 
                |     Parameters:
                | 
                |         iDOFField[in]
                |             The field. 
                |         iInitialAverageFlux[in]
                |             The initial average flux.

        :param int i_dof_field:
        :param float i_initial_average_flux:
        :return: None
        """
        return self.com_object.SetInitialAverageFlux(i_dof_field, i_initial_average_flux)

    def set_r_alpha_l(self, i_dof_field: int, i_r_alpha_l: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRAlphaL(SimSolutionControlsDOFField iDOFField,double
                | iRAlphaL)
                |     Sets the convergence criterion for the ratio of the largest (scaled)
                |     residual to the corresponding average flux norm for
                |     convergence
                |     to be accepted in one iteration (that is, for a linear case).

        :param int i_dof_field:
        :param float i_r_alpha_l:
        :return: None
        """
        return self.com_object.SetRAlphaL(i_dof_field, i_r_alpha_l)

    def set_r_alpha_n(self, i_dof_field: int, i_r_alpha_n: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRAlphaN(SimSolutionControlsDOFField iDOFField,double
                | iRAlphaN)
                |     Sets the convergence criterion for the ratio of the largest (scaled)
                |     residual to the corresponding average flux norm for convergence.

        :param int i_dof_field:
        :param float i_r_alpha_n:
        :return: None
        """
        return self.com_object.SetRAlphaN(i_dof_field, i_r_alpha_n)

    def set_r_alpha_p(self, i_dof_field: int, i_r_alpha_p: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRAlphaP(SimSolutionControlsDOFField iDOFField,double
                | iRAlphaP)
                |     Sets the alternative residual convergence criterion to be used after IP
                |     iterations.

        :param int i_dof_field:
        :param float i_r_alpha_p:
        :return: None
        """
        return self.com_object.SetRAlphaP(i_dof_field, i_r_alpha_p)

    def set_total_average_flux(self, i_dof_field: int, i_total_average_flux: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTotalAverageFlux(SimSolutionControlsDOFField iDOFField,double
                | iTotalAverageFlux)
                |     Sets the total average flux for the field. 

        :param int i_dof_field:
        :param float i_total_average_flux:
        :return: None
        """
        return self.com_object.SetTotalAverageFlux(i_dof_field, i_total_average_flux)

    def __repr__(self):
        return f'SimSolutionControls(name="{ self.name }")'
