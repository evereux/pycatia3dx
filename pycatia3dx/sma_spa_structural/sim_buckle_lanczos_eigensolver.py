"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimBuckleLanczosEigensolver(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimBuckleLanczosEigensolver
                | 
                | Represents the Buckle Lanczos Eigensolver object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def maximum_eigenvalue(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumEigenvalue() As double
                |     Returns or sets the maximum Eigen value.

        :return: float
        """

        return self.com_object.MaximumEigenvalue

    @maximum_eigenvalue.setter
    def maximum_eigenvalue(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumEigenvalue = value

    @property
    def maximum_eigenvalue_set(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumEigenvalueSet() As boolean
                |     Returns or sets the flag that determines if the maximum Eigen value is
                |     specified.
                |     TRUE : the maximum Eigen value is specified.
                |     FALSE : the maximum Eigen value is not specified.

        :return: bool
        """

        return self.com_object.MaximumEigenvalueSet

    @maximum_eigenvalue_set.setter
    def maximum_eigenvalue_set(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MaximumEigenvalueSet = value

    @property
    def minimum_eigenvalue(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MinimumEigenvalue() As double
                |     Returns or sets the minimum Eigen value.

        :return: float
        """

        return self.com_object.MinimumEigenvalue

    @minimum_eigenvalue.setter
    def minimum_eigenvalue(self, value: float):
        """
        :param float value:
        """

        self.com_object.MinimumEigenvalue = value

    @property
    def minimum_eigenvalue_set(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MinimumEigenvalueSet() As boolean
                |     Returns or sets the flag that determines if the minimum Eigen value is
                |     specified.
                |     TRUE : the minimum Eigen value is specified.
                |     FALSE : the minimum Eigen value is not specified.

        :return: bool
        """

        return self.com_object.MinimumEigenvalueSet

    @minimum_eigenvalue_set.setter
    def minimum_eigenvalue_set(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MinimumEigenvalueSet = value

    @property
    def number_of_eigenvalues(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfEigenvalues() As long
                |     Returns or sets the number of Eigen values. 

        :return: int
        """

        return self.com_object.NumberOfEigenvalues

    @number_of_eigenvalues.setter
    def number_of_eigenvalues(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfEigenvalues = value

    def __repr__(self):
        return f'SimBuckleLanczosEigensolver(name="{ self.name }")'
