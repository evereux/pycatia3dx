"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class SimShellSectionOptions(CATBaseDispatch):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimShellSectionOptions
                | 
                | Represents the shell section options.
                | Role:After creating the shell section, you can set the various options provided
                | in this interface.
                | Example:
                | 
                |  Given a shell section object, you can set the various
                |  options.
                |  
                | 
                |  Dim oShellSectionOptions As SimShellSectionOptions
                |  Set oShellSectionOptions = oShellSection.GetItem("SimShellSectionOptions")
                |  oShellSectionOptions.SplitByThicknessOffsetFlag = True
                |  oShellSectionOptions.Interval = 0.002
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def interval(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Interval() As double
                |     Returns or sets the thickness grouping value. Quantity: LENGTH, units: m

        :return: float
        """

        return self.com_object.Interval

    @interval.setter
    def interval(self, value: float):
        """
        :param float value:
        """

        self.com_object.Interval = value

    @property
    def interval_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IntervalFlag() As boolean (Read Only)
                |     Returns the flag that determines if the thickness interval range value is
                |     taken as "Unlimited" or as specified by the user.
                |     TRUE: the thickness interval range value is considered as unlimited and
                |     user must not specify any value.
                | 
                |     FALSE: the thickness interval range value is to be specified by
                |     user.

        :return: bool
        """

        return self.com_object.IntervalFlag

    @property
    def round_off_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RoundOffFlag() As boolean
                |     Returns or sets the round off flag that rounds off the thickness or offset
                |     values upto 4 decimal places.
                |     TRUE: the thickness interval range value is rounded off.
                | 
                |     FALSE: the thickness interval range value is not rounded
                |     off.

        :return: bool
        """

        return self.com_object.RoundOffFlag

    @round_off_flag.setter
    def round_off_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.RoundOffFlag = value

    @property
    def split_by_thickness_offset_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SplitByThicknessOffsetFlag() As boolean
                |     Returns or sets the thickness grouping flag that determines whether the
                |     section is to be grouped according to thickness interval or
                |     not.
                |     TRUE: the section will be grouped in different sections.
                | 
                |     FALSE: the section will not be grouped in different
                |     sections.

        :return: bool
        """

        return self.com_object.SplitByThicknessOffsetFlag

    @split_by_thickness_offset_flag.setter
    def split_by_thickness_offset_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SplitByThicknessOffsetFlag = value

    def __repr__(self):
        return f'SimShellSectionOptions()'
