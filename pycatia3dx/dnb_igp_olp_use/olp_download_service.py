"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence


class OLPDownloadService(Service):
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
                |                         OlpDownloadService
                | 
                | Service to download tasks and convert them into native robot
                | programs.
                | 
                | Example: (VB.NET)
                | 
                |  
                |  Dim DownloadService As OlpDownloadService = CATIA.Application.GetSessionService("OlpDownloadService")
                |  
                |  Dim CellRoot As VPMRootOccurrence = Nothing
                |  Dim ProdService As PLMProductService = CATIA.ActiveEditor.GetService("PLMProductService")
                |  CellRoot = ProdService.RootOccurrence
                |  Dim Robots As List(Of VPMOccurrence) = New List(Of VPMOccurrence)
                |  For i As Integer = 1 To parent.Occurrences.Count
                |      Dim occ As VPMOccurrence = CellRoot.Occurrences.Item(i)
                |      Try
                |          Dim resource As RscMotionController = occ
                |          If resource.GetMotionControllerType(resource) = DELRscMotionControllerType.DELRscMotionControllerType_Arm Then
                |              Robots.Add(occ)
                | 			  Continue For
                | 		  End If
                |      Catch ex As Exception
                |  
                |      End Try
                |  Next
                |  
                |  For Each Robot As VPMOccurrence In Robots
                |      Dim robottaskmanager As TaskManager = Robot
                |      DownloadService.Resource = Robot
                | 
                | 	  'Set default translator for robot found. This step is not required if using
                | default translator, as the default translator will be set during downloader if
                | no other translator is set.
                | 	  DownloadService.Translator = "" 
                |      DownloadService.Download(robottaskmanager.TaskList)
                |      DownloadService.SaveToFolder("E:\tmp\" & CellRoot.Name & "\" &
                |      Robot.Name)
                |  Next
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def download_call_tasks(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DownloadCallTasks() As boolean
                |     Get/Set the option to download called tasks during
                |     download.
                |     If true, then any tasks called by a downloaded task will be downloaded as
                |     part of that task. Default value is false. This must be called before Download.

        :return: bool
        """

        return self.com_object.DownloadCallTasks

    @download_call_tasks.setter
    def download_call_tasks(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DownloadCallTasks = value

    @property
    def resource(self) -> VPMOccurrence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Resource() As VPMOccurrence
                |     Get/Set the resource.
                |     This is the occurrence of the robot or tool that is being downloaded. If
                |     the robot system contains multiple devices, any of the resources can be used.
                |     this is required for download.

        :return: VPMOccurrence
        """

        return VPMOccurrence(self.com_object.Resource)

    @resource.setter
    def resource(self, value: VPMOccurrence):
        """
        :param VPMOccurrence value:
        """

        self.com_object.Resource = value

    @property
    def template_dir(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TemplateDir() As CATBSTR
                |     Get/Set the template directory.
                |     This is the directory where existing robot programs from this robot's
                |     controller are stored. If set, they are used to generate the new programs in
                |     the same formatting and using the system variables from the robot backup to
                |     adjust the download. If this is not set prior to Download, templates will not
                |     be used during download.

        :return: str
        """

        return self.com_object.TemplateDir

    @template_dir.setter
    def template_dir(self, value: str):
        """
        :param str value:
        """

        self.com_object.TemplateDir = value

    @property
    def translator(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Translator() As CATBSTR
                |     Get/Set the translator.
                |     This is the title of the translator (e.g. "DELMIA Fanuc Translator"). The
                |     database will be searched for a matching translator. If you do not specify a
                |     translator, the default one from the preferences will be used.

        :return: str
        """

        return self.com_object.Translator

    @translator.setter
    def translator(self, value: str):
        """
        :param str value:
        """

        self.com_object.Translator = value

    @property
    def translator_option(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TranslatorOption() As CATBSTR
                |     Get/Set the translator option.
                |     This is upload option. If not set, the default one from the preferences
                |     will be used.

        :return: str
        """

        return self.com_object.TranslatorOption

    @translator_option.setter
    def translator_option(self, value: str):
        """
        :param str value:
        """

        self.com_object.TranslatorOption = value

    @property
    def use_design_position(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UseDesignPosition() As DELOlpInitialPositionMode
                |     Get/Set the option to use design position during download.
                |     Can be set to either DELOlpDesignPosition or DELOlpCurrentPosition to
                |     control behavior of points attached to moving objects. Default value is
                |     DELOlpCurrentPosition. This must be called after Download but before saving.

        :return: DELOlpInitialPositionMode
        """

        return self.com_object.UseDesignPosition

    @use_design_position.setter
    def use_design_position(self, value: int):
        """
        :param int value:
        """

        self.com_object.UseDesignPosition = value

    def download(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub Download(CATSafeArrayVariant iTaskList)
                |     Translate the tasks into native robot programs.
                |     The Resource must be set before calling this method.
                |
                |     Parameters:
                |
                |         iTaskList
                |             List of DELMIAResourceTask objects.

        :return: tuple
        """
        return self.com_object.Download()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'download'
        # vba_code = """
        # Public Function download(olp_download_service)
        #     Dim iTaskList (2)
        #     olp_download_service.Download iTaskList
        #     download = iTaskList
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def export_messages_to_file(self, i_file: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ExportMessagesToFile(CATBSTR iFile)
                |     Create a file with all the translation messagse.
                | 
                |     Parameters:
                | 
                |         iFile
                |             The full path to the file to create. If the file extension is xls,
                |             xlsx or xlsm an Excel file will be created otherwise a text file will be
                |             created.

        :param str i_file:
        :return: None
        """
        return self.com_object.ExportMessagesToFile(i_file)

    def finalize(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Finalize()
                |     Clean up the translation service's state manager.
                |     This MUST be run after all translation service functions are complete.

        :return: None
        """
        return self.com_object.Finalize()

    def save_to_database(self, i_save_resource: VPMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SaveToDatabase(VPMOccurrence iSaveResource)
                |     Save the programs to a document attached to a resource in the database.
                |     Download must be called before calling this method.
                | 
                |     Parameters:
                | 
                |         iSaveResource
                |             The resource occurrence on which to save the documents. The
                |             documents will be saved on the resource's reference

        :param VPMOccurrence i_save_resource:
        :return: None
        """
        return self.com_object.SaveToDatabase(i_save_resource.com_object)

    def save_to_folder(self, i_save_dir: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SaveToFolder(CATBSTR iSaveDir)
                |     Save the programs to a folder on your computer. Download must be called
                |     before calling this method.
                | 
                |     Parameters:
                | 
                |         iSaveDir
                |             The full path to the directory to save the files. 

        :param str i_save_dir:
        :return: None
        """
        return self.com_object.SaveToFolder(i_save_dir)

    def __repr__(self):
        return f'OLPDownloadService(name="{self.name}")'
