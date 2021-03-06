"""
Levels described in the ICLR 2019 submission.
"""

import gym
from .verifier import *
from .levelgen import *


class Level_GoToObj(RoomGridLevel):
    """
    Go to an object, inside a single room with no doors, no distractors
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        objs = self.add_distractors(num_distractors=1)
        obj = objs[0]
        self.instrs = GoToInstr(ObjDesc(obj.type, obj.color))


class Level_GoToObjS4(Level_GoToObj):
    def __init__(self, seed=None):
        super().__init__(room_size=4, seed=seed)


class Level_GoToObjS6(Level_GoToObj):
    def __init__(self, seed=None):
        super().__init__(room_size=6, seed=seed)


class Level_GoToRedBallGrey(RoomGridLevel):
    """
    Go to the red ball, single room, with obstacles.
    The obstacles/distractors are all grey boxes, to eliminate
    perceptual complexity. No unblocking required.
    """

    def __init__(self, room_size=8, num_dists=7, seed=None):
        self.num_dists = num_dists
        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        obj, _ = self.add_object(0, 0, 'ball', 'red')

        for i in range(self.num_dists):
            self.add_object(0, 0, 'box', 'grey')

        # Make sure no unblocking is required
        self.check_objs_reachable()

        self.instrs = GoToInstr(ObjDesc(obj.type, obj.color))


class Level_GoToRedBall(RoomGridLevel):
    """
    Go to the red ball, single room, with distractors.
    This level has distractors but doesn't make use of language.
    """

    def __init__(self, room_size=8, num_dists=7, seed=None):
        self.num_dists = num_dists
        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        obj, _ = self.add_object(0, 0, 'ball', 'red')
        self.add_distractors(num_distractors=self.num_dists, all_unique=False)

        # Make sure no unblocking is required
        self.check_objs_reachable()

        self.instrs = GoToInstr(ObjDesc(obj.type, obj.color))


class Level_GoToRedBallNoDists(Level_GoToRedBall):
    def __init__(self, seed=None):
        super().__init__(room_size=8, num_dists=0, seed=seed)


class Level_GoToLocal(RoomGridLevel):
    """
    Go to an object, inside a single room with no doors, no distractors
    """

    def __init__(self, room_size=8, num_dists=8, seed=None):
        self.num_dists = num_dists
        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        objs = self.add_distractors(
            num_distractors=self.num_dists, all_unique=False)
        self.check_objs_reachable()
        obj = self._rand_elem(objs)
        self.instrs = GoToInstr(ObjDesc(obj.type, obj.color))


class Level_GoToLocalS5N2(Level_GoToLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=5, num_dists=2, seed=seed)


class Level_GoToLocalS6N2(Level_GoToLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=6, num_dists=2, seed=seed)


class Level_GoToLocalS6N3(Level_GoToLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=6, num_dists=3, seed=seed)


class Level_GoToLocalS6N4(Level_GoToLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=6, num_dists=4, seed=seed)


class Level_GoToLocalS7N4(Level_GoToLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=7, num_dists=4, seed=seed)


class Level_GoToLocalS7N5(Level_GoToLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=7, num_dists=5, seed=seed)


class Level_GoToLocalS8N2(Level_GoToLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=8, num_dists=2, seed=seed)


class Level_GoToLocalS8N3(Level_GoToLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=8, num_dists=3, seed=seed)


class Level_GoToLocalS8N4(Level_GoToLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=8, num_dists=4, seed=seed)


class Level_GoToLocalS8N5(Level_GoToLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=8, num_dists=5, seed=seed)


class Level_GoToLocalS8N6(Level_GoToLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=8, num_dists=6, seed=seed)


class Level_GoToLocalS8N7(Level_GoToLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=8, num_dists=7, seed=seed)


class Level_PutNextLocal(RoomGridLevel):
    """
    Put an object next to another object, inside a single room
    with no doors, no distractors
    """

    def __init__(self, room_size=8, num_objs=8, seed=None):
        self.num_objs = num_objs
        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        objs = self.add_distractors(
            num_distractors=self.num_objs, all_unique=True)
        self.check_objs_reachable()
        o1, o2 = self._rand_subset(objs, 2)

        self.instrs = PutNextInstr(
            ObjDesc(o1.type, o1.color),
            ObjDesc(o2.type, o2.color)
        )


class Level_PutNextLocalS5N3(Level_PutNextLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=5, num_objs=3, seed=seed)


class Level_PutNextLocalS6N4(Level_PutNextLocal):
    def __init__(self, seed=None):
        super().__init__(room_size=6, num_objs=4, seed=seed)


class Level_GoTo(RoomGridLevel):
    """
    Go to an object, the object may be in another room. Many distractors.
    """

    def __init__(
        self,
        room_size=8,
        num_rows=3,
        num_cols=3,
        num_dists=18,
        doors_open=False,
        seed=None
    ):
        self.num_dists = num_dists
        self.doors_open = doors_open
        super().__init__(
            num_rows=num_rows,
            num_cols=num_cols,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        self.connect_all()
        objs = self.add_distractors(
            num_distractors=self.num_dists, all_unique=False)
        self.check_objs_reachable()
        obj = self._rand_elem(objs)
        self.instrs = GoToInstr(ObjDesc(obj.type, obj.color))

        # If requested, open all the doors
        if self.doors_open:
            self.open_all_doors()


class Level_GoToOpen(Level_GoTo):
    def __init__(self, seed=None):
        super().__init__(doors_open=True, seed=seed)


class Level_GoToObjMaze(Level_GoTo):
    """
    Go to an object, the object may be in another room. No distractors.
    """

    def __init__(self, seed=None):
        super().__init__(num_dists=1, doors_open=False, seed=seed)


class Level_GoToObjMazeOpen(Level_GoTo):
    def __init__(self, seed=None):
        super().__init__(num_dists=1, doors_open=True, seed=seed)


class Level_GoToObjMazeS4R2(Level_GoTo):
    def __init__(self, seed=None):
        super().__init__(num_dists=1, room_size=4, num_rows=2, num_cols=2, seed=seed)


class Level_GoToObjMazeS4(Level_GoTo):
    def __init__(self, seed=None):
        super().__init__(num_dists=1, room_size=4, seed=seed)


class Level_GoToObjMazeS5(Level_GoTo):
    def __init__(self, seed=None):
        super().__init__(num_dists=1, room_size=5, seed=seed)


class Level_GoToObjMazeS6(Level_GoTo):
    def __init__(self, seed=None):
        super().__init__(num_dists=1, room_size=6, seed=seed)


class Level_GoToObjMazeS7(Level_GoTo):
    def __init__(self, seed=None):
        super().__init__(num_dists=1, room_size=7, seed=seed)


class Level_GoToImpUnlock(RoomGridLevel):
    """
    Go to an object, which may be in a locked room.
    Competencies: Maze, GoTo, ImpUnlock
    No unblocking.
    """

    def gen_mission(self):
        # Add a locked door to a random room
        id = self._rand_int(0, self.num_rows)
        jd = self._rand_int(0, self.num_cols)
        door, pos = self.add_door(id, jd, locked=True)
        locked_room = self.get_room(id, jd)

        # Add the key to a different room
        while True:
            ik = self._rand_int(0, self.num_rows)
            jk = self._rand_int(0, self.num_cols)
            if ik is id and jk is jd:
                continue
            self.add_object(ik, jk, 'key', door.color)
            break

        self.connect_all()

        # Add distractors to all but the locked room.
        # We do this to speed up the reachability test,
        # which otherwise will reject all levels with
        # objects in the locked room.
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if i is not id or j is not jd:
                    self.add_distractors(
                        i,
                        j,
                        num_distractors=2,
                        all_unique=False
                    )

        # The agent must be placed after all the object to respect constraints
        while True:
            self.place_agent()
            start_room = self.room_from_pos(*self.start_pos)
            # Ensure that we are not placing the agent in the locked room
            if start_room is locked_room:
                continue
            break

        self.check_objs_reachable()

        # Add a single object to the locked room
        # The instruction requires going to an object matching that description
        obj, = self.add_distractors(
            id, jd, num_distractors=1, all_unique=False)
        self.instrs = GoToInstr(ObjDesc(obj.type, obj.color))


class Level_Pickup(RoomGridLevel):
    """
    Pick up an object, the object may be in another room.
    """

    def gen_mission(self):
        self.place_agent()
        self.connect_all()
        objs = self.add_distractors(num_distractors=18, all_unique=False)
        self.check_objs_reachable()
        obj = self._rand_elem(objs)
        self.instrs = PickupInstr(ObjDesc(obj.type, obj.color))


class Level_UnblockPickup(RoomGridLevel):
    """
    Pick up an object, the object may be in another room. The path may
    be blocked by one or more obstructors.
    """

    def gen_mission(self):
        self.place_agent()
        self.connect_all()
        objs = self.add_distractors(num_distractors=20, all_unique=False)

        # Ensure that at least one object is not reachable without unblocking
        # Note: the selected object will still be reachable most of the time
        if self.check_objs_reachable(raise_exc=False):
            raise RejectSampling('all objects reachable')

        obj = self._rand_elem(objs)
        self.instrs = PickupInstr(ObjDesc(obj.type, obj.color))


class Level_Open(RoomGridLevel):
    """
    Open a door, which may be in another room
    """

    def gen_mission(self):
        self.place_agent()
        self.connect_all()
        self.add_distractors(num_distractors=18, all_unique=False)
        self.check_objs_reachable()

        # Collect a list of all the doors in the environment
        doors = []
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                room = self.get_room(i, j)
                for door in room.doors:
                    if door:
                        doors.append(door)

        door = self._rand_elem(doors)
        self.instrs = OpenInstr(ObjDesc(door.type, door.color))


class Level_Unlock(RoomGridLevel):
    """
    Unlock a door.

    Competencies: Maze, Open, Unlock. No unblocking.
    """

    def gen_mission(self):
        # Add a locked door to a random room
        id = self._rand_int(0, self.num_rows)
        jd = self._rand_int(0, self.num_cols)
        door, pos = self.add_door(id, jd, locked=True)
        locked_room = self.get_room(id, jd)

        # Add the key to a different room
        while True:
            ik = self._rand_int(0, self.num_rows)
            jk = self._rand_int(0, self.num_cols)
            if ik is id and jk is jd:
                continue
            self.add_object(ik, jk, 'key', door.color)
            break

        # With 50% probability, ensure that the locked door is the only
        # door of that color
        if self._rand_bool():
            colors = list(filter(lambda c: c is not door.color, COLOR_NAMES))
            self.connect_all(door_colors=colors)
        else:
            self.connect_all()

        # Add distractors to all but the locked room.
        # We do this to speed up the reachability test,
        # which otherwise will reject all levels with
        # objects in the locked room.
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if i is not id or j is not jd:
                    self.add_distractors(
                        i,
                        j,
                        num_distractors=3,
                        all_unique=False
                    )

        # The agent must be placed after all the object to respect constraints
        while True:
            self.place_agent()
            start_room = self.room_from_pos(*self.start_pos)
            # Ensure that we are not placing the agent in the locked room
            if start_room is locked_room:
                continue
            break

        self.check_objs_reachable()

        self.instrs = OpenInstr(ObjDesc(door.type, door.color))


class Level_PutNext(RoomGridLevel):
    """
    Put an object next to another object. Either of these may be in another room.
    """

    def gen_mission(self):
        self.place_agent()
        self.connect_all()
        objs = self.add_distractors(num_distractors=18, all_unique=False)
        self.check_objs_reachable()
        o1, o2 = self._rand_subset(objs, 2)
        self.instrs = PutNextInstr(
            ObjDesc(o1.type, o1.color),
            ObjDesc(o2.type, o2.color)
        )


class Level_PickupLoc(LevelGen):
    """
    Pick up an object which may be described using its location. This is a
    single room environment.

    Competencies: PickUp, Loc. No unblocking.
    """

    def __init__(self, seed=None):
        # We add many distractors to increase the probability
        # of ambiguous locations within the same room
        super().__init__(
            seed=seed,
            action_kinds=['pickup'],
            instr_kinds=['action'],
            num_rows=1,
            num_cols=1,
            num_dists=12,
            locked_room_prob=0,
            locations=True,
            unblocking=False
        )


class Level_GoToSeq(LevelGen):
    """
    Sequencing of go-to-object commands.

    Competencies: Maze, GoTo, Seq
    No locked room.
    No locations.
    No unblocking.
    """

    def __init__(
        self,
        room_size=8,
        num_rows=3,
        num_cols=3,
        num_dists=18,
        seed=None
    ):
        super().__init__(
            room_size=room_size,
            num_rows=num_rows,
            num_cols=num_cols,
            num_dists=num_dists,
            seed=seed,
            action_kinds=['goto'],
            locked_room_prob=0,
            locations=False,
            unblocking=False
        )


class Level_GoToSeqS5R2(Level_GoToSeq):
    def __init__(self, seed=None):
        super().__init__(room_size=5, num_rows=2, num_cols=2, num_dists=4, seed=seed)


class Level_Synth(LevelGen):
    """
    Union of all instructions from PutNext, Open, Goto and PickUp. The agent
    may need to move objects around. The agent may have to unlock the door,
    but only if it is explicitly referred by the instruction.

    Competencies: Maze, Unblock, Unlock, GoTo, PickUp, PutNext, Open
    """

    def __init__(
        self,
        room_size=8,
        num_rows=3,
        num_cols=3,
        num_dists=18,
        seed=None
    ):
        # We add many distractors to increase the probability
        # of ambiguous locations within the same room
        super().__init__(
            room_size=room_size,
            num_rows=num_rows,
            num_cols=num_cols,
            num_dists=num_dists,
            seed=seed,
            instr_kinds=['action'],
            locations=False,
            unblocking=True,
            implicit_unlock=False
        )


class Level_SynthS5R2(Level_Synth):
    def __init__(self, seed=None):
        super().__init__(
            room_size=5,
            num_rows=2,
            num_cols=2,
            num_dists=7,
            seed=seed
        )


class Level_SynthLoc(LevelGen):
    """
    Like Synth, but a significant share of object descriptions involves
    location language like in PickUpLoc. No implicit unlocking.

    Competencies: Maze, Unblock, Unlock, GoTo, PickUp, PutNext, Open, Loc
    """

    def __init__(self, seed=None):
        # We add many distractors to increase the probability
        # of ambiguous locations within the same room
        super().__init__(
            seed=seed,
            instr_kinds=['action'],
            locations=True,
            unblocking=True,
            implicit_unlock=False
        )


class Level_SynthSeq(LevelGen):
    """
    Like SynthLoc, but now with multiple commands, combined just like in GoToSeq.
    No implicit unlocking.

    Competencies: Maze, Unblock, Unlock, GoTo, PickUp, PutNext, Open, Loc, Seq
    """

    def __init__(self, seed=None):
        # We add many distractors to increase the probability
        # of ambiguous locations within the same room
        super().__init__(
            seed=seed,
            locations=True,
            unblocking=True,
            implicit_unlock=False
        )


class Level_MiniBossLevel(LevelGen):
    def __init__(self, seed=None):
        super().__init__(
            seed=seed,
            num_cols=2,
            num_rows=2,
            room_size=5,
            num_dists=7,
            locked_room_prob=0.25
        )


class Level_BossLevel(LevelGen):
    def __init__(self, seed=None):
        super().__init__(
            seed=seed
        )


class Level_BossLevelNoUnlock(LevelGen):
    def __init__(self, seed=None):
        super().__init__(
            seed=seed,
            locked_room_prob=0,
            implicit_unlock=False
        )


class Level_CustomGoToObjSmall(RoomGridLevel):
    """
    Custom small GoToObj level with two objects, and a compound instruction
    to visit them in order. No distractors.
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        objs = self.add_distractors(num_distractors=2)
        assert len(objs) == 2

        self.instrs = BeforeInstr(
            GoToInstr(ObjDesc(objs[0].type, objs[0].color)),
            GoToInstr(ObjDesc(objs[1].type, objs[1].color)),
            strict=True
        )


