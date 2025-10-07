"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class PcbComponent(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PCBComponent

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def capacitance(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CAPACITANCE() As CATBSTR
                |     Gets and sets the CAPACITANCE Type of a component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.CAPACITANCE

    @capacitance.setter
    def capacitance(self, value: str):
        """
        :param str value:
        """

        self.com_object.CAPACITANCE = value

    @property
    def poweropr(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property POWEROPR() As CATBSTR
                |     Gets and sets the Operating power rating of a component. The possible value
                |     are MECHANICAL or ELECTRICAL
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.POWEROPR

    @poweropr.setter
    def poweropr(self, value: str):
        """
        :param str value:
        """

        self.com_object.POWEROPR = value

    @property
    def power_max(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property POWER_MAX() As CATBSTR
                |     Gets and sets the POWER MAX of a component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.POWER_MAX

    @power_max.setter
    def power_max(self, value: str):
        """
        :param str value:
        """

        self.com_object.POWER_MAX = value

    @property
    def package_number(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PackageNumber() As CATBSTR
                |     Gets and sets the Package number of a component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.PackageNumber

    @package_number.setter
    def package_number(self, value: str):
        """
        :param str value:
        """

        self.com_object.PackageNumber = value

    @property
    def resistance(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RESISTANCE() As CATBSTR
                |     Gets and sets the RESISTANCE of a component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.RESISTANCE

    @resistance.setter
    def resistance(self, value: str):
        """
        :param str value:
        """

        self.com_object.RESISTANCE = value

    @property
    def therm_cond(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property THERM_COND() As CATBSTR
                |     Gets and sets the thermal conductivity of a component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.THERM_COND

    @therm_cond.setter
    def therm_cond(self, value: str):
        """
        :param str value:
        """

        self.com_object.THERM_COND = value

    @property
    def theta_jb(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property THETA_JB() As CATBSTR
                |     Gets and sets the junction to board thermal resistance of a
                |     component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.THETA_JB

    @theta_jb.setter
    def theta_jb(self, value: str):
        """
        :param str value:
        """

        self.com_object.THETA_JB = value

    @property
    def theta_jc(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property THETA_JC() As CATBSTR
                |     Gets and sets junction to case thermal resistance of a
                |     component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.THETA_JC

    @theta_jc.setter
    def theta_jc(self, value: str):
        """
        :param str value:
        """

        self.com_object.THETA_JC = value

    @property
    def tolerance(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TOLERANCE() As CATBSTR
                |     Gets and sets the TOLERANCE of a component.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed 

        :return: str
        """

        return self.com_object.TOLERANCE

    @tolerance.setter
    def tolerance(self, value: str):
        """
        :param str value:
        """

        self.com_object.TOLERANCE = value

    def __repr__(self):
        return f'PcbComponent(name="{ self.name }")'
