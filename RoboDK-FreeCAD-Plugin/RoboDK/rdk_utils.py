import os
import tempfile

import FreeCAD, FreeCADGui
import Part, PartGui
import Import

import robodk
import robolink
from robodk.robomath import *
#import robodk.robomath


def rdk_model_export():
    model_name = FreeCADGui.ActiveDocument.Document.Name
    file_name = tempfile.gettempdir() + '\\' + model_name + '.stp'

    sel = FreeCADGui.Selection.getSelection()

    Import.export(sel, file_name)

    RDK = robolink.Robolink()
    RDK.AddFile(file_name)

    os.remove(file_name)


def rdk_curve_export():
    RDK = robolink.Robolink()

    flip = -1  # 1
    res = 1  # mm

    pts = []
    faces = []
    edges = []

    sel = FreeCADGui.Selection.getSelectionEx()

    for obj in sel:

        elems = obj.SubObjects

        for elem in elems:
            if len(elem.Faces) == 0 and len(elem.Edges) == 1:
                edges.append(elem.Edges[0])
            if len(elem.Faces) == 1:
                faces.append(elem.Faces[0])

    for edge in edges:

        fc = []

        for face in faces:

            cm_el = face.ElementMap.keys() & edge.ElementMap.keys()

            for el in cm_el:
                if el.startswith('Edge'):
                    fc.append(face)

        cr = edge.discretize(Distance=res)

        for vect in cr:

            i = 0
            j = 0
            k = 1

            if len(fc) == 0 and len(faces) == 1:

                u, v = faces[0].Surface.parameter(vect)
                normal = faces[0].Surface.normal(u, v)

                i = flip * normal.x
                j = flip * normal.y
                k = flip * normal.z

            if len(fc) == 1:

                u, v = fc[0].Surface.parameter(vect)
                normal = fc[0].Surface.normal(u, v)

                i = flip * normal.x
                j = flip * normal.y
                k = flip * normal.z

            if len(fc) == 2:

                u, v = fc[0].Surface.parameter(vect)
                normal0 = fc[0].Surface.normal(u, v)

                u, v = fc[1].Surface.parameter(vect)
                normal = fc[1].Surface.normal(u, v)

                i = flip * (normal.x + normal0.x) / 2
                j = flip * (normal.y + normal0.y) / 2
                k = flip * (normal.z + normal0.z) / 2

            pt = [vect.x, vect.y, vect.z, i, j, k]
            pts.append(pt)

        RDK.AddCurve(pts)
        pts = []


def rdk_points_export():
    RDK = robolink.Robolink()

    sel = FreeCADGui.Selection.getSelectionEx()

    flip = -1  # 1

    faces = []
    points = []
    pts = []

    i = 0
    j = 0
    k = 0

    for obj in sel:

        elems = obj.SubObjects

        for elem in elems:
            if len(elem.Vertexes) == 1:
                points.append(elem.Vertexes[0])
            if len(elem.Faces) == 1:
                faces.append(elem.Faces[0])

    for pt in points:

        itm = (pt.Vertexes)[0].Point

        if len(faces) > 0:
            u, v = faces[0].Surface.parameter(itm)
            normal = faces[0].Surface.normal(u, v)

            i = flip * normal.x
            j = flip * normal.y
            k = flip * normal.z

        pn = [itm[0], itm[1], itm[2], i, j, k]
        pts.append(pn)

    RDK.AddPoints(pts)


def setIconsPath(path):
    global icons_path
    icons_path = path
    return (True)


def iconsPath():
    global icons_path
    return (icons_path)


def info(string):
    FreeCAD.Console.PrintMessage("%s\n" % string)


def warn(string):
    FreeCAD.Console.PrintWarning("%s\n" % string)


def error(string):
    FreeCAD.Console.PrintError("%s\n" % string)


def debug(string):
    FreeCAD.Console.PrintMessage("%s\n" % string)


def doNothing(string):
    return (None)
