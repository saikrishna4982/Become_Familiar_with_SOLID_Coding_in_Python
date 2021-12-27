# Become Familiar with SOLID Coding in Python
In the Above File I took an example of ElectricBulb to Explain SOLID Principles, Now let's look How the Example Covers All the **SOLID** Principles
### 1.Single Responsibility Principle : 
The Main aim of SRP is the class or method should have only one job to do, So in the example if you see there are two classes switch and lightbulb, whose job is turn on/off the light depending on the switch which states that it has only one task to do 
### 2.Open Closed Principle : 
OCP States that the class/function should be open for extension but closed for modification, In the above example if we want to add any extra features such as getting different color lights we can add that by adding list of colors we want to display in Ligtbullb class and how we should display, thereby we are just adding functionaity to the bulb instead of modifing the code
### 3.Liskov Substitution Principle :
LSP Defines that if a subclass redefines a function present in base class then there should not be any difference in behaviour of the function and it is a substitute for the base class, So in The example we have two classes Device,LightBulb where LigtBulb is inheriting the properties of Device class and redfining the behaviour of methods present in base class without changing it's behaviour
### 4.Interface Segregation Principle :
The Interface Segregation Principle states that clients should not be forced to implement interfaces they don't use. Instead of one fat interface many small interfaces are preferred based on groups of methods, each one serving one submodule.The Above Example Contains only the necessary interfaces that client require to turn on the bulb
### 5.Dependency Inversion Principle :
DIP states High-Level Modules should not depend on Low-Level Modules Both Should dependon abstractions. Abstractions should not depend on details. Details should depend on abstractions, in the Example file we have a LightBulb class(Low-Level) class which depends on Device class(High-level) class there by Following DIP

### You can run the File By Using the Following Steps:
1.Clone the File into your local machine<br>
2.Open Command Prompt and navigate into the Downloaded file Folder<br>
3.Type '''python SOLID.py'''<br>
4.By Default you will see output as **Truned On** if you want to Turn off add **s.toggle()** at the end of code.<br>