class Level_CustomGoToObjAndOr(RoomGridLevel):
    """
    Custom small GoToObj level with two objects, and a compound instruction with
    connectors AND and OR. No distractors.
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        objs = self.add_distractors(num_distractors=2)
        assert len(objs) == 2

        i = self._rand_int(0, 2)
        obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))

        if i == 0:
            self.instrs = AndInstr(obj_instr_0, obj_instr_1, strict=True)
        elif i == 1:
            self.instrs = OrInstr(obj_instr_0, obj_instr_1, strict=True)

class Level_CustomGoToObjAnd(RoomGridLevel):
    """
    Custom small GoToObj level with two objects, and a compound instruction with
    connectors AND and OR. No distractors.
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        objs = self.add_distractors(num_distractors=2)
        assert len(objs) == 2

        obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))

        self.instrs = AndInstr(obj_instr_0, obj_instr_1)

class Level_CustomGoToObjOr(RoomGridLevel):
    """
    Custom small GoToObj level with two objects, and a compound instruction with
    connectors AND and OR. No distractors.
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        objs = self.add_distractors(num_distractors=2)
        assert len(objs) == 2

        obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))

        self.instrs = OrInstr(obj_instr_0, obj_instr_1)


class Level_CustomGoToObjMedium(RoomGridLevel):
    """
    Custom small GoToObj level with two objects, and a compound instruction.
    The tasks can be connected with "and", "or", "then"(after) or "before".

    No distractors.
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        objs = self.add_distractors(num_distractors=2)
        assert len(objs) == 2

        # pick randomly between Before, After
        i = self._rand_int(0, 2)
        obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))

        if i == 0:
            self.instrs = BeforeInstr(obj_instr_0, obj_instr_1, strict=True)
        elif i == 1:
            self.instrs = AfterInstr(obj_instr_0, obj_instr_1, strict=True)


