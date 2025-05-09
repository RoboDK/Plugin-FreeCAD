import FreeCAD, FreeCADGui
import rdk_utils

RDK_MODEL_ICON = rdk_utils.iconsPath() + '/rdk_models.svg'
RDK_CURVES_ICON = rdk_utils.iconsPath() + '/rdk_curves.svg'
RDK_POINTS_ICON = rdk_utils.iconsPath() + '/rdk_points.svg'


class rdk_ui:

    def __init__(self, changevalue):
        self.changevalue = changevalue

    def Activated(self):

        if self.changevalue == "export_models":
            FreeCAD.Console.PrintMessage('export_model' + '\n')
            rdk_utils.rdk_model_export()
        if self.changevalue == "export_curves":
            FreeCAD.Console.PrintMessage('export_curves' + '\n')
            rdk_utils.rdk_curve_export()
        if self.changevalue == "export_points":
            FreeCAD.Console.PrintMessage('export_points' + '\n')
            rdk_utils.rdk_points_export()

    def GetResources(self):
        if self.changevalue == "export_models":
            TOOL_ICON = RDK_MODEL_ICON
            TOOLTIP_VAL = 'Models export'
        if self.changevalue == "export_curves":
            TOOL_ICON = RDK_CURVES_ICON
            TOOLTIP_VAL = 'Curves export'
        if self.changevalue == "export_points":
            TOOL_ICON = RDK_POINTS_ICON
            TOOLTIP_VAL = 'Points export'

        return {'Pixmap': TOOL_ICON, 'MenuText': 'Short text', 'ToolTip': TOOLTIP_VAL}


FreeCADGui.addCommand('rdk_models_export', rdk_ui("export_models"))
FreeCADGui.addCommand('rdk_curves_export', rdk_ui("export_curves"))
FreeCADGui.addCommand('rdk_points_export', rdk_ui("export_points"))
