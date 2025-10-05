"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimJobDiagnosticSummary(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimJobDiagnosticSummary
                | 
                | Represents the Job Diagnostic Summary object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def number_of_cutbacks(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfCutbacks() As long (Read Only)
                |     Returns the number of cutbacks.

        :return: int
        """

        return self.com_object.NumberOfCutbacks

    @property
    def number_of_do_fs(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfDOFs() As long (Read Only)
                |     Returns the total number of DOFs.

        :return: int
        """

        return self.com_object.NumberOfDOFs

    @property
    def number_of_elements(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfElements() As long (Read Only)
                |     Returns the number of elements.

        :return: int
        """

        return self.com_object.NumberOfElements

    @property
    def number_of_errors(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfErrors() As long (Read Only)
                |     Returns the number of errors.

        :return: int
        """

        return self.com_object.NumberOfErrors

    @property
    def number_of_increments(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfIncrements() As long (Read Only)
                |     Returns the number of increments.

        :return: int
        """

        return self.com_object.NumberOfIncrements

    @property
    def number_of_iterations(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfIterations() As long (Read Only)
                |     Returns the number of iterations.

        :return: int
        """

        return self.com_object.NumberOfIterations

    @property
    def number_of_nodes(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfNodes() As long (Read Only)
                |     Returns the number of nodes.

        :return: int
        """

        return self.com_object.NumberOfNodes

    @property
    def number_of_simulation_check_warnings(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfSimulationCheckWarnings() As long (Read Only)
                |     Returns the number of warnings from simulation check.

        :return: int
        """

        return self.com_object.NumberOfSimulationCheckWarnings

    @property
    def number_of_steps(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfSteps() As long (Read Only)
                |     Returns the number of steps.

        :return: int
        """

        return self.com_object.NumberOfSteps

    @property
    def number_of_warnings(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfWarnings() As long (Read Only)
                |     Returns the number of warnings.

        :return: int
        """

        return self.com_object.NumberOfWarnings

    @property
    def system_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SystemTime() As double (Read Only)
                |     Returns the system time.

        :return: float
        """

        return self.com_object.SystemTime

    @property
    def user_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UserTime() As double (Read Only)
                |     Returns the user time.

        :return: float
        """

        return self.com_object.UserTime

    @property
    def wallclock_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WallclockTime() As double (Read Only)
                |     Returns the wallclock time. 

        :return: float
        """

        return self.com_object.WallclockTime

    def __repr__(self):
        return f'SimJobDiagnosticSummary(name="{ self.name }")'
