# Part 1 of Practice for Palantir Online Interview found on:
# https://leetcode.com/discuss/interview-question/2372796/Palantir-Online-Interview
#
# Author: Sierra Bonilla
# Date: 11-03-2022

def tasksToRun(taskDefinitionsInput, changedFiles):
    print('hi')

if __name__ == '__main__':

    taskDefinitionsInput = [
        "task: taskA",
        "files: lib/foo.txt lib/bar.txt"
        "deps:",
        "",
        "task: taskB",
        "files: src/baz.txt",
        "deps:",
        "",
        "task: taskC",
        "files: README.md",
        "deps:",
        ""]
        
    changedFiles = [
        "lib/foo.txt",
        "README.md"]

    tasksToRun(taskDefinitionsInput,changedFiles)