class Level_CustomGoToObjDistr(RoomGridLevel):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        objs = self.add_distractors(num_distractors=3)
        o1, o2 = self._rand_subset(objs, 2)
        self.check_objs_reachable()

        # pick randomly between Before, After, And, Or
        i = self._rand_int(0, 2)
        obj_instr_0 = GoToInstr(ObjDesc(o1.type, o1.color))
        obj_instr_1 = GoToInstr(ObjDesc(o2.type, o2.color))

        if i == 0:
            self.instrs = BeforeInstr(obj_instr_0, obj_instr_1, strict=True)
        elif i == 1:
            self.instrs = AfterInstr(obj_instr_0, obj_instr_1, strict=True)


class Level_TransferBase(RoomGridLevel):
    """
    """

    def __init__(self, room_size=8, seed=None):
        # Since we have a transfer level, extend the default colors and
        # object types
        from gym_minigrid.minigrid import COLORS, COLOR_NAMES, COLOR_TO_IDX, IDX_TO_COLOR
        from copy import deepcopy

        self.NEW_COLORS = {
            'cyan': np.array([0, 128, 128])
            # 'magenta': np.array([128, 0, 128])
        }
        self.NEW_COLOR_NAMES = sorted(list(self.NEW_COLORS.keys()))
        self.OLD_COLOR_NAMES = list(
            set(COLOR_NAMES) - set(self.NEW_COLOR_NAMES))

        self.NEW_OBJECTS = ['triangle']
        self.OLD_OBJECTS = ['key', 'ball', 'box']

        if 'cyan' not in COLOR_NAMES:
            COLORS.update(self.NEW_COLORS)
            COLOR_NAMES.extend(self.NEW_COLOR_NAMES)
            COLOR_TO_IDX.update({'cyan': 6})
            IDX_TO_COLOR.update({6: 'cyan'})
        assert len(COLOR_NAMES) == 7

        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )


