"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_results.sim_field_plot import SimFieldPlot


class SimMultiView(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMultiView
                | 
                | Represents the Multi view manager.
                | Role:Multi view manager allows to apply view configuration to the viewer, and
                | to add plots in it.
                | Example:
                | 
                |  Given a SimResultsManager object, you can retrieve the Multi view manager as
                |  following.
                |  
                | 
                |  Dim MultiViewManager 'As SimMultiView
                |  Set MultiViewManager = ResultsManager.MultiViewManager
                |  
                | 
                | See also:
                |     SimResultsManager.MultiViewManager
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def configuration(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Configuration(SimConfiguration ieConfiguration) (Write
                | Only)
                |     Applies the given multi view configuration to current
                |     viewer.
                |     Applying a multi view configuration will divide the viewer area into
                |     sections (also known as viewpoints) each capable of holding maximum one plot at
                |     any time The available configurations are: VPFourSquare to apply four views
                |     (2x2). VPTriLeft to apply four views with three views on left and one main view
                |     on right. VPTriBottom to apply four views with three views on bottom and one
                |     main view on top. VPTwoRow to apply two views top and bottom. VPTwoColumn to
                |     apply two views left and right. VPSingle to apply default single
                |     view.
                | 
                |     Parameters:
                | 
                |         ieConfiguration
                |             The configuration to be applied. 
                | 
                |     Returns:
                |         Returns True if configuration applied successfully

        :return: int
        """

        return self.com_object.Configuration

    @configuration.setter
    def configuration(self, value: int):
        """
        :param int value:
        """

        self.com_object.Configuration = value

    @property
    def synchronize(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Synchronize(boolean ibSynchronize) (Write Only)
                |     Sets the synchronization mode for viewpoints. Setting synchronization mode
                |     TRUE will propagate actions performed such as Pan, Zoom, Rotate in one
                |     viewpoint to other viewpoints.
                | 
                |     Parameters:
                | 
                |         ibSynchronize
                |             If TRUE (default) all viewpoints will stay in
                |             sync.
                |             Else, only the viewpoint where actions are performed will get
                |             affected. 
                | 
                |     Returns:
                |         Returns True if synchronization set successfully

        :return: bool
        """

        return self.com_object.Synchronize

    @synchronize.setter
    def synchronize(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Synchronize = value

    def add_plot(self, i_plot: SimFieldPlot, in_position: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddPlot(SimFieldPlot iPlot,long inPosition)
                |     Adds a plot in multi view configuration at given position.
                |     Adds the given field plot into the desired viewpoint location of the
                |     current configuration. This field plot will replace any existing plot and will
                |     deactivate the existing plot if it was not available in any other
                |     viewpoint.
                | 
                |     Returns:
                |         Returns True if plot was added successfully 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :param SimFieldPlot i_plot:
        :param int in_position:
        :return: None
        """
        return self.com_object.AddPlot(i_plot.com_object, in_position)

    def __repr__(self):
        return f'SimMultiView(name="{ self.name }")'
