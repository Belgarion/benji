# noinspection PyUnresolvedReferences
from sparsebitfield import SparseBitfield


class BlockUidHistory:

    def __init__(self):
        self._history = {}

    def add(self, storage_id, block_uid):
        history = self._history
        if storage_id not in history:
            history[storage_id] = {}
        if block_uid.left not in history[storage_id]:
            history[storage_id][block_uid.left] = SparseBitfield()
        history[storage_id][block_uid.left].add(block_uid.right)

    def seen(self, storage_id, block_uid):
        history = self._history
        if storage_id not in history:
            return False
        if block_uid.left not in history[storage_id]:
            return False
        return block_uid.right in history[storage_id][block_uid.left]