class Level_TransferGoToObjSmall0(Level_TransferBase):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add an object we have seen before
        objs = self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=True, new_object=False))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 2

        self.instrs = BeforeInstr(
            GoToInstr(ObjDesc(objs[0].type, objs[0].color)),
            GoToInstr(ObjDesc(objs[1].type, objs[1].color)),
            strict=True
        )


class Level_TransferGoToObjSmall1(Level_TransferBase):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add an object we have seen before
        objs = self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=True))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 2

        self.instrs = BeforeInstr(
            GoToInstr(ObjDesc(objs[0].type, objs[0].color)),
            GoToInstr(ObjDesc(objs[1].type, objs[1].color)),
            strict=True
        )


class Level_TransferGoToObjSmall2(Level_TransferBase):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add an object we have seen before
        objs = self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=True, new_object=True))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 2

        self.instrs = BeforeInstr(
            GoToInstr(ObjDesc(objs[0].type, objs[0].color)),
            GoToInstr(ObjDesc(objs[1].type, objs[1].color)),
            strict=True
        )


class Level_TransferGoToObjBeforeAfter0(Level_TransferBase):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add an object we have seen before
        objs = self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=True, new_object=False))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 2

        i = self._rand_int(0, 2)
        obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))

        if i == 0:
            self.instrs = BeforeInstr(obj_instr_0, obj_instr_1, strict=True)
        elif i == 1:
            self.instrs = AfterInstr(obj_instr_0, obj_instr_1, strict=True)


