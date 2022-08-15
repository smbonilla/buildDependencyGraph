class Node:

    def __init__(self, defineOneTask):
        '''
        Node class defines one node in the dependency graph by
        passing the class the three list items starting with
        'task:', 'files:', and 'deps:'
        
        Attributes:
        taskName (string): name of the task
        files (list of strings): names of files in the within task
        dependents (list of strings): name of tasks dependent
            on task
        '''

        # define task name 
        self.taskName = defineOneTask[0].split()
        self.taskName = self.taskName[1]

        # define files within task
        self.files = []
        allFiles = defineOneTask[1].split()
        for i in range(len(allFiles) - 1):
            self.files.append(allFiles[i + 1])

        # define dependent tasks
        self.dependents = []
        allDependents = defineOneTask[2].split()
        for k in range(len(allDependents) - 1):
            self.dependents.append(allDependents[k + 1])

class BuildGraph:
    def __init__(self, cities):
        self.adjList = {}
        
        for city in cities:
            if city[0] not in self.adjList.keys():
                self.adjList[city[0]] = []
            if city[1] not in self.adjList.keys():
                self.adjList[city[1]] = []
            
            self.adjList[city[0]].append(city[1])
            self.adjList[city[1]].append(city[0])