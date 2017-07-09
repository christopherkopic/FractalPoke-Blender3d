# FractalPoke-Blender3d

# What is it?
Fractal Poke is an add-on for Blender 3D (blender.org), which enables the user to create fractal-like structures on top of selected faces on a mesh.

It was inspired by the structures shown in Simon Holmedal’s ‚Always Forever‘:
http://www.simonholmedal.com/alwaysforever/

It was written by Christopher Kopic in July 2017.

# Installing the addon.
1.	Download the .zip file and unpack it.
2.	In Blender open the user preferences, navigate to the add-ons tab and click ‚Install Add-on from File‘
3.	Inside the unpacked folder, select the FractalPoke.py file and click ‚Install Add-on from File…‘
4.	Select the checkbox next to ‚Mesh: Fractal Poke‘ and click ‚Safe User Settings‘

# Using the operator.
The operator works with every mesh object, which has at least one face. To use it, tab into edit mode, select the faces, you want to modify, hit space, type ‚Fractal Poke‘ and hit enter. The selected faces should change immediately and you are presented with six parameters, you can tweak:

-	Iterations: This controls how many times the faces are subdivided. Be careful with this value as calcualtion times increase very rapidly!
-	Start Offset: This controls the distance the first iteration is moved inward or outward, basically controlling the overall size of the structure.
-	Offset Multiplier: As the name suggests, the offset gets multiplied by this value for each iteration, increasing or decreasing it over time.
-	Flip Offset: If enabled, the offset flips direction for each iteration.
-	Grow Selection: If enabled, new faces around the initial ones are selected with each iteration, which blends the structure into its surroundings.
-	Shrink Selection: With every iteration, the outmost faces get deselected, shrinking the affected area over time.

# Animating it.
Since you can’t keyframe the sliders of an operator, animating the fractals takes a bit of preparation, but it can still be done fairly easily using shape keys. For this example, let’s animate the start offset, which makes the fractal ‚grow‘ from a flat plane.

1.	Prepare your model just up to the point where you would normally use the operator. This also includes selecting all faces you want to ‚fractalize‘.
2.	Change to Object Mode, duplicate your model using Shift-D and put it down somewhere in your scene (doesn’t matter where).
3.	Select your first object, tab into Edit Mode and use the operator as you usually would. Only this time set the start offset to zero and exit to Object Mode.
4.	Select your duplicate and call the operator as well. All the values you previously set, should still be the same. Now set the start offset to the maximum value you want to use and exit to Object Mode.
5.	You should now have two models with the exact same vertex count and the same fractalized faces, with the only difference of one object still looking flat and normal and the other one having the signature fractal style.
6.	Select your flat looking object, navigate to the shape key menu and add a base shape key.
7.	Select both objects, making sure the flat one is the active one.
8.	In the shape key menu click the black arrow under the plus and minus button and select ‚Join as Shapes‘
9.	Your flat object should now have a new shape key and, if you set the value slider of said key to 1, should look exactly like your second object.
10.	You can now keyframe this slider as you wish and thus animate your fractals.

You can use this technique to animate any parameter that does not change vertex count i.e. start offset, offset multiplier and flip offset.
