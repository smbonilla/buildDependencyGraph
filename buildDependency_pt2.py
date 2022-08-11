# Part 2 of Practice for Palantir Online Interview found on:
# https://leetcode.com/discuss/interview-question/2372796/Palantir-Online-Interview
#
# Author: Sierra Bonilla
# Date: 11-03-2022

# built-in RegEx Module
import re


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

        # initialize tasksChanged 
        tasksChanged = []

        # count current line number
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
                    if currline[i + 1] in changedFiles:
                        
                        # return only name of the task
                        taskLine = taskDefinitionsInput[lineCount - 1].split()

                        # check if already added before
                        if taskLine[1] not in tasksChanged:
                            tasksChanged.append(taskLine[1])

            # increment line count
            lineCount += 1

        return tasksChanged

    else:
        print('All inputs must be strings!')


def test_tasksToRun(calculated, true):
    '''
    test_tasksToRun Function checks that the answer is correct
    and prints if the test has passed.

    Args:
    calculated (list of strings): a list of tasks to be changed 
        output from the tasksToRun function.
    true (list of strings): true list of tasks to be changed.

    :
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
        "task: distributeImages",
        "files: images/dogs/*.jpg images/*/*.png",
        "deps: compressJpegs compressPngs",
        "",
        "task: compressJpegs",
        "files: images/dogs/*.jpg",
        "deps:",
        "",
        "task: compressPngs",
        "files: images/*/*.png",
        "deps:",
        ""]

    # test changedFiles
    changedFiles = [
        "images/dogs/dalmatian.jpg",
        "images/dogs/retriever.jpg"
        ]

    # define true answer
    true = [
        "compressJpegs",
        "distributeImages"]

    calculated = tasksToRun(taskDefinitionsInput,changedFiles)
    print(calculated)

    # test answer from tasksToRun
    test_tasksToRun(calculated, true)