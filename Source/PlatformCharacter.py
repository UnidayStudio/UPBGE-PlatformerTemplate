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

class PlatformCharacter(bge.types.KX_PythonComponent):
	""" PlatformCharacter Component:
		Simple Character Movement component.
	"""

	args = OrderedDict([
		("Walk speed", 0.1),
		("Walk Keys", {"A and D Keys", "Left and Right Arrows", "Both"}),
		("Jump Key", {"W Key", "Up Arrow", "Space Key", "Both"})
	])

	def start(self, args):
		self.active = True  # Use this to enable or disable the system, if you need

		self.character = bge.constraints.getCharacter(self.object)

		self.walkSpeed = args["Walk speed"]

		self.keyLeft = [bge.events.AKEY]
		self.keyRight = [bge.events.DKEY]
		self.keyJump = [bge.events.WKEY]

		if args["Walk Keys"] == "Left and Right Arrows":
			self.keyLeft = [bge.events.LEFTARROWKEY]
			self.keyRight = [bge.events.RIGHTARROWKEY]
		elif args["Walk Keys"] == "Both":
			self.keyLeft += [bge.events.LEFTARROWKEY]
			self.keyRight += [bge.events.RIGHTARROWKEY]

		if args["Jump Key"] == "Up Arrow":
			self.keyJump = [bge.events.UPARROWKEY]
		elif args["Jump Key"] == "Space Key":
			self.keyJump = [bge.events.SPACEKEY]
		elif args["Jump Key"] == "Both":
			self.keyJump += [bge.events.UPARROWKEY, bge.events.SPACEKEY]

	def activeKeys(self, keyList):
		keyboard = bge.logic.keyboard.inputs

		for key in keyList:
			if keyboard[key].active:
				return True
		return False

	def activatedKeys(self, keyList):
		keyboard = bge.logic.keyboard.inputs

		for key in keyList:
			if keyboard[key].activated:
				return True
		return False

	def characterMovement(self):
		if self.activatedKeys(self.keyJump):
			self.character.jump()

		movement = 0
		if self.activeKeys(self.keyLeft):
			movement = -1
		elif self.activeKeys(self.keyRight):
			movement = 1

		movVec = mathutils.Vector([0, movement, 0]) * self.walkSpeed

		self.character.walkDirection = self.object.worldOrientation * movVec


	def update(self):
		if self.active:
			self.characterMovement()

