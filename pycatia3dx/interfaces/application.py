"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx import CatScriptCommand
from pycatia3dx.interfaces.editors import Editors
from pycatia3dx.interfaces.printer import Printer
from pycatia3dx.interfaces.printers import Printers
from pycatia3dx.interfaces.service import Service
from pycatia3dx.interfaces.window import Window
from pycatia3dx.interfaces.windows import Windows
from pycatia3dx.os.file_system import FileSystem
from pycatia3dx.os.system_configuration import SystemConfiguration
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.system_service import SystemService
from pycatia3dx.types import ApplicationService, application_service_types

if TYPE_CHECKING:
    from pycatia3dx.interfaces.editor import Editor


class Application(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Application
                | 
                | Represents the current application and its frame window.
                | The application is the root object for all the other objects you can use and
                | access from scripts. It directly aggregates three collections:
                | 
                |     The editor collection represented by the Editors object. This collection
                |     contains all the editors currently opened by the
                |     application
                |     The window collection represented by the Windows object. This collection
                |     contains all the windows currently opened by the application, each window
                |     displaying objects managed by an editor
                |     The printer collection represented by the Printers object. This collection
                |     contains all the printers accessible from the application
                | 
                | Session level Service objects can be retrieved from the application object
                | thanks to the GetSessionService method.
                | 
                | The active editor and the active window are two key objects for the application
                | you can access using the ActiveEditor and ActiveWindow properties respectively.
                | The active window is the window the end user is currently working in, and the
                | active editor gives access to the objects visible in the active window and to
                | the set of operations that can be applied to those objects. In addition, the
                | active printer can be retrieved thanks to the ActivePrinter
                | property.
                | 
                | When you create or use macros for in-process access, the application is always
                | referred to as CATIA.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def active_editor(self) -> 'Editor':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property ActiveEditor() As Editor (Read Only)
                |     Returns the active editor.
                |     The active editor is the editor that controls the objects the end user is
                |     currently editing and that are displayed in the active
                |     window.
                | 
                |     Example:
                | 
                |          This example retrieves in ActiveEdt the active
                |          editor of the CATIA application.
                |          
                | 
                |          Dim ActiveEdt As Editor
                |          Set ActiveEdt = CATIA.ActiveEditor

        :return: Editor
        """
        from pycatia3dx.interfaces.editor import Editor

        return Editor(self.com_object.ActiveEditor)

    @property
    def active_printer(self) -> Printer:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property ActivePrinter() As Printer
                |     Returns or sets the active printer.
                |     The active printer is the printer on which documents are printed without
                |     any other printer selection.
                | 
                |     Example:
                | 
                |          This example retrieves in ActivePrt the active
                |          printer of the CATIA application.
                |          
                | 
                |          Dim ActivePrt As Printer
                |          Set ActivePrt = CATIA.ActivePrinter

        :return: Printer
        """

        return Printer(self.com_object.ActivePrinter)

    @active_printer.setter
    def active_printer(self, value: Printer):
        """
        :param Printer value:
        """

        self.com_object.ActivePrinter = value

    @property
    def active_window(self) -> Window:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property ActiveWindow() As Window (Read Only)
                |     Returns the active window.
                |     The active window is the window in which the end user is currently editing
                |     objects under control of the active editor.
                | 
                |     Example:
                | 
                |          This example retrieves in ActiveWin the active
                |          window of the CATIA application.
                |          
                | 
                |          Dim ActiveWin As Window
                |          Set ActiveWin = CATIA.ActiveWindow

        :return: Window
        """

        return Window(self.com_object.ActiveWindow)

    @property
    def cache_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property CacheSize() As long
                |     Returns or sets the default local cache size used by the
                |     application.
                | 
                |     Example:
                | 
                |          This example sets the cache size for by the CATIA
                |          application to those defined in LocalCacheSize.
                |          
                | 
                |          LocalCacheSize= 10
                |          CATIA.CacheSize = LocalCacheSize

        :return: int
        """

        return self.com_object.CacheSize

    @cache_size.setter
    def cache_size(self, value: int):
        """
        :param int value:
        """

        self.com_object.CacheSize = value

    @property
    def caption(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Caption() As CATBSTR
                |     Returns or sets the application's window title.
                |     This title is displayed in the application's window title
                |     bar.
                | 
                |     Example:
                | 
                |          This example retrieves in Title the CATIA
                |          application's window title.
                |          
                | 
                |          Title = CATIA.Caption
                |          
                | 
                | 
                |          
                | 
                | 
                |          The returned value is like this:
                |          
                | 
                |         CNext

        :return: str
        """

        return self.com_object.Caption

    @caption.setter
    def caption(self, value: str):
        """
        :param str value:
        """

        self.com_object.Caption = value

    @property
    def display_file_alerts(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property DisplayFileAlerts() As boolean
                |     Returns or sets the application ability to display file
                |     alerts.
                |     True if the application enables file alert display.
                |     True is the default. A file alert is, for example, the dialog box that
                |     prompts you that the file you want to save is in read only mode, or that the
                |     file you want to close needs to be saved. It could be handy to disable these
                |     file alerts for Automation since they may freeze your macro execution, waiting
                |     for an end user input in the displayed dialog box.
                | 
                |     Example:
                | 
                |          This example disables file alerts for the CATIA
                |          application.
                |          
                | 
                |          CATIA.DisplayFileAlerts = False

        :return: bool
        """

        return self.com_object.DisplayFileAlerts

    @display_file_alerts.setter
    def display_file_alerts(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DisplayFileAlerts = value

    @property
    def editors(self) -> Editors:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Editors() As Editors (Read Only)
                |     Returns the collection of editors currently managed by the
                |     application.
                | 
                |     Example:
                | 
                |          This example retrieves in EdtCollection the collection
                |          of
                |          editors currently managed by the CATIA application.
                |          
                | 
                |          Dim EdtCollection As Editors
                |          Set EdtCollection = CATIA.Editors

        :return: Editors
        """

        return Editors(self.com_object.Editors)

    @property
    def file_system(self) -> FileSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property FileSystem() As FileSystem (Read Only)
                |     Returns the file system.
                |     The file system provides access to a computer's file
                |     system.
                | 
                |     Example:
                | 
                |          This example retrieves in AppliFileSys the file
                |          system of the CATIA application.
                |          
                | 
                |          Dim AppliFileSys As FileSystem
                |          Set AppliFileSys = CATIA.FileSystem

        :return: FileSystem
        """

        return FileSystem(self.com_object.FileSystem)

    @property
    def full_name(self) -> str:
        # noinspection GrazieInspection
        """
                .. note::
                    :class: toggle

                    3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                        | Property FullName() As CATBSTR (Read Only)
                        |     Returns the application's executable file full name, including its
                        |     path.
                        |     This name is the name of the executable file used to start the
                        |     application.
                        |
                        |     Example:
                        |
                        |          This example retrieves in ApplicationFullName the
                        |          CATIA application's executable file full name.
                        |
                        |
                        |          ApplicationFullName = CATIA.FullName
                        |
                        |
                        |
                        |
                        |
                        |
                        |          The returned value is like this:
                        |
                        |
                        |          \\lisa\\cxr1arel\\bsf\\alpha_a\\code\\bin\\CNEXT.exe

                :return: str
                """

        return self.com_object.FullName

    @property
    def hso_synchronized(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property HSOSynchronized() As boolean
                |     For selection performance purposes, returns or sets the HSO synchronization
                |     in comparison with the CSO.
                |     Role: Precises if, for all Selection object instances, the HSO (Highlighted
                |     Set of Objects) is synchronized in comparison with the CSO (Current Set of
                |     Objects).
                | 
                |     Valid values are:
                | 
                |         True: In this case, Selection methods work directly with CATIA's CSO,
                |         to reflect instantly the changes made in Automation Selection. This ensures
                |         correct selection results, but may impact performance in certain
                |         cases.
                |         This is the default value at the beginning of a CATIA
                |         session.
                |         False: In this case, Selection methods work with an internal SO buffer,
                |         which allows faster execution when performing a large number of CSO-independent
                |         Selection calls, or when performing a single Selection call working on a large
                |         number of objects (usually the Search method). This may also prevent the
                |         features from blinking between two user interactions.
                | 
                |     Note: even if this property is set to False, the HSO is synchronized in
                |     comparison with the CSO at the begining of the following
                |     methods:
                | 
                |         Selection.SelectElement
                |         Selection.SelectMultipleElements
                |         Selection.SelectElementOtherEditor
                |         Selection.IndicateOrSelectElement2D
                |         Selection.IndicateOrSelectElement3D
                |         Application.StartCommand
                | 
                |     CAUTION: If you use the False value of this property, you must make sure to
                |     reset it to True for CATIA's CSO to reflect properly the changes made in
                |     Automation Selection. For example, it should be reset to True before
                |     interactive parts of your script: MsgBox, InputBox calls, VBA/VSTA forms
                |     updates and so on.

        :return: bool
        """

        return self.com_object.HSOSynchronized

    @hso_synchronized.setter
    def hso_synchronized(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.HSOSynchronized = value

    @property
    def height(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Height() As float
                |     Returns or sets the height of the application's frame
                |     window.
                |     The height is expressed in pixels.
                | 
                |     Example:
                | 
                |          This example sets the height of the CATIA
                |          application's frame window to 300 pixels.
                |          
                | 
                |          CATIA.Height = 300

        :return: float
        """

        return self.com_object.Height

    @height.setter
    def height(self, value: float):
        """
        :param float value:
        """

        self.com_object.Height = value

    @property
    def interactive(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Interactive() As boolean
                |     Returns or sets the application sensitivity to end user
                |     interactions.
                |     True if the application is end user interaction sensitive.
                | 
                |     Example:
                | 
                |          This example makes the CATIA application sensitive
                |          to end user interactions.
                |          
                | 
                |          CATIA.Interactive = True

        :return: bool
        """

        return self.com_object.Interactive

    @interactive.setter
    def interactive(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Interactive = value

    @property
    def left(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Left() As float
                |     Returns or sets the distance from the application's frame window left side
                |     to the left side of the screen.
                |     This distance is expressed in pixels.
                | 
                |     Example:
                | 
                |          This example sets the distance from the CATIA
                |          application's frame window left side to the left side of the
                |          screen
                |          to 150 pixels.
                |          
                | 
                |          CATIA.Left = 150

        :return: float
        """

        return self.com_object.Left

    @left.setter
    def left(self, value: float):
        """
        :param float value:
        """

        self.com_object.Left = value

    @property
    def local_cache(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property LocalCache() As CATBSTR
                |     Returns or sets the default local cache path used by the
                |     application.
                | 
                |     Example:
                | 
                |          This example sets the cache path for by the CATIA
                |          application to those defined in LocalCachePath.
                |          
                | 
                |          LocalCachePath= "/tmp/cache"
                |          CATIA.LocalCache = LocalCachePath

        :return: str
        """

        return self.com_object.LocalCache

    @local_cache.setter
    def local_cache(self, value: str):
        """
        :param str value:
        """

        self.com_object.LocalCache = value

    @property
    def path(self) -> str:
        # noinspection GrazieInspection
        """
                .. note::
                    :class: toggle

                    3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                        | Property Path() As CATBSTR (Read Only)
                        |     Returns the path of the application's executable files.
                        |
                        |     Example:
                        |
                        |          This example retrieves in ApplicationPath the path where
                        |          the
                        |          CATIA application executable files are located.
                        |
                        |
                        |          ApplicationPath = CATIA.Path
                        |
                        |
                        |
                        |
                        |
                        |
                        |          The returned value is like this:
                        |
                        |
                        |          \\lisa\\cxr1arel\\bsf\\alpha_a\\code\\bin

                :return: str
                """

        return self.com_object.Path

    @property
    def printers(self) -> Printers:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Printers() As Printers (Read Only)
                |     Returns the collection of the printers currently managed by the
                |     application.
                | 
                |     Example:
                | 
                |          This example retrieves in PrintersCollection the collection of
                |          the
                |          printers currently managed by the CATIA application.
                |          
                | 
                |          Dim PrintersCollection As Windows
                |          Set PrintersCollection = CATIA.Printers

        :return: Printers
        """

        return Printers(self.com_object.Printers)

    @property
    def refresh_display(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property RefreshDisplay() As boolean
                |     Returns or sets whether the update of the display is enabled during the
                |     script replay.
                |     Role: To improve performance, this update can be temporarely disabled by
                |     setting this property to False in the script.
                |     True (value set by default) if the application's display is refreshed after
                |     each method call executed in late binding mode . This property does not affect
                |     early binding calls nor the get methods because they are never followed by a
                |     refresh of the display.
                | 
                |     Example:
                | 
                |          This example makes the update of the CATIA application's display
                |          disabled during the script replay.
                |          
                | 
                |          CATIA.RefreshDisplay = False

        :return: bool
        """

        return self.com_object.RefreshDisplay

    @refresh_display.setter
    def refresh_display(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.RefreshDisplay = value

    @property
    def script_command(self) -> CatScriptCommand:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property ScriptCommand() As CatScriptCommand
                |     Enables the scripter to make his script behave as a CATIA
                |     command.
                |     Note: General notice regarding exclusive and shared
                |     commands:
                |     One has to know that an exclusive command, such as the Pad command of the
                |     "Part Design" workbench, when being selected, cancels the instanciated commands
                |     (such as the Select command). Contrarily, a shared command, such as the Print
                |     command, when being selected, does not cancel the instanciated commands: the
                |     Print command becomes active and, when its dialog is finished, the command
                |     which was active before the selection of the Print command becomes active
                |     again.
                |     This property allows to:
                | 
                |         tell CATIA that the script execution is actually
                |         finished.
                |         For example, in VBA, the end of the CATMain procedure execution does
                |         not mean the end of the script. Some forms may still be displayed. At this
                |         state of execution, comparing to the regular CATIA command protocol, the
                |         interactive command embodied in the script is not ended. The script ends when
                |         the last user form is hidden.
                |         tell CATIA that the script execution begins, and to cancel the active
                |         command (e.g. the Select command)
                | 
                |     This information will be used by CATIA to wait for the effective end of the
                |     script execution before activating the Select interactive
                |     command.
                |     See CatScriptCommand for authorized values and unauthorized state
                |     transitions.
                |     Example:
                | 
                |         Visual Basic for Applications:
                |             RenameCommand module
                | 
                |             'This command renames a feature
                |              Option Explicit
                |              Public EnteredName As String
                |              Public SelectedFeature As AnyObject
                |              Public AnInteractiveMethodIsRunning As Boolean
                |              Sub CATMain()
                |                   AnInteractiveMethodIsRunning = False
                |                   Dim AverageDialogWindowRight, AverageDialogWindowBottom As
                |                   Double
                |                   AverageDialogWindowRight = 38#          'distance from the right side of
                |                                                           'the CATIA frame and
                |                                                           the right
                |                                                           'side of the dialog window
                |                   AverageDialogWindowBottom = 81#         'distance from the bottom side of
                |                                                           'the CATIA frame and
                |                                                           the bottom
                |                                                           'side of the dialog window
                |                   CATIA.HSOSynchronized = False
                |                   CATIA.ScriptCommand = CatScriptCommandStart    'we activate, at the beginning of the script,
                |                                              'a fake exclusive command. The
                |                                              Select
                |                                              'interactive command is not active
                |                                              anymore.
                |                                              'The status bar is
                |                                              empty
                |                   Load RenameOperation
                |                   RenameOperation.Left = 0.75 * (CATIA.Left + CATIA.Width _
                |                     - AverageDialogWindowRight - RenameOperation.Width -
                |                     100)
                |                   RenameOperation.Top = 0.72 * (CATIA.Top + CATIA.Height _
                |                     - AverageDialogWindowBottom -
                |                     RenameOperation.Height)
                |                   RenameOperation.Show
                |                   CATIA.StatusBar = "Enter the new feature name or select the Feature selection editor control"
                |                   RenameOperation.NameValue.SetFocus
                |                   CATIA.HSOSynchronized = True
                |              End Sub                         'the end of the
                |              procedure
                | 
                |             RenameOperation form
                | 
                |              +----------------------------------+
                |              !                   +------------+ !
                |              ! Name:             !            ! !
                |              !                   +------------+ !
                |              !                   +------------+ !
                |              ! Feature selection:!No selection! !
                |              !                   +------------+ !
                |              !                         +------+ !
                |              !                         !  OK  ! !
                |              !                         +------+ !
                |              +----------------------------------+
                |              Option Explicit
                |              ' Method corresponding to the selection of the editor at the right
                |              of the
                |              ' "Feature selection" label
                |              Private Sub FeatureValue_MouseUp(ByVal Button As Integer,
                |              _
                |                                               ByVal Shift As Integer, ByVal X
                |                                               As Single, _
                |                                               ByVal Y As
                |                                               Single)
                |                   If (AnInteractiveMethodIsRunning) Then Exit
                |                   Sub
                |                   Dim Filter(0)
                |                   Dim Selection    'Warning: we do not put "As Selection"
                |                   because,
                |                                    'otherwise, the Selection methods passing
                |                                    a
                |                                    'CATSafeArrayVariant as parameter would
                |                                    trigger
                |                                    'a compilation error
                |                   Dim Status As String
                |                   Set Selection = CATIA.ActiveEditor.Selection
                |                   CATIA.HSOSynchronized = False
                |                   'We read the Name editor control
                |                   EnteredName = NameValue.Text
                |                   'We propose to the user that he select a
                |                   feature:
                |                   RenameOperation.NameValue.Enabled = False
                |                   RenameOperation.FeatureValue.Enabled = False
                |                   RenameOperation.OKCommandButton.Enabled = False 'we disable all
                |                                                                   'the currently
                |                                                                  'enabled
                |                                                                  'dialog
                |                                                                  'controls
                |                   AnInteractiveMethodIsRunning = True
                |                   Filter(0) = "AnyObject"
                |                   Status = Selection.SelectElement(Filter,"Select a feature",False)
                |                   AnInteractiveMethodIsRunning = False
                |                   RenameOperation.OKCommandButton.Enabled = True  'we enable the
                |                                                                   'disabled dialog
                |                                                                  'controls
                |                   If (Status="Cancel") Then
                |                       CATIA.HSOSynchronized = True
                |                       CATIA.ScriptCommand = CatScriptCommandStop  
                |                       Unload RenameOperation
                |                       Exit Sub
                |                   End If
                |                   Set SelectedFeature = Selection.Item(1).Value
                |                   SelectedFeature.Name = EnteredName
                |                   CATIA.StatusBar = "Click OK"
                |                   CATIA.HSOSynchronized = True
                |              End Sub
                |              ' Method corresponding to the selection of the OK command
                |              button
                |              Private Sub OKCommandButton_Click()
                |                   If (AnInteractiveMethodIsRunning) Then Exit
                |                   Sub
                |                   'We hide the RenameOperation dialog window
                |                   RenameOperation.Hide
                |                   CATIA.HSOSynchronized = True
                |                   CATIA.ScriptCommand = CatScriptCommandStop       'the created fake exclusive command 
                |                                              'instanciated goes out of its
                |                                              sleeping
                |                                              'state. 
                |                                              'The Select interactive command
                |                                              becomes
                |                                              'active again
                |                   Unload RenameOperation
                |              End Sub                         'the end both, of the method, and
                |              of the 
                |                                              'script execution
                |                                              itself
                | 
                |         VBScript case:
                | 
                |          Sub CATMain()
                |            Dim Filter(0)
                |            CATIA.ScriptCommand = CatScriptCommandStart                    'we activate, at the beginning of the script,
                |                                                     'a fake exclusive command.
                |                                                     The Select
                |                                                     'interactive command is not
                |                                                     active
                |                                                     anymore.
                |                                                     'The status bar is
                |                                                     empty
                |            . . .
                |            
                |            Set Selection = CATIA.ActiveDocument.Selection
                |            Filter(0) = "AnyObject"
                |            Status = Selection.SelectElement(Filter,"Select the feature",False)
                |            If (Status="Cancel") then
                |                CATIA.ScriptCommand = CatScriptCommandStop
                |                Exit Sub
                |            End If
                |             . . .
                |            
                |            CATIA.ScriptCommand = CatScriptCommandStop                  'the created fake command is desactivated. 
                |                                                     'The Select interactive
                |                                                     command
                |                                                     becomes
                |                                                     'active
                |                                                     again
                |          End Sub                                    'the end of the
                |          script
                | 
                |     Different uses of this property might cause the CATIA frame to freeze,
                |     until the Escape key is pressed.

        :return: CatScriptCommand
        """

        return self.com_object.ScriptCommand

    @script_command.setter
    def script_command(self, value: CatScriptCommand):
        """
        :param CatScriptCommand value:
        """

        self.com_object.ScriptCommand = value

    @property
    def status_bar(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property StatusBar() As CATBSTR
                |     Returns or sets the text displayed in the application's window status
                |     bar.
                |     Note: This property must be coupled with the use of the ScriptCommand
                |     property.
                |     Note: Setting this property will fail (being followed by a script error) if
                |     one of the following error occurs (CATIA.ScriptCommand current value
                |     is...):
                | 
                |         ... CatScriptCommandDefault => CATIA.StatusBar cannot be
                |         set.
                |         ... CatScriptCommandStop => CATIA.StatusBar cannot be
                |         set.
                | 
                |     Example:
                |         This example is written in Visual Basic for Applications. It Asks the
                |         end user to select an OK command button of a form.
                | 
                |          Sub CATMain()
                |          CATIA.ScriptCommand = CatScriptCommandStart
                |          Load MyForm
                |          MyForm.Show
                |          CATIA.StatusBar = "Select the OK command button"
                |           . . .
                |          End Sub                                      
                |          Private Sub OKCommandButton_Click()
                |           . . .   
                |          MyForm.Hide
                |          CATIA.ScriptCommand = CatScriptCommandStop    
                |          Unload MyForm       
                |          End Sub

        :return: str
        """

        return self.com_object.StatusBar

    @status_bar.setter
    def status_bar(self, value: str):
        """
        :param str value:
        """

        self.com_object.StatusBar = value

    @property
    def system_configuration(self) -> SystemConfiguration:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property SystemConfiguration() As SystemConfiguration (Read
                | Only)
                |     Returns the system configuration object.
                |     The system configuration object provides access to system or configuration
                |     dependent resources.
                | 
                |     Returns:
                |         The system configuration object.

        :return: SystemConfiguration
        """

        return SystemConfiguration(self.com_object.SystemConfiguration)

    @property
    def system_service(self) -> SystemService:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property SystemService() As SystemService (Read Only)
                |     Returns system services.
                | 
                |     Example:
                | 
                |          This example retrieves in AppliSysSer the CATIA
                |          application's system services.
                |          
                | 
                |          Dim AppliSysSer As SystemService
                |          Set AppliSysSer = CATIA.SystemService

        :return: SystemService
        """

        return SystemService(self.com_object.SystemService)

    @property
    def top(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Top() As float
                |     Returns or sets the distance from the application'si frame window top to
                |     the top of the screen.
                |     This distance is expressed in pixels.
                | 
                |     Example:
                | 
                |          This example sets the distance from the CATIA 
                |          application's frame window top to the top of the screen to 50
                |          pixels.
                |          
                | 
                |          CATIA.Top = 50

        :return: float
        """

        return self.com_object.Top

    @top.setter
    def top(self, value: float):
        """
        :param float value:
        """

        self.com_object.Top = value

    @property
    def undo_redo_lock(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property UndoRedoLock() As boolean
                |     Returns or sets the application status about Undo/Redo.
                |     True if the Undo/Redo mechanism is locked.
                |     False is the default. Since Undo/Redo mechanism uses lots of memory, it can
                |     be useful to disable it during consuming operations. Then Undo and Redo stacks
                |     are flushed and no model modification is kept until the Undo/Redo mechanism is
                |     unlocked. It is mandatory to unlock it before the end of the
                |     macro.
                | 
                |     Example:
                | 
                |          This example disables Undo/Redo mechanism until it is
                |          unlocked.
                |          
                | 
                |          CATIA.UndoRedoLock = True

        :return: bool
        """

        return self.com_object.UndoRedoLock

    @undo_redo_lock.setter
    def undo_redo_lock(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UndoRedoLock = value

    @property
    def user_interface_language(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property UserInterfaceLanguage() As CATBSTR (Read Only)
                |     Returns the user interface language.
                |     This is the language in which CATIA displays message catalog strings. The
                |     possible values are:
                | 
                |         English
                |         French
                |         German
                |         Italian
                |         Japanese
                |         Simplified_Chinese
                |         Korean
                | 
                |     With a .catvba script, or with a .catvbs script encoded in UTF-8, this
                |     property may be used to set:
                | 
                |         the .catvba dialog windows strings
                |         the Application.StatusBar property
                |         the iMessage parameter of the Selection.SelectElement
                |         method
                | 
                |     to a NLS value.
                | 
                |     Example:
                | 
                |          This example supposes the script is a .catvbs script encoded in UTF8.
                |          It asks the end user to select a
                |          
                |         Pad . 
                | 
                |          Dim PadSelectionFilter(0),PadSelectionStatusBar(0)
                |          Set PadSelectionFilter = "Pad"
                |          if (CATIA.UserInterfaceLanguage="French") then
                |              PadSelectionStatusBar = "Sélectionnez un Pad"
                |          else
                |              PadSelectionStatusBar = "Select a Pad"
                |          end if
                |          Set Selection = CATIA.ActiveEditor.Selection
                |          Status = Selection.SelectElement(PadSelectionFilter, PadSelectionStatusBar, False)

        :return: str
        """

        return self.com_object.UserInterfaceLanguage

    @property
    def visible(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Visible() As boolean
                |     Returns or sets the application's window visibility.
                |     True if the application's window is visible to the end
                |     user.
                | 
                |     Example:
                | 
                |          This example makes the CATIA application's window
                |          visible.
                |          
                | 
                |          CATIA.Visibility = True

        :return: bool
        """

        return self.com_object.Visible

    @visible.setter
    def visible(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Visible = value

    @property
    def width(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Width() As float
                |     Returns or sets the width of the application's frame
                |     window.
                |     The width is expressed in pixels.
                | 
                |     Example:
                | 
                |          This example sets the width of the CATIA
                |          application's frame window to 350 pixels.
                |          
                | 
                |          CATIA.Width = 350

        :return: float
        """

        return self.com_object.Width

    @width.setter
    def width(self, value: float):
        """
        :param float value:
        """

        self.com_object.Width = value

    @property
    def windows(self) -> Windows:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Windows() As Windows (Read Only)
                |     Returns the collection of windows currently managed by the
                |     application.
                | 
                |     Example:
                | 
                |          This example retrieves in WinCollection the collection
                |          of
                |          windows currently managed by the CATIA application.
                |          
                | 
                |          Dim WinCollection As Windows
                |          Set WinCollection = CATIA.Windows

        :return: Windows
        """

        return Windows(self.com_object.Windows)

    def disable_new_undo_redo_transaction(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub DisableNewUndoRedoTransaction()
                |     Prevents new Undo/Redo transaction creation.
                |     If too many Undo/Redo transactions are created during macro execution, it
                |     may affect performance. So it is valuable to prevent Undo/Redo transaction
                |     creation during macro execution when lots of data are created, deleted or
                |     modified.
                |     Note: preventing Undo/Redo transaction creation must not be done when a
                |     selection is required in the macro
                |     Do not forget to call EnableNewUndoRedoTransaction at the end of the macro
                |     or before selection to restore the common behavior.
                | 
                |     Example:
                |         This example prevents new transactions to be created, which may
                |         increase performance.
                | 
                |          CATIA.DisableNewUndoRedoTransaction()

        :return: None
        """
        return self.com_object.DisableNewUndoRedoTransaction()

    def enable_new_undo_redo_transaction(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub EnableNewUndoRedoTransaction()
                |     Allows new Undo/Redo transaction creation.
                | 
                |     Example:
                |         This example restores the common behavior after
                |         DisableNewUndoRedoTransaction has been called.
                | 
                |          CATIA.EnableNewUndoRedoTransaction()

        :return: None
        """
        return self.com_object.EnableNewUndoRedoTransaction()

    def file_selection_box(self, i_title: str, i_extension: str, i_mode: int) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func FileSelectionBox(CATBSTR iTitle,CATBSTR iExtension,CatFileSelectionMode
                | iMode) As CATBSTR
                |     Displays a modal dialog box.
                |     Role: This dialog box can be used to select or enter the name of a file to
                |     open or save.
                | 
                |     Parameters:
                | 
                |         iTitle
                |             The title of the dialog box. 
                |         iExtension
                |             A file extension filter. 
                |         iMode
                |             The mode in which to run the dialog box (either
                |             CatFileSelectionModeOpen or CatFileSelectionModeSave).
                |             
                | 
                |     Returns:
                |         A string containing the full path of the selected file, or a
                |         zero-length string if the user selects Cancel. 
                |     Example:
                | 
                |          This example asks the user to select a text file and prints the path
                |          of the selected
                |          file.
                |          
                | 
                |          filepath = CATIA.FileSelectionBox("Select a text file", "*.txt", CatFileSelectionModeOpen)
                |          CATIA.SystemServices.Print "The selected file is " &
                |          filepath

        :param str i_title:
        :param str i_extension:
        :param int i_mode:
        :return: str
        """
        return self.com_object.FileSelectionBox(i_title, i_extension, i_mode)

    def folder_selection_box(self, i_title: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func FolderSelectionBox(CATBSTR iTitle) As CATBSTR
                |     Displays a modal dialog box.
                |     Role: This dialog box can be used to select or enter the name of a
                |     folder.
                | 
                |     Parameters:
                | 
                |         iTitle
                |             The title of the dialog box. 
                | 
                |     Returns:
                |         A string containing the full path of the selected folder, or a
                |         zero-length string if the user selects Cancel. 
                |     Example:
                | 
                |          This example asks the user to select a folder and prints the path of
                |          the selected
                |          folder.
                |          
                | 
                |          folderpath = CATIA.FolderSelectionBox("Select a folder")
                |          CATIA.SystemServices.Print "The selected folder is " &
                |          folderpath

        :param str i_title:
        :return: str
        """
        return self.com_object.FolderSelectionBox(i_title)

    def get_session_service(self, i_service: str) -> ApplicationService:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetSessionService(CATBSTR iService) As Service
                |     Returns the specified service.
                |     Role:This method returns a Service
                | 
                |     Parameters:
                | 
                |         iService
                |             The id of the service to be retrieved. 
                | 
                |     Returns:
                |         The requested service 
                |     Example:
                | 
                |          This example retrieves in Service1 the IDService
                |          application's service.
                |          
                | 
                |          Dim Service1 As Service
                |          Set Service1 = CATIA.GetSessionService("IDService")

        :param str i_service:
        :return: AnyService
        """

        if i_service not in [service for service in application_service_types]:
            raise KeyError(f'{i_service} not a recognized service.')

        return application_service_types[i_service]['type'](self.com_object.GetSessionService(i_service))

    def get_workbench_id(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetWorkbenchId() As CATBSTR
                |     Returns the identifier of the current workbench.
                | 
                |     Parameters:
                | 
                |         oWorkbenchId
                |             The identifier of the current workbench.

        :return: str
        """
        return self.com_object.GetWorkbenchId()

    def help(self, i_help_id: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Help(CATBSTR iHelpID)
                |     Displays application's online help.
                | 
                |     Parameters:
                | 
                |         iHelpID
                |             Identifier of the help message to display 
                | 
                |     Example:
                | 
                |          This example displays the string referred to by the
                |          HelpKey
                |          message key in the message catalog concatenation. 
                |          
                | 
                |          CATIA.Help("HelpKey")

        :param str i_help_id:
        :return: None
        """
        return self.com_object.Help(i_help_id)

    def quit(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Quit()
                |     Exits the application and closes all open windows.
                | 
                |     Example:
                | 
                |          This example exits the CATIA application
                |          and closes all its open windows.
                |          
                | 
                |          CATIA.Quit()

        :return: None
        """
        return self.com_object.Quit()

    def start_command(self, i_command_id: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub StartCommand(CATBSTR iCommandId)
                |     Starts a command.
                |     Role: This method Starts a command and executes it until its first
                |     interaction. Please notice that interactions such as selections you could add
                |     after in your macro will not work. StartCommand is useful to execute one-shot
                |     (not interactive) commands. It is not safe for interactive
                |     commands.
                | 
                |     Parameters:
                | 
                |         iCommandId
                |             The identifier of the command to be started. This identifier can be
                |             the name of the command or its alias. Use the name of the command in the
                |             corresponding language installed on your machine.

        :param str i_command_id:
        :return: None
        """
        return self.com_object.StartCommand(i_command_id)

    def start_workbench(self, i_workbench_id: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub StartWorkbench(CATBSTR iWorkbenchId)
                |     Starts a workbench.
                | 
                |     Parameters:
                | 
                |         iWorkbenchId
                |             The identifier of the workbench to be started.

        :param str i_workbench_id:
        :return: None
        """
        return self.com_object.StartWorkbench(i_workbench_id)

    def __repr__(self):
        return f'Application(name="{self.name}")'
