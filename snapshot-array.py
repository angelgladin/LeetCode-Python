# https://leetcode.com/problems/snapshot-array/

class SnapshotArray:

    def __init__(self, length: int):
        self.n = length
        self.levels = []
        self.levels.append(dict())
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.levels[-1][index] = val

    def snap(self) -> int:
        aux = self.levels[self.snap_id].copy()
        self.levels.append(aux)
        self.snap_id += 1
        return self.snap_id -1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.levels[snap_id]:
            return self.levels[snap_id][index]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
