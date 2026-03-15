# GmE 205 – Laboratory Exercise 5: Polymorphism in Spatial Object Systems

# Overview
- This Laboratory Exercise integrates the four pillars, Encapsulation, Inheritance, Abstraction, Polymorphism, of Object-Oriented Programming within a spatial system.

# Environment Setup
- Python, VS Code, Shapely, GitHub

# How to Run
- Activate the virtual environment
- Implement polymorphic method in SpatialObject
- Implement different behavior in each subclasses
- Update analysis functions to use polymorphism

# Conceptual Reflection
1. Where does polymorphism appear in your system?
- Polymorphism appears in the implementation of the effective_area() method across different spatial classes such as Parcel, Building, and Road. Although each class shares the same method name defined in the SpatialObject base class, they implement the method differently depending on their spatial characteristics. When effective_area() is called, the correct version of the method is automatically executed based on the object’s class type.

2. How does polymorphism remove conditional logic from analysis.py?
- Polymorphism eliminates the need for conditional statements that check the type of each spatial object. Instead of writing multiple if or else conditions to determine how to calculate area, the analysis code simply calls feature.effective_area(). The object itself determines how the area should be computed, making the code cleaner, more readable, and easier to maintain.

3. Which OOP pillar allows multiple spatial classes to share a method name?
- The OOP pillar responsible for allowing multiple classes to share the same method name is polymorphism. Through polymorphism, different classes can implement the same method defined in a base class while providing their own specific behavior.

4. Why is it better for objects to compute their own area rather than using conditional logic?
- It is better for object to compute their own area becase each object known its structure and rules and new spatial objects can be added without modifying the main analysis logic. This reduces dependency on external logic, prevents complex conditional structures, and makes the system easier to extend and maintain as new spatial object types are introduced.

5. If you add a new class tomorrow (e.g., River), what changes are required in spatial.py?
- If polymorphism and inheritance are properly used, very few changes are required. You would only need to create a new subclass River that inherits from SpatialObject and implements its own version of the effective_area() method. The code becomes simpler and easier to manage because each spatial object handles its own behavior. This avoids complicated if or else statements and makes it easier to add new spatial object types later without changing the existing code.