class Level_TransferGoToObjBeforeAfter1(Level_TransferBase):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add an object we have seen before
        objs = self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=True))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 2

        i = self._rand_int(0, 2)
        obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))

        if i == 0:
            self.instrs = BeforeInstr(obj_instr_0, obj_instr_1, strict=True)
        elif i == 1:
            self.instrs = AfterInstr(obj_instr_0, obj_instr_1, strict=True)


class Level_TransferGoToObjBeforeAfter2(Level_TransferBase):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add an object we have seen before
        objs = self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=True, new_object=True))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 2

        i = self._rand_int(0, 2)
        obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))

        if i == 0:
            self.instrs = BeforeInstr(obj_instr_0, obj_instr_1, strict=True)
        elif i == 1:
            self.instrs = AfterInstr(obj_instr_0, obj_instr_1, strict=True)


class Level_TransferGoToObjAnd0(Level_TransferBase):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add an object we have seen before
        objs = self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=True, new_object=False))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 2

        obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))

        self.instrs = AndInstr(obj_instr_0, obj_instr_1, strict=True)


class Level_TransferGoToObjAnd1(Level_TransferBase):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add an object we have seen before
        objs = self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=True))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 2

        obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))

        self.instrs = AndInstr(obj_instr_0, obj_instr_1, strict=True)


