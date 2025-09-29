"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject


class AssemblyConstraint(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AssemblyConstraint
                | 
                | This interface is implemented by the Assembly Constraint.
                | 
                | Role: Contains API to manage the Assembly Constraint.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Activity() As boolean
                |     Returns/Sets the Assembly Constraint Activity.

        :return: bool
        """

        return self.com_object.Activity

    @activity.setter
    def activity(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Activity = value

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Mode() As CatAssemblyConstraintMode
                |     Sets/Gets the mode of the constraint.

        :return: int
        """

        return self.com_object.Mode

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.Mode = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CatAssemblyConstraintType
                |     Returns/Sets the Assembly Constraint Type.

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def get_max_value(self, inbv: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetMaxValue(short inbv) As double
                |     Gets a maximal value of the constraint.
                | 
                |     Parameters:
                | 
                |         iNbv
                |             [in] The value identifier. 
                |         oValue
                |             [out] The value in CATIA System Units(mm and degrees).
                |             
                | 
                |     Returns:
                | 
                |         TRUE
                |             if the value is defined. 
                |         FALSE
                |             if the value is UNSET.

        :param int inbv:
        :return: float
        """
        return self.com_object.GetMaxValue(inbv)

    def get_max_value_as_param(self, inbv: int) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetMaxValueAsParam(short inbv) As Parameter
                |     Returns the Parameter corresponding to a maximum value of the constraint.

        :param int inbv:
        :return: Parameter
        """
        return Parameter(self.com_object.GetMaxValueAsParam(inbv))

    def get_min_value(self, inbv: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetMinValue(short inbv) As double
                |     Gets a minimal value of the constraint.
                | 
                |     Parameters:
                | 
                |         iNbv
                |             [in] The value identifier. 
                |         oValue
                |             [out] The value in CATIA System Units(mm and degrees).
                |             
                | 
                |     Returns:
                | 
                |         TRUE
                |             if the value is defined. 
                |         FALSE
                |             if the value is UNSET.

        :param int inbv:
        :return: float
        """
        return self.com_object.GetMinValue(inbv)

    def get_min_value_as_param(self, inbv: int) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetMinValueAsParam(short inbv) As Parameter
                |     Returns the Parameter corresponding to a minimum value of the constraint.

        :param int inbv:
        :return: Parameter
        """
        return Parameter(self.com_object.GetMinValueAsParam(inbv))

    def get_nb_options(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetNbOptions() As short
                |     Gets the number of possible options for this constraint.
                | 
                |     Returns:
                | 
                |         The number of the options.

        :return: int
        """
        return self.com_object.GetNbOptions()

    def get_nb_supports(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetNbSupports() As short
                |     Returns number of support.
                | 
                |     Parameters:
                | 
                |         onbSupport
                |             [out] the number of support. 
                | 
                |     Returns:
                | 
                |         the number of support
                |             if the operation is successful. 
                |         Zero
                |             if the operation is failed.

        :return: int
        """
        return self.com_object.GetNbSupports()

    def get_nb_values(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetNbValues() As short
                |     Returns the number of values in the constraint.

        :return: int
        """
        return self.com_object.GetNbValues()

    def get_option(self, inum_option: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetOption(short inumOption) As
                | CatAssemblyConstraintOption
                |     Gets an option of the constraint.
                | 
                |     Parameters:
                | 
                |         inumOption
                |             [in] The value identifier. 
                | 
                |     Returns:
                | 
                |         a CatAssemblyConstraintOption
                |             if the operation is successful. 
                |         nothing
                |             if the operation is failed.

        :param int inum_option:
        :return: int
        """
        return self.com_object.GetOption(inum_option)

    def get_support(self, inum_support: int, ib_fold: bool, o_support: str, o_ctx_support: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetSupport(short inumSupport,boolean ibFold,CATBSTR oSupport,CATBSTR
                | oCtxSupport)
                |     Returns support.
                | 
                |     Parameters:
                | 
                |         inumSupport
                |             [in] the Support number. 
                |         oSupport
                |             [out] the Support as
                |             string:"Product.1\Product.2\Rep1.1\ObjectName". If the Object has no name, the
                |             TypeName is returned. 
                |         oCtxSupport
                |             [out] the context of the Support as string.

        :param int inum_support:
        :param bool ib_fold:
        :param str o_support:
        :param str o_ctx_support:
        :return: None
        """
        return self.com_object.GetSupport(inum_support, ib_fold, o_support, o_ctx_support)

    def get_value(self, inbv: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetValue(short inbv) As double
                |     Gets a value of the constraint.
                | 
                |     Parameters:
                | 
                |         iNbv
                |             [in] The value identifier. 
                |         oValue
                |             [out] The value in CATIA System Units(mm and degrees).
                |
                |     Returns:
                | 
                |         TRUE
                |             if the value is defined. 
                |         FALSE
                |             if the value is UNSET.

        :param int inbv:
        :return: float
        """
        return self.com_object.GetValue(inbv)

    def get_value_as_param(self, inbv: int) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetValueAsParam(short inbv) As Parameter
                |     Returns the Parameter corresponding to a value of the constraint.

        :param int inbv:
        :return: Parameter
        """
        return Parameter(self.com_object.GetValueAsParam(inbv))

    def set_max_value(self, inbv: int, ival: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetMaxValue(short inbv,double ival)
                |     Sets a maximal value of the constraint.
                | 
                |     Parameters:
                | 
                |         iNbv
                |             [in] The value identifier. 
                |         ival
                |             [in] The minimun value in CATIA System Units(mm and degrees).

        :param int inbv:
        :param float ival:
        :return: None
        """
        return self.com_object.SetMaxValue(inbv, ival)

    def set_min_value(self, inbv: int, ival: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetMinValue(short inbv,double ival)
                |     Sets a minimal value of the constraint.
                | 
                |     Parameters:
                | 
                |         iNbv
                |             [in] The value identifier. 
                |         ival
                |             [in] The minimun value in CATIA System Units(mm and degrees).

        :param int inbv:
        :param float ival:
        :return: None
        """
        return self.com_object.SetMinValue(inbv, ival)

    def set_option(self, inum_option: int, ioption: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetOption(short inumOption,CatAssemblyConstraintOption
                | ioption)
                |     Sets the options number of the constraint.
                | 
                |     Parameters:
                | 
                |         inumOption
                |             [in] The value identifier. 
                |         iOption
                |             [in] The option.

        :param int inum_option:
        :param int ioption:
        :return: None
        """
        return self.com_object.SetOption(inum_option, ioption)

    def set_value(self, inbv: int, ival: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetValue(short inbv,double ival)
                |     Sets a value of the constraint.
                | 
                |     Parameters:
                | 
                |         inbv
                |             [in] The value identifier. 
                |         ival
                |             [in] The value in CATIA System Units(mm and degrees).

        :param int inbv:
        :param float ival:
        :return: None
        """
        return self.com_object.SetValue(inbv, ival)

    def __repr__(self):
        return f'AssemblyConstraint(name="{self.name}")'
