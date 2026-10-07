"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.sma_mpa_results.sim_results_step import SimResultsStep
from pycatia3dx.types.general import CATVariant


class SimResultsSteps(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimResultsSteps
                | 
                | Represents the collection of results analysis cases and can be used to retrieve
                | each results case.
                | Example:
                | 
                |  Given a ResultsAnalysisCase object, you can create a Results Steps object as
                |  following.
                |  
                | 
                |  Dim oResultsSteps As SimResultsSteps
                |  Set oResultsSteps = oResultsAnalysisCase.ResultsSteps
                |  
                | 
                | See also:
                |     SimResultsManager
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SimResultsStep)
        self.com_object = com_object

    def item(self, index: CATVariant) -> SimResultsStep:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant index) As SimResultsStep
                |     Returns the ResultsStep.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of ResultsStep to access. The index starts from 1.
                |             
                | 
                |     Returns:
                |         Returns the ResultsStep. 

        :param CATVariant index:
        :return: SimResultsStep
        """
        return SimResultsStep(self.com_object.Item(index))

    def __getitem__(self, n: int) -> SimResultsStep:
        if (n + 1) > self.count:
            raise StopIteration

        return SimResultsStep(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[SimResultsStep]:
        for i in range(self.count):
            yield SimResultsStep(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'SimResultsSteps(name="{self.name}")'