class Level_TransferGoToObjAnd2(Level_TransferBase):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add an object we have seen before
        objs = self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=True, new_object=True))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 2

        obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))

        self.instrs = AndInstr(obj_instr_0, obj_instr_1, strict=True)


class Level_CustomUnblockPickupSmall(RoomGridLevel):
    """
    Pick up an object, the object may be in another room. The path may
    be blocked by one or more obstructors.
    """
    def __init__(self, room_size=8, seed=None):
        super().__init__(
            num_rows=1,
            num_cols=2,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        self.connect_all()
        objs = self.add_distractors(num_distractors=2, all_unique=False)

        # Ensure that at least one object is not reachable without unblocking
        if self.check_objs_reachable(raise_exc=False):
            raise RejectSampling('all objects reachable')

        self.np_random.shuffle(objs)
        assert len(objs) == 2

        obj_instr_0 = PickupInstr(ObjDesc(objs[0].type, objs[0].color))
        obj_instr_1 = PickupInstr(ObjDesc(objs[1].type, objs[1].color))
        self.instrs = BeforeInstr(obj_instr_0, obj_instr_1, strict=True)



class Level_CustomGoToObjMultiple(RoomGridLevel):
    """
    Pick up an object, the object may be in another room. The path may
    be blocked by one or more obstructors.
    """
    def __init__(self, room_size=8, seed=None):
        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        objs = self.add_distractors(num_distractors=2, all_unique=False)
        self.np_random.shuffle(objs)
        i = self._rand_int(0, 9)
        assert len(objs) == 2
        if i == 0:
            # 1 1
            obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
            obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        elif i == 1:
            # 2 1
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=2)
            obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        elif i == 2:
            # 1 2
            obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=2)
        elif i == 3:
            # 2 2
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=2)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=2)
        elif i == 4:
            # 1 3
            obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=3)
        elif i == 5:
            # 3 1
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=3)
            obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        elif i == 6:
            # 2 3
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=2)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=3)
        elif i == 7:
            # 3 2
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=3)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=2)
        elif i == 8:
            # 3 3
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=3)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=3)

        self.instrs = BeforeInstr(obj_instr_0, obj_instr_1, strict=True)


