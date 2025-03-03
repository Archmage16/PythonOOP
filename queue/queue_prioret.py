class Queue_Prio:
    def __init__(self, capacity = 100):
        self.__capacity = capacity
        self.__data = [" "] * capacity
        self.__count = 0
    
    @property
    def count(self) : return self.__count
    @property
    def capacity(self) -> int : return self.__capacity
    
    def set_capacity(self, new_capa):
        if new_capa > self.capacity:
            size = (new_capa - self.capacity)
            self.__data = self.__data + [' '] * size
        elif new_capa > self.count:
            self.__data = self.__data[:new_capa]
        else:
            print("Error. You cut real datas")
            self.__data = self.__data[:new_capa]
            self.count = new_capa
        self.__capacity = new_capa
    
    @property
    def isEmpty(self) -> bool:
        return self.count == 0
    @property
    def isFull(self) -> bool:
        return self.count == self.capacity
    
    def insert_with_priority(self, value, priority):
        if self.__count >= self.__capacity:
            print("Queue is full")
            self.set_capacity(self.__capacity * 2 + 1)
        self.__data[self.__count] = (value, priority)
        self.__count += 1
        return self.count
    
    def filter_by_priorety(self):
        for i in range(self.count):
            for j in range(self.count):
                if self.__data[i][1] > self.__data[j][1]:
                    self.__data[i], self.__data[j] = self.__data[j], self.__data[i]
                            
        
    
    def pull_highest_priority(self):
        self.filter_by_priorety()
        if self.isEmpty:
            print("Queue is empty!!!")
        self.__count -= 1
        result = self.__data[0]
        self.__data = self.__data[1:] + [' ']
        return result
    
    def peek(self):
        return self.__data[0]
    
    def Show(self):
        print(f"[{self.capacity}]/{self.count} : {self.__data}")
        
        
        
q1 = Queue_Prio(capacity = 10)

q1.insert_with_priority("task1", 5)
q1.insert_with_priority("task2", 1)
q1.insert_with_priority("task3", 3)
q1.insert_with_priority("task4", 2)
q1.insert_with_priority("task5", 5)
q1.Show()
print("Filtered by priority")

q1.filter_by_priorety()
q1.Show()
for i in range(5):
    print(q1.pull_highest_priority())