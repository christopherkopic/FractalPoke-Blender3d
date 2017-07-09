bl_info = {
 "name": "FractalPoke",
 "author": "Christopher Kopic",
 "version": (1, 0),
 "blender": (2, 7, 8),
 "location": "",
 "description": "Iterative Poking inspired by Simon Holmedal's Always Forever",
 "warning": "",
 "wiki_url": "",
 "tracker_url": "",
 "category": "Mesh"}


import bpy
from bpy.types import Operator
from bpy.props import FloatProperty, IntProperty, BoolProperty

class FractalPoke(bpy.types.Operator):
    """Fractal Poke"""
    bl_idname = "mesh.fractal_poke"
    bl_label = "Fractal Poke"
    bl_options = {'REGISTER', 'UNDO'}

    iterations = IntProperty(
        name = "Iterations",
        default = 3,
        min = 1,
        description = "Be careful as complexity will increase exponentially"
        )

    start_offset = FloatProperty(
        name = "Start Offset",
        default = 1.0,
        description = "Offset for first poke iteration"
        )

    offset_multiplier = FloatProperty(
        name = "Offset Multiplier",
        default = 0.5,
        description = "Increases or decreases offset for each iteration"
        )

    offset_flip = BoolProperty(
        name = "Flip Offset",
        default = False,
        description = "Flips offsetting inward or outward for each iteration"
        )

    grow_selection = BoolProperty(
        name = "Grow Selection",
        default = False,
        description = "Grows selection for each iteration"
        )

    shrink_selection = BoolProperty(
        name = "Shrink Selection",
        default = False,
        description = "Shrinks selection for each iteration"
        )

    def execute(self, context):
        my_offset = self.start_offset

        for i in range(self.iterations):
            bpy.ops.mesh.poke(offset = my_offset)
            my_offset *= self.offset_multiplier

            if self.offset_flip:
                my_offset *= -1

            if self.grow_selection:
                bpy.ops.mesh.select_more()

            if self.shrink_selection:
                bpy.ops.mesh.select_less()

        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return ob is not None and ob.mode == 'EDIT'
    
def register():
    bpy.utils.register_class(FractalPoke)

def unregister():
    bpy.utils.unregister_class(FractalPoke)

if __name__ == "__main__":
    register()
