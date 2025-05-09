import os
import rdk_utils
import FreeCAD, FreeCADGui

path_rdk_utils = os.path.dirname(rdk_utils.__file__)
path_rdk_icons = os.path.join(path_rdk_utils, 'Resources', 'icons')
path_rdk_settings_ui = os.path.join(path_rdk_utils, 'Resources', 'ui')
rdk_utils.setIconsPath(path_rdk_icons)
global main_rdk_icon
main_rdk_icon = os.path.join(path_rdk_icons, 'rdk.png')


class rdk_workbench(Workbench):

    MenuText = "RoboDK"

    global main_rdk_icon
    Icon = main_rdk_icon

    def Initialize(self):

        import rdk_ui
        import rdk_utils

        list = ["rdk_models_export", "rdk_curves_export", "rdk_points_export"]  # Contains the commands
        self.appendToolbar("My Scripts", list)

        FreeCADGui.addPreferencePage(os.path.dirname(rdk_utils.__file__) + '/Resources/ui/rdk_settings.ui', 'RoboDK Settings')


Gui.addWorkbench(rdk_workbench())