class Level_CustomGoToObjThrees(RoomGridLevel):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            num_rows=1,
            num_cols=1,
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        objs = self.add_distractors(num_distractors=3)
        assert len(objs) == 3
        i = self._rand_int(0,3)

        go_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        go_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        go_2 = GoToInstr(ObjDesc(objs[2].type, objs[2].color))

        if i == 0:
            # then then
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='beforebefore')
        elif i == 1:
            # then after
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='beforeafter')
        elif i == 2:
            # after then
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='afterbefore')
        elif i == 3:
            # after after
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='afterafter')


class Level_TransferGoToObjMultiple0(Level_TransferBase):
    """
    Pick up an object, the object may be in another room. The path may
    be blocked by one or more obstructors.
    """
    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add an object we have seen before
        objs = self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=True, new_object=False))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 2

        i = self._rand_int(0, 9)
        if i == 0:
            # 1 1
            obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
            obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        elif i == 1:
            # 2 1
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=2)
            obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        elif i == 2:
            # 1 2
            obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=2)
        elif i == 3:
            # 2 2
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=2)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=2)
        elif i == 4:
            # 1 3
            obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=3)
        elif i == 5:
            # 3 1
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=3)
            obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        elif i == 6:
            # 2 3
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=2)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=3)
        elif i == 7:
            # 3 2
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=3)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=2)
        elif i == 8:
            # 3 3
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=3)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=3)

        self.instrs = BeforeInstr(obj_instr_0, obj_instr_1, strict=True)


class Level_TransferGoToObjMultiple1(Level_TransferBase):
    """
    Pick up an object, the object may be in another room. The path may
    be blocked by one or more obstructors.
    """
    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add an object we have seen before
        objs = self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=True))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 2

        i = self._rand_int(0, 9)
        if i == 0:
            # 1 1
            obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
            obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        elif i == 1:
            # 2 1
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=2)
            obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        elif i == 2:
            # 1 2
            obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=2)
        elif i == 3:
            # 2 2
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=2)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=2)
        elif i == 4:
            # 1 3
            obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=3)
        elif i == 5:
            # 3 1
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=3)
            obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        elif i == 6:
            # 2 3
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=2)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=3)
        elif i == 7:
            # 3 2
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=3)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=2)
        elif i == 8:
            # 3 3
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=3)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=3)

        self.instrs = BeforeInstr(obj_instr_0, obj_instr_1, strict=True)


