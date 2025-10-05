"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimBuckleSubspaceEigensolver(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimBuckleSubspaceEigensolver
                | 
                | Represents the Buckle Subspace Eigensolver object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def maximum_iterations(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumIterations() As long
                |     Returns or sets the maximum number of iterations.

        :return: int
        """

        return self.com_object.MaximumIterations

    @maximum_iterations.setter
    def maximum_iterations(self, value: int):
        """
        :param int value:
        """

        self.com_object.MaximumIterations = value

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
        return f'SimBuckleSubspaceEigensolver(name="{ self.name }")'
