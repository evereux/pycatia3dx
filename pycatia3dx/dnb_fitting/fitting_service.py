"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_fitting.fit_track import FitTrack
from pycatia3dx.types.general import CATVariant


class FittingService(Service):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         FittingService
                | 
                | Represents the FittingService.
                | 
                | Role: The FittingService is the object that provides a set of operations to
                | manage Fit Tracks. This object can be used to add or remove Fit Tracks in a
                | session along with being able to get the a specific Track using index and
                | number of Tracks in the session.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_context: AnyObject, i_type: str) -> FitTrack:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBaseDispatch iContext,CATBSTR iType) As FitTrack
                |     Returns a newly created Fitting Track in the given
                |     context.
                |     Role: Creates a new Fitting Track of the given type in the given context
                |     and returns the new track.
                | 
                |     Parameters:
                | 
                |         iContext
                |             The context in which the Fitting Track is being
                |             created.
                |             Legal values: 
                |         Nothing
                |             Context not required. Only in MSR context. 
                |         Occurrence
                |             Organizational Resource Occurrence under which the Track is created
                |             for a Track under Resource. 
                |         iType
                |             The string of the type of the Track to be created.
                |             Legal values: 
                |         DNBFitTrack
                |             Required for creating a Fitting Track. 
                |         DNBFctPrcsTrackExcitation
                |             Required for creating a Functional Process Track. 
                | 
                |     Returns:
                |         The created Fitting Track. 
                |     Example:
                | 
                |             This example returns in myTrack the Fitting Track created in MSR
                |             context.
                |           
                | 
                |           Dim oFittingSrv As FittingService
                |           Set oFittingSrv = DELMIA.ActiveEditor.GetService("FittingService")
                | 
                |           Dim theContext As CATBaseDispatch
                |           Set theContext = Nothing 
                | 
                |           Dim trackType As CATBSTR
                |           trackType = "DNBFitTrack"
                | 
                |           Dim myTrack As FitTrack
                |           Set myTrack = oFittingSrv.Add(theContext, trackType)

        :param AnyObject i_context:
        :param str i_type:
        :return: FitTrack
        """
        return FitTrack(self.com_object.Add(i_context.com_object, i_type))

    def count(self, i_context: AnyObject) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Count(CATBaseDispatch iContext) As long
                |     Returns the number of Tracks in the current context.
                | 
                |     Parameters:
                | 
                |         iContext
                |             The context from which the number of Fitting Tracks is
                |             retrieved.
                |             Legal values: 
                |         Nothing
                |             Context not required. Only in MSR context. 
                |         Occurrence
                |             Organizational Resource Occurrence. 
                | 
                |     Returns:
                |         The number of Fitting Track in the iContext. 
                |     Example:
                | 
                |            
                | 
                |         Dim theContext As CATBaseDispatch
                |         Set theContext = Nothing 
                | 
                |         Dim nbTracks As Integer
                |         nbTracks = myFittingSrv.Count(theContext)

        :param AnyObject i_context:
        :return: int
        """
        return self.com_object.Count(i_context.com_object)

    def item(self, i_context: AnyObject, i_index: CATVariant) -> FitTrack:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATBaseDispatch iContext,CATVariant iIndex) As
                | FitTrack
                |     Returns a Fitting Track by index in the given context.
                | 
                |     Parameters:
                | 
                |         iContext
                |             The context from which the Fitting Track is being
                |             retrieved.
                |             Legal values: 
                |         Nothing
                |             Context not required. Only in MSR context. 
                |         Occurrence
                |             Organizational Resource Occurrence under from which the Track is
                |             retrieved. 
                |         iIndex
                |             The index of the Track to retrieve from the list of Tracks. The
                |             index of the first Track is 1, and the index of the last Track is Count.
                |             
                | 
                |     Returns:
                |         The returned Fitting Track at iIndex. 
                |     Example:
                | 
                |                 This example retrieves in oTrack the first
                |                 Track
                |                 from the lsit of Tracks present under
                |                 excitations.
                |                 
                | 
                |         Dim theContext As CATBaseDispatch
                |         Set theContext = Nothing 
                | 
                |                 Dim oTrack As FitTrack
                |                 Set oTrack = oFittingSrv.Item theContext, 1

        :param AnyObject i_context:
        :param CATVariant i_index:
        :return: FitTrack
        """
        return FitTrack(self.com_object.Item(i_context.com_object, i_index))

    def remove(self, i_context: AnyObject, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATBaseDispatch iContext,CATVariant iIndex)
                |     Removes a Track object from the current Context.
                | 
                |     Parameters:
                | 
                |         iContext
                |             The context from which the Fitting Track is being
                |             deleted.
                |             Legal values: 
                |         Nothing
                |             Context not required. Only in MSR context. 
                |         Occurrence
                |             Organizational Resource Occurrence from which the Track is removed.
                |             
                |         iIndex
                |             The index of the Track to remove from the list of Tracks. The index
                |             of the first Track is 1, and the index of the last Track is Count.
                |             
                | 
                |     Example:
                | 
                |                 The following example removes the first Track in MSR
                |                 context.
                |                 
                | 
                |         Dim theContext As CATBaseDispatch
                |         Set theContext = Nothing 
                | 
                |                 myFittingSrv.Remove theContext, 1

        :param AnyObject i_context:
        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_context.com_object, i_index)

    def __repr__(self):
        return f'FittingService(name="{ self.name }")'