class Level_TransferGoToObjMultiple2(Level_TransferBase):
    """
    Pick up an object, the object may be in another room. The path may
    be blocked by one or more obstructors.
    """
    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add an object we have seen before
        objs = self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=True, new_object=True))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 2

        i = self._rand_int(0, 9)
        if i == 0:
            # 1 1
            obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
            obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        elif i == 1:
            # 2 1
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=2)
            obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        elif i == 2:
            # 1 2
            obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=2)
        elif i == 3:
            # 2 2
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=2)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=2)
        elif i == 4:
            # 1 3
            obj_instr_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=3)
        elif i == 5:
            # 3 1
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=3)
            obj_instr_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        elif i == 6:
            # 2 3
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=2)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=3)
        elif i == 7:
            # 3 2
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=3)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=2)
        elif i == 8:
            # 3 3
            obj_instr_0 = RepeatGoToInstr(ObjDesc(objs[0].type, objs[0].color), repeat=3)
            obj_instr_1 = RepeatGoToInstr(ObjDesc(objs[1].type, objs[1].color), repeat=3)

        self.instrs = BeforeInstr(obj_instr_0, obj_instr_1, strict=True)


class Level_TransferGoToObjThrees0(Level_TransferBase):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add objects we have seen before
        objs = self.add_new_objects(
            num_new_objs=2, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=True, new_object=False))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 3

        i = self._rand_int(0,3)

        go_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        go_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        go_2 = GoToInstr(ObjDesc(objs[2].type, objs[2].color))

        if i == 0:
            # then then
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='beforebefore')
        elif i == 1:
            # then after
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='beforeafter')
        elif i == 2:
            # after then
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='afterbefore')
        elif i == 3:
            # after after
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='afterafter')


class Level_TransferGoToObjThrees1(Level_TransferBase):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add objects we have seen before
        objs = self.add_new_objects(
            num_new_objs=2, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=False, new_object=True))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 3

        i = self._rand_int(0,3)

        go_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        go_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        go_2 = GoToInstr(ObjDesc(objs[2].type, objs[2].color))

        if i == 0:
            # then then
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='beforebefore')
        elif i == 1:
            # then after
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='beforeafter')
        elif i == 2:
            # after then
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='afterbefore')
        elif i == 3:
            # after after
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='afterafter')

class Level_TransferGoToObjThrees2(Level_TransferBase):
    """
    """

    def __init__(self, room_size=8, seed=None):
        super().__init__(
            room_size=room_size,
            seed=seed
        )

    def gen_mission(self):
        self.place_agent()
        # Add objects we have seen before
        objs = self.add_new_objects(
            num_new_objs=2, new_color=False, new_object=False)
        # Add an object with a color we have not seen before
        objs.extend(self.add_new_objects(
            num_new_objs=1, new_color=True, new_object=True))
        # shuffle the list to ensure more randomness with new object
        self.np_random.shuffle(objs)
        assert len(objs) == 3

        i = self._rand_int(0,3)

        go_0 = GoToInstr(ObjDesc(objs[0].type, objs[0].color))
        go_1 = GoToInstr(ObjDesc(objs[1].type, objs[1].color))
        go_2 = GoToInstr(ObjDesc(objs[2].type, objs[2].color))

        if i == 0:
            # then then
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='beforebefore')
        elif i == 1:
            # then after
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='beforeafter')
        elif i == 2:
            # after then
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='afterbefore')
        elif i == 3:
            # after after
            self.instrs = ThreeOrderedInstr(go_0, go_1, go_2, strict=True, mode='afterafter')


# Register the levels in this file
register_levels(__name__, globals())
