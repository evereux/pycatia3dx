"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.sma_spa_structural.sim_buckle_lanczos_eigensolver import SimBuckleLanczosEigensolver
from pycatia3dx.sma_spa_structural.sim_buckle_subspace_eigensolver import SimBuckleSubspaceEigensolver


class SimBuckleStep(SimStep):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SMAMpaFoundationIDLItf.SimStep
                |                         SimBuckleStep
                | 
                | Represents the Buckle Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimBuckleStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyBuckleStep As SimBuckleStep
                |      Set MyBuckleStep = MySteps.Add("SimBuckleStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimBuckleStep named "Buckle
                |     Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyBuckleStep As SimBuckleStep
                |      Set MyBuckleStep = MySteps.Item("Buckle Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a SimBuckleStep as
                |     following:
                | 
                |      ...
                |      myBuckleStep = mySteps.Add("SimBuckleStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a SimBuckleStep named
                |     "Buckle Step.1" as following:
                | 
                |      ...
                |      myBuckleStep = mySteps.Item("Buckle Step.1")
                |      
                | 
                | See also:
                |     SimSteps
    
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
    def lanczos_solver(self) -> SimBuckleLanczosEigensolver:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LanczosSolver() As SimBuckleLanczosEigensolver (Read
                | Only)
                |     Returns the Lanczos solver.

        :return: SimBuckleLanczosEigensolver
        """

        return SimBuckleLanczosEigensolver(self.com_object.LanczosSolver)

    @property
    def solver_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SolverType() As SimBuckleStepSolverType
                |     Returns or sets the solver type.

        :return: int
        """

        return self.com_object.SolverType

    @solver_type.setter
    def solver_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SolverType = value

    @property
    def subspace_solver(self) -> SimBuckleSubspaceEigensolver:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SubspaceSolver() As SimBuckleSubspaceEigensolver (Read
                | Only)
                |     Returns the Subspace solver. 

        :return: SimBuckleSubspaceEigensolver
        """

        return SimBuckleSubspaceEigensolver(self.com_object.SubspaceSolver)

    def __repr__(self):
        return f'SimBuckleStep(name="{ self.name }")'
