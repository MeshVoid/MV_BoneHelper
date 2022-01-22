"""
Copyright (C) 2021 Chingiz Jumagulov

Created by Chingiz Jumagulov

Contacts:
    
Website: meshvoid.com
Artstation: arstation.com/meshvoid
E-mail: meshvoid@gmail.com

"""

bl_info = {
    "name": "MeshVoid BoneHelper ",
    "author": "MeshVoid - meshvoid.com, @ Chingiz Jumagulov",
    "description": "MeshVoid BoneHelper Addon",
    "blender": (2, 92, 0),
    "version": (0, 1),
    "location": "View3D > Toolbar > MVBHP",
    "category": "Rigging",
}

import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class

'''UI PANELS'''

class MVBH_Panel(bpy.types.Panel):
    #Creates a Panel in the Object properties window
    #This addons main UI
    
    bl_idname = "MVBH_PT"
    bl_label = "MeshVoid BoneHelper"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MVBHP"
    
    def draw(self, context):
        
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text="Bone Helper", icon='BONE_DATA')
        
        row = layout.row()
        row.operator("mvbh.def_tgt", text ="DEF->TGT") # TODO - add custom operators to the buttons
        row = layout.row()
        #row.operator("mvbh.def_tgt", text ="TGT->CTL")
        row = layout.row()
        #row.operator("mvbh.def_tgt", text ="CTL->MCH")



'''FUNCTIONS AND VARIABLES'''


def get_edit_bone_list(self, context):
    # Get list of selected pose bones
    selected = bpy.context.selected_editable_bones
    bone_list = [bone.name for bone in selected]
    return bone_list



        
'''OPERATOR Classes'''
class MVBH_Operator_DEF_TGT(bpy.types.Operator):
    #TODO: Make this class turn DEF bones into TGT bones
    
    bl_idname = "mvbh.def_tgt"
    bl_label = "MVBH_DEF_TGT_Operator"
    bl_description = "Adds TGT bones to selected bones. Select Bones in Edit Mode"

    def execute(self, context):
        context = bpy.context
        obj = context.object
        
        namelist = [("DEF", "TGT")]
        for name, newname in namelist:
            # get the pose bone with name
            pb = obj.pose.bones.get(name)
            # continue if no bone of that name
            if pb is None:
                continue
            # rename
            pb.name = newname
            print('RENAMED' 'TO TGT')
        return{"FINISHED"}




classes = [
    MVBH_Panel,
    MVBH_Operator_DEF_TGT
    
]


def register():
    for cl in classes:
        register_class(cl)


def unregister():
    for cl in classes:
        unregister_class(cl)
    
if __name__ == "__main__":
    register()