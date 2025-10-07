"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_object_frame_profile import OLPObjectFrameProfile


class OLPUploadService(Service):

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
                |                         OlpUploadService
                | 
                | Service to upload robot programs and convert them into 3DExperience
                | Tasks.
                | 
                | Example: (VB.NET)
                | 
                |  Dim Uploader As OlpUploadService = CATIA.Application.GetSessionService("OlpUploadService")
                |  Dim FilesToUpload as Object() = { C:\\ToUpload\\File1, C:\\ToUpload\\File2 }
                |  Dim Robot as Object = RobotSelection 'getting this selection is outside the scope of this example
                | 
                |  Uploader.SetResource(Robot)
                |  Uploader.SetFiles(FilesToUpload)
                |  Uploader.Translator = "" 'Setting this to an empty string will use the default translator, set in your preferences. If you want to use a specific other translator, set that name instead
                |  Uploader.Parse()
                |  Uploader.Upload()
                |  Uploader.PostProcess()
                |  Uploader.Finalize()
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def allow_device_param_update(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllowDeviceParamUpdate() As boolean
                |     Get/Set the option to allow device parameters to be
                |     updated.
                |     If false then any updates to the properties of the device that would
                |     normally be modified by the translator will be ignored. This includes Hard
                |     Limits, Soft Limits, Max Speeds and Accelerations, Singularity Tolerance, Heart
                |     Beat, Controller Type, Acceleration Mode, and Turn Mode.
                |     Default value is true. This must be called before Upload.

        :return: bool
        """

        return self.com_object.AllowDeviceParamUpdate

    @allow_device_param_update.setter
    def allow_device_param_update(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AllowDeviceParamUpdate = value

    @property
    def create_cartesian_homes(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CreateCartesianHomes() As boolean
                |     Get/Set the option to create home positions with the Cartesian position
                |     set.
                |     If true, all created and modified home positions will be created as
                |     Cartesian homes which preserves the Cartesian position instead of the joint
                |     values when replacing a resource.
                |     Default value is false. This must be called before Upload.

        :return: bool
        """

        return self.com_object.CreateCartesianHomes

    @create_cartesian_homes.setter
    def create_cartesian_homes(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CreateCartesianHomes = value

    @property
    def create_homes_for_joint_targets(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CreateHomesForJointTargets() As boolean
                |     Get/Set the option to create home positions for all joint
                |     targets.
                |     If true, home positions for all joint target motions will be created
                |     instead of just setting the joint values on the motion
                |     directly.
                |     Default value is false. This must be called before Upload.

        :return: bool
        """

        return self.com_object.CreateHomesForJointTargets

    @create_homes_for_joint_targets.setter
    def create_homes_for_joint_targets(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CreateHomesForJointTargets = value

    @property
    def delete_referenced_tags_and_homes(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DeleteReferencedTagsAndHomes() As boolean
                |     Get/Set the option to delete tags and homes in replaced
                |     tasks.
                |     If true, then tags and homes used only in the tasks that are replaced will
                |     be deleted. This only has an effect if ReplaceTasks is set to
                |     true.
                |     Default value is false. This must be called before Upload.

        :return: bool
        """

        return self.com_object.DeleteReferencedTagsAndHomes

    @delete_referenced_tags_and_homes.setter
    def delete_referenced_tags_and_homes(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DeleteReferencedTagsAndHomes = value

    @property
    def delete_unused_profiles(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DeleteUnusedProfiles() As boolean
                |     Get/Set the option to delete unused profiles.
                |     If true, then all profiles which are not used will be deleted at the end of
                |     the upload. Any profiles defined on the robot reference will be
                |     kept.
                |     Default value is false. This must be called before Upload.

        :return: bool
        """

        return self.com_object.DeleteUnusedProfiles

    @delete_unused_profiles.setter
    def delete_unused_profiles(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DeleteUnusedProfiles = value

    @property
    def files(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Files() As CATSafeArrayVariant
                |     Get/Set the files to be translated.
                |     Each entry is a string that is a full path to a file to be uploaded. Must
                |     be called before Parse.

        :return: tuple
        """

        return self.com_object.Files

    @files.setter
    def files(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.Files = value

    @property
    def replace_tasks(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReplaceTasks() As boolean
                |     Get/Set the option to replace the tasks.
                |     If true existing tasks with the same name as the uploaded tasks will be
                |     overwritten.
                |     Default value is false. This must be called before Upload.

        :return: bool
        """

        return self.com_object.ReplaceTasks

    @replace_tasks.setter
    def replace_tasks(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ReplaceTasks = value

    @property
    def resource(self) -> VPMOccurrence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Resource() As VPMOccurrence
                |     Get/Set the resource.
                |     This is the occurrence of the robot or tool that is being uploaded. If the
                |     robot system contains multiple devices, any of the resources can be used.

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
    def tasks_to_upload(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TasksToUpload() As CATSafeArrayVariant
                |     Get/Set the tasks to be upload.
                |     This can be used to limit the tasks uploaded in cases where you do not want
                |     to upload all tasks contained in the Parsed files. This is primarially used if
                |     a file contains multiple tasks.
                |     You can get the list of all tasks contained in the files and then set back
                |     a subset of those tasks as the ones to be created. If you do nothing, all tasks
                |     will be created.
                |     Each item in the list is the name of a task as a string.
                |     If called, this must be called after Parse but before Upload.

        :return: tuple
        """

        return self.com_object.TasksToUpload

    @tasks_to_upload.setter
    def tasks_to_upload(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.TasksToUpload = value

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
    def upload_object_frame_coords(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UploadObjectFrameCoords() As boolean
                |     Get/Set the option to use uploaded object frame
                |     coordinates.
                |     If false, the object frame coordinates imported from the robot program will
                |     be ignored. In most cases you should leave this option set to true. Only set to
                |     false if you have manually positioned the object frames in the correct
                |     locations. You can perform a legacy part coordinate upload by creating an
                |     object frame, attaching it to the part, and setting the offset to zero relative
                |     to the part.
                |     Default value is true. This must be called after Upload, but before
                |     PostProcess.

        :return: bool
        """

        return self.com_object.UploadObjectFrameCoords

    @upload_object_frame_coords.setter
    def upload_object_frame_coords(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UploadObjectFrameCoords = value

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
                |     DELOlpCurrentPosition. This must be called after Upload but before PostProcess.

        :return: DELOlpInitialPositionMode
        """

        return self.com_object.UseDesignPosition

    @use_design_position.setter
    def use_design_position(self, value: int):
        """
        :param int value:
        """

        self.com_object.UseDesignPosition = value

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

    def get_object_frames(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetObjectFrames() As CATSafeArrayVariant
                |     Obtain the object frames associated with the upload.
                | 
                |     Parameters:
                | 
                |         oFrameList
                |             The list of Object Frames associated with the upload. Each item in
                |             the list is an OlpObjectFrameProfile. This must be called after Upload, but
                |             before PostProcess.

        :return: tuple
        """
        return self.com_object.GetObjectFrames()

    def parse(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Parse()
                |     Parse the files to be uploaded in order to identify the tasks that will be
                |     created and other information about the controller setup. (application types,
                |     device types) This is called before Upload.

        :return: None
        """
        return self.com_object.Parse()

    def post_process(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PostProcess()
                |     Finalize creation of the tasks, tags, profiles and call MacroSetConfigs.
                |     This must be called only after Upload

        :return: None
        """
        return self.com_object.PostProcess()

    def set_part_for_object_frame(self, i_object_profile: OLPObjectFrameProfile, i_feature: AnyObject, i_part_occurrence: VPMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPartForObjectFrame(OlpObjectFrameProfile iObjectProfile,AnyObject
                | iFeature,VPMOccurrence iPartOccurrence)
                |     Set a part to attach an object frame to.
                | 
                |     Parameters:
                | 
                |         iObjectProfile
                |             The Object Frame to be attached. 
                |         iFeature
                |             The Referential Feature to which to attach the frame. This should
                |             be a tag, mount port, or other referential feature. This may be nothing if no
                |             referential feature is used. 
                |         iPartOccurrence
                |             The part to which to attach the frame. This must be called after
                |             Upload, but before PostProcess.

        :param OLPObjectFrameProfile i_object_profile:
        :param AnyObject i_feature:
        :param VPMOccurrence i_part_occurrence:
        :return: None
        """
        return self.com_object.SetPartForObjectFrame(i_object_profile.com_object, i_feature.com_object, i_part_occurrence.com_object)

    def upload(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Upload()
                |     Translate the files 

        :return: None
        """
        return self.com_object.Upload()

    def __repr__(self):
        return f'OLPUploadService(name="{ self.name }")'
