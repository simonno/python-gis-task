# Task Description

**Carefully read the task and please check the examples of output at the end of the description.**

## 🤓 Task
You are tasked with developing a street colouring algorithm using Python3. Your algorithm should color lines in the same color when perceived as a **single street**.

1. You don't need to match coordinates with real-world streets; the streets provided are purely examples.
2. You **CAN** utilize third-party libraries, but **CAN'T** employ third-party services.
3. The solution should solely be based on the information in the file from the sample directory.
4. This is primarily an algorithmic task.
5. How to determine a street? Craft an algorithm that, in your opinion, yields the most accurate representation of distinct streets.

## ❓ Definition of a "Single Street"
A "single street" is an uninterrupted line segment. Determine when multiple line segments can be considered as one continuous street. Consider:

- **Continuity:** Roads, despite changing direction, are continuous. Think on what could disrupt a street's flow.
- **Crossroads:** At junctions, certain line segments might be part of the same street. Analyze the angles between intersecting lines for insights. Base your decisions on the patterns observed in the sample data, keeping in mind that specific geoinformation is absent. Be creative.

## ⚠️ Requirements
- Instead of forking this repository, create your own.
- Attach the result of your solution to your repo. Place an image in the repository and name it "solution.png".
- The image's dimensions should be 3000x3000px.
- Your repository should include a file detailing how your algorithm operates. This can be added to the README.md under the "Explanation" section.

## ❌ What is not acceptable
- Randomly coloring the lines without logic.

## 🤔 Examples
### ℹ️ Initial image
![Initial data](https://raw.githubusercontent.com/zakhar-bozhok-jito/jun-python-gis-test-task/master/out-examples/initial.png)

### ✅ Possible accepted solution
Generated output where different streets might occasionally have the same color.
![Sample output1](https://raw.githubusercontent.com/zakhar-bozhok-jito/jun-python-gis-test-task/master/out-examples/processed-solid.png)

### ✅ Another possible accepted solution
Generated output with varied line styles.
![Sample output2](https://raw.githubusercontent.com/zakhar-bozhok-jito/jun-python-gis-test-task/master/out-examples/processed.png)
