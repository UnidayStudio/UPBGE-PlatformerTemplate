###############################################################################
#               Platformer Game | Template v 1.0 | UPBGE 0.2.4+               #
###############################################################################
#                      Created by: Guilherme Teres Nunes                      #
#                       Access: youtube.com/UnidayStudio                      #
#                               github.com/UnidayStudio                       #
###############################################################################
import bge
import mathutils
from collections import OrderedDict

class PathAlignment(bge.types.KX_PythonComponent):
	""" Path Alignment Component:
		This class makes the object automatically align to the nearest point
	of a mesh. This can be useful to create paths in 2.5D Platformers, climb
	systems and much more. There is an variable called 'active' that you can
	use to enable or disable this system."""

	args = OrderedDict([
		("Path Object Name", ""),
		#("Side Axis", {"X", "Y", "Z"}),
		#("Up Axis", {"X", "Y", "Z", "None"}),
		("Force Up Axis Aligment", False),
		("Align Smooth", 1.0)
	])

	def start(self, args):
		self.active = True # Use this to enable or disable the system, if you need
		self.path = self.object.scene.objects[args["Path Object Name"]]

		self.bvhPath = self.__getBVHtree()

		axis = {"X": 0, "Y": 1, "Z": 2, "None":-1}

		self.sideAxis = 0#axis[args["Side Axis"]]
		self.upAxis = 2#axis[args["Up Axis"]]
		self.forceUp = args["Force Up Axis Aligment"]

		self.alignSmooth = min(1, max(0.1, args["Align Smooth"]))

	def __getBVHtree(self):
		"""This function builds a BVH tree for the path object mesh and stores
		on the global dict. So if the user use this components on multiple
		objects, they will not create a new BVH tree every time."""

		gDictName = "BVHtree_"+self.path.name

		if not gDictName in bge.logic.globalDict:
			bge.logic.globalDict[gDictName] = self.path.meshes[0].constructBvh(self.path.worldTransform)

		return bge.logic.globalDict[gDictName]

	def update(self):
		if self.active:
			pathData = self.bvhPath.find_nearest(self.object.worldPosition)

			self.object.worldPosition = pathData[0]

			if self.upAxis != -1 and not self.forceUp:
				self.object.alignAxisToVect([0, 0, 1], self.upAxis, 1)

			self.object.alignAxisToVect(pathData[1], self.sideAxis, self.alignSmooth)

			if self.upAxis != -1 and self.forceUp:
				self.object.alignAxisToVect([0, 0, 1], self.upAxis, 1)
