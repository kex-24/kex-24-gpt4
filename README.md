# Horse Management Simulator

### Deadline
This work should be completed before the exercise, on **Friday 15th September**.

### Instructions
For instructions on how to do and submit the assignment, please see the assignments section of the course instructions.

### Preparation

- Read and answer all questions in Module 2: Looking Inside Classes.
- Access the OLI material via Canvas or directly at the provided webpage.

Note: The OLI material and tasks might be slightly out of line this year, so it is acceptable to read ahead if you did not find all the material.

### Learning Goals

This week's learning goals include:
* Designing Java classes
* Adding instance fields
* Adding a constructor method
* Creating getters and setters
* Using the dot operator
* Printing to the terminal
* Using the 'main' method
* Understanding scope and variable shadowing

### Troubleshooting Guide
If you have any questions or problems, follow this procedure: 

1. Look at this week's posted issues. Are other students asking about your problem?
2. If not, post a question yourself by creating a New Issue.
3. Ask a TA in person during the weekly lab. Check your schedule to see when the next lab is.

### Assignment

Your task is to create a Java simulation of managing a stable of horses. Each horse has several characteristics that you'll model in Java. Imagining a real-life scenario where managing the details of horses in a stable might be a daily task, you can understand the necessity of such a system.

#### Exercise 2.0 Our Horse Management Journey Begins

To start, create a new Java file called Horse.java in the src folder. Define the class Horse within it, and add a main method to your Horse class.

Now, let's create our first horse. Add the main method provided in Example 1 to your Horse class. Then create the variables listed below in the main method and assign the corresponding values.

- String name: Shadow
- int age: 5
- int speed: 40
- boolean isTamed: true

Example 1:

```java
class Horse {

  public static void main(String[] args) {
    // Create your variables here!

    // Print information of the assigned values
    System.out.println("This is your first horse: ");
    System.out.println("Name: " + name);
    System.out.println("Age: " + age);
    System.out.println("Speed: " + speed);
    System.out.println("Is tamed: " + isTamed);
  } // end main method

} // end class
```

Test your code and check that everything works before continuing.

#### Exercise 2.1 More Horses
Create two additional horses, bringing the total count to three. Just like before, print the information of all three horses to the console.

#### Exercise 2.2 -- Fields
Move the horse's data from being local variables inside the main method to being fields of the Horse class. Create the following fields but don't assign any values to them yet:

- String name
- int age
- int speed
- boolean isTamed

#### Exercise 2.3 -- Getters and Setters
Make all fields private and provide getters and setters for each. Follow naming conventions.

#### Exercise 2.4 -- Constructor
Implement a constructor for the Horse class to allow setting all attributes when a new Horse object is created.

#### Exercise 2.5 -- More Horses, again
Using the constructor, create two more horse objects.

#### Exercise 2.6 -- printInfo()
Create a method called printInfo() that prints all information about the horse.

#### Exercise 2.7 -- Horse Race!
Implement a method called race which will simulate a race between two horses. The horse with the higher speed wins. Print the outcome of the race.

#### Exercise 2.8 -- Variable Shadowing
Understand and solve examples of Variable Shadowing.

### Checklist 
- Create three horses directly in the main method and print their information to the console. Delete this code when done.
- Create fields for the Horse class: String name, int age, int speed, and boolean isTamed. Test modifying their values directly using the dot operator on a horse object.
- Create getters and setters for all fields, and use these to access and modify the horse's fields.
- Create a constructor method for the Horse class and create a few horses using the constructor only.
- Make the printInfo() method that prints all information about the horse.
- Create a race() method so horses can race each other. The method should take the horse which it is racing against as an argument and print the outcome.
- Look at the variable shadowing examples.

### Acknowledgment
This task was designed by:
[Your Name]

Proofreading & Bug fixes by:
[Your Name or Colleague's Name]