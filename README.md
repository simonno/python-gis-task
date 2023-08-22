**Carefully read the task and please check the examples of output in the end of the description**

## Task
You have to develop a streets colouring algorithm using python3. Your algorithm should paint lines in the same colour when you think it is a **single street**.
1. You don't have to match coordinates with streets from real world. Those streets were taken just for example.
2. You **CAN** use any 3-rd party libraries, but you **CAN'T** use 3-rd party services.
3. Create a solution just based on the information in the file from sample directory.
4. It's an just an algorithimic task.
5. What is a street? You have to tailor a best-fitting algorithm which will result as you think to best results of trying to be 

## Definition of a "Single Street":

A "single street" is a continuous line segment without interruptions. Your task is to decide when multiple line segments should be regarded as one continuous street. Consider:

**Continuity:** Roads, even when changing direction, remain unbroken. Determine what might interrupt a street's continuity.

**Crossroads:** At intersections, some lines might belong to the same street. Evaluate the angles between intersecting segments to help deduce this.
Rely on patterns in the sample data, as specific geoinformation isn't provided. Use your creativity.

## Requirements:
- Don't fork this repo, just create your own.
- Attach result of your solution to repo. Just put an image into repository and name it "solution.png"
- Generated image size: 3000x3000px
- Your repo with solution should contain file with explanation of how your algorithm works (it can be added to README.md with section Explanation)

## What is not acceptable
- Just randomly colouring lines

## Examples
### Initial image
![Initial data](https://raw.githubusercontent.com/zakhar-bozhok-jito/jun-python-gis-test-task/master/out-examples/initial.png)
### Possible accepted solution
Possible generated output of the solution. Some of different lines were occasionaly colourized the same color.
![Sample output1](https://raw.githubusercontent.com/zakhar-bozhok-jito/jun-python-gis-test-task/master/out-examples/processed-solid.png)
### Possible accepted solution
Possible generated output, but lines have also different line styles.
![Sample output2](https://raw.githubusercontent.com/zakhar-bozhok-jito/jun-python-gis-test-task/master/out-examples/processed.png)
