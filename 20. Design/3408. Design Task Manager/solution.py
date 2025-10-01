import heapq

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}
        self.heap = []

        for userId, taskId, priority in tasks:
            self.tasks[taskId] = [priority, userId]
            heapq.heappush(self.heap, [-priority, -taskId])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = [priority, userId]
        heapq.heappush(self.heap, [-priority, -taskId])

    def edit(self, taskId: int, newPriority: int) -> None:
        self.tasks[taskId][0] = newPriority
        # add a new item to the queue
        heapq.heappush(self.heap, [-newPriority, -taskId])

    def rmv(self, taskId: int) -> None:
        self.tasks.pop(taskId)

    def execTop(self) -> int:
        while self.heap:
            priority, taskId = heapq.heappop(self.heap)
            priority, taskId = -priority, -taskId
            # execute task only if priority matches. Otherwise task was probably update or deleted. Skip it.
            if priority == self.tasks.get(taskId, [-1, -1])[0]:
                # dict.pop allows to remove item and read its value 
                return self.tasks.pop(taskId)[1]
        
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()