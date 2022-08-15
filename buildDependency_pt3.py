# Part 3 of Practice for Palantir Online Interview found on:
# https://leetcode.com/discuss/interview-question/2372796/Palantir-Online-Interview
#
# Author: Sierra Bonilla
# Date: 12-03-2022

# built-in RegEx Module
import re

class Graph:

    def __init__(self, taskDefinitionsInput):
        '''
        Graph class defines a dependency graph object that can be used
        to traverse through the tree.
        
        Attributes:
        deps (dictionary): 
            name --> name of the task
            key  --> list of dependencies
        '''

        # define total number of tasks in taskDefinitionsInput
        numTasks = int(len(taskDefinitionsInput)/4)
        
        # intializing dictionary to store dependencies
        self.deps = {}

        # loop through all tasks
        for i in range(numTasks):
            
            # saving one task and its properties to defineOneTask variable
            defineOneTask = taskDefinitionsInput[i*4:(i*4)+3]

            # saving the task name to name variable
            name =  defineOneTask[0].split()

            # saving the dependents to depsList variable
            depsList = defineOneTask[2].split()

            # creating dictionary
            self.deps[name[1]] = depsList[1:]


def tasksToRun(taskDefinitionsInput, changedFiles):
    '''
    tasksToRun Function checks the files in the tasks in
    taskDefinitionsInput for changedFiles and output the tasks 
    that need to be rerun.

    Args:
    taskDefinitionsInput (list of strings): a list of task definitions
        with exactly 4 lines for each task. The first line must be 
        prefixed by 'task:', second line prefixed with 'files:', and
        third line prefixed with 'deps:'.
    changedFiles (list of strings): is a list of file paths that 
        have recently changed.

    Returns:
    tasksChanged (list of strings):
        a list of task names that should re-run.
    '''

    # check that the inputs are correct file type 
    if all(isinstance(item, str) for item in taskDefinitionsInput) and all(isinstance(item, str) for item in changedFiles): 

        # initialize tasksChanged, could use set also to save space and time checking if task already exists
        tasksChanged = []

        # initialize count current line number
        lineCount = 0

        # loop through the lines in taskDefinitionsInput and determine if 
        # files in changedFiles are a child
        for lines in taskDefinitionsInput:

            # split up the current line into individual elements
            currline = lines.split()

            # check that current line isn't empty and if the current line is the files line  
            if currline and currline[0] == 'files:':

                # loop through files 
                for i in range(len(currline) - 1):
                    
                    # check if the file has been changed 
                    # if currline[i + 1] in changedFiles:
                    if matchGlob(currline[i + 1], changedFiles):
                        
                        # return only name of the task
                        taskLine = taskDefinitionsInput[lineCount - 1].split()

                        # check if already added before, or use set? 
                        if taskLine[1] not in tasksChanged:
                            tasksChanged.append(taskLine[1])

            # increment line count
            lineCount += 1

        # sort the tasksChanged by the dependents according to the depencyGraph created
        graph = Graph(taskDefinitionsInput)
        sortedTasksChanged = sortTasks(tasksChanged, graph)

        return tasksChanged

    else:
        print('All inputs must be strings!')

def escapeSpecialChars(file):
    '''
    escapeSpecialChars Function takes a string as an input and
    escapes all special characters denoted by the regexp engine
    and replaces the * global pattern with '.*?' which signifies
    to the regexp function to look for any set of characters that 
    matches with the minimal amount possible. 

    Args:
    file (string): pathway to be corrected string

    Returns:
    fileProcessed (string): file pathway processed
    '''

    # escapes all special characters
    fileProcessed = re.escape(file)

    # replaces global * with .*?
    fileProcessed = re.sub(r'\\\*',r'.*?',fileProcessed)

    # letterCount = 0

    # for letter in file:
    #     # if letter in ['.','^','$','+','?','<','>','[',']','{','}','|']:
    #     #     file = file[:letterCount] + '\\' + file[letterCount:]
    #     # elif letter == '*':
    #     #     file = file[:letterCount] + '.' + file[letterCount+1:]
        
    #     letterCount += 1

    return fileProcessed

def matchGlob(glob, changedFiles):
    '''
    matchGlob Function takes the global pattern and the
    changed files and calls escapeSpecialChars on the strings 
    for the regexp engine and then uses re.search to find a match.

    Args:
    glob (string): global file pathway 
    changedFiles (list of strings): changed file pathway

    Returns:
    fileProcessed (string): file pathway processed
    '''

    # initalize corrected filepath for changedFiles removing special chars
    correctedPaths = [None]*len(changedFiles)

    # changedFile index count
    fileCount = 0

    # change format of changedFiles
    for filepath in changedFiles:
        correctedPaths[fileCount] = escapeSpecialChars(filepath)
        fileCount += 1

    # change format for global file
    globProcessed = escapeSpecialChars(glob)

    for path in correctedPaths:
        # print('Looking for "%s" in "%s" --> ' %(globProcessed, path), end=' '),
        if re.search(globProcessed, path) or globProcessed == path:
            # print('Found a Match!')
            return True
        else:
            # print('No Match!')
            return False

def sortTasks(tasksChanged, graph):
    '''
    sortTasks Function determines dependencies and sorts tasks to be run 
    in the correct order (leaf --> root)/

    Args:
    tasksChanged (list of strings): a list of tasks to be changed 
        output from the tasksToRun function.
    graph (Graph object): a Graph object that defines the dependencies
        of each task

    Returns:
    sortTasks (list of strings):
        a list of task names that should re-run in the correct order.
    '''

    for item in tasksChanged: 
        print(graph.deps[item])



def test_tasksToRun(calculated, true):
    '''
    test_tasksToRun Function checks that the answer is correct
    and prints if the test has passed.

    Args:
    calculated (list of strings): a list of tasks to be changed 
        output from the tasksToRun function.
    true (list of strings): true list of tasks to be changed.

    Returns:
    tasksChanged (list of strings):
        a list of task names that should re-run.
    '''

    # check if equal and output to terminal if test passed!
    if calculated == true:

        print('Test Passed!!!')

    else:
        print('Test did not pass :(')


if __name__ == "__main__":
    
    # test taskDefinitionsInput
    taskDefinitionsInput = [
        "task: eatDinner",  "files: kitchen-setup.txt plates.txt",  "deps: cookRice bakePotatoes setupPlates", "",
        "task: cookRice",  "files: kitchen-setup.txt rice-instructions.txt",  "deps:", "",
        "task: bakePotatoes",  "files: kitchen-setup.txt potato-recipe.txt",  "deps:", "",
        "task: setupPlates",  "files: plates.txt",  "deps:", ""]

    # test changedFiles
    changedFiles = ["kitchen-setup.txt"]

    # define true answer
    true = [
        "cookRice",
        "bakePotatoes",
        "eatDinner",
        ]

    calculated = tasksToRun(taskDefinitionsInput,changedFiles)

    print('Expected -->  "%s"  Received -->  "%s"' %(true, calculated))

    # test answer from tasksToRun
    test_tasksToRun(calculated, true)

    # graph = Graph(taskDefinitionsInput)
    # print(graph.deps['eatDinner'])