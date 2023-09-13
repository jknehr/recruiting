## Background
In this project you are going to create a model elevator system.  Modern elevators are much more complex today than when they were first invented. Today, many buildings do not have a single elevator that everyone on every floor has to wait to use; instead there are multiple elevators in multiple elevator banks, sky lobbies, express elevators, and other features of these systems aimed at a more optimal solution to moving people between floors.

### Objectives
How are these systems designed?  Let's explore some possible objectives of an elevator system:
1. It must eventually pick up a person calling it (they cannot wait forever).
2. It must eventually drop a person off who's inside the elevator to their target floor (they also cannot be stuck waiting forever).
3. It should aim to generally minimize the average total time it takes for someone to go from one floor to another, taking #1 and #2 into consideration. For example, it might be most time-optimal to service a high traffic route and let people outside of that route wait longer, but it could be in conflict with objective #2 of eventually dropping them off to their destination.  `Total time` = `caller wait time` + `elevator travel time to destination floor.`

### Call Mechanisms
In addition to having multiple conflicting objectives, elevators typically fall into 2 categories with respect to their call system:

**Type 1**: The first type is perhaps the most well known. Here, a person calls the elevator to their floor and only specifies whether they are going up or down by pushing one of two buttons.  They must then wait blindly until one of the elevators arrives at the floor.  Once they get into the elevator that comes to their floor, they then push another button inside the elevator for their target floor.  In this case, the elevator system has no information other than (a) *originating floor* and (b) *target direction* before they pick up a passenger.

**Type 2**: In the second type, a person, upon entering the elevator area, specifies which floor they want to travel to and the console immediately tells them which elevator number to wait for.  In this case, the elevator knows (a) *originating floor* and (b) *target floor* and the passenger knows which elevator to expect to come for them. Once the elevator comes to pick them up, they cannot change their floor assignment without starting over.

### Time
Lastly, time is a critical input for this system for two main reasons:
1. All information about passengers travel is not known all at once up front.  Elevator systems work in the real world where they get a continuous flow of new requests throughout the day, so the elevator system must be reactive as it learns new information about its tasks.
2. Time is one of the considerations for the system to attempt to minimize, and thus it's measurement is critical to building a successful system.

For this project, we are going to abstract out time separate from real time so we can control it precisely for our inputs and measurements.


## Requirements

Model out an elevator system in python that supports a configurable amount of elevators (e.g 1 - 10) and building floors (_n_) with a scheduling algorithm of your choice, taking into consideration the objectives mentioned above.  Please also make each elevator configurable for a maximum amount of passengers it can hold at one time. For this exercise, you can assume we will be building a **Type 2** system, where the originating floor and target floor information will be available to the system upon passenger request. Additionally, we will assume that it takes any elevator 1 time unit to move by 1 floor in either the up or down direction.

Write a function for your model that takes as input a list of requests with the following data points for each request:
1. Request Time (an integer from 0 to infinity)
2. ID (a string identifier for a passenger)
3. Source Floor (integer between 1 and n, the number of floors)
4. Target Floor (integer between 1 and n, the number of floors)

Time can be specified more than once in this list but always increases. The passenger ID is expected to be unique for all entries.  For example, in the following CSV, the list might contain a sequence of passenger requests indicating that at time 0 two people made requests at the same time, and then jump ahead to time 10 for the third request.
```csv
time,id,source,dest
0,passenger1,1,51
0,passenger2,1,37
10,passendar3,20,1
```

The function should exit once all input requests have been processed by the system AND all passengers have been delivered to their final destination floors.  **You will be penalized if you "look ahead" in the request queue beyond your current time.**


This function should output:
1. What floor each elevator is at for every point in time to a file.  Even if the input does not have continuous time (like in the example above it skips from time 0 to time 10), you should tick time forward by 1 unit in continuous fashion, logging the locations of each elevator in the system at all times.
2. Before exiting, the function should also write out summary statistics for what the min, max, and mean `total time` and `wait times` were for all passengers.  Have a look at the full distribution - what information stands out to you?


## Deliverables
1. Deliver your solution as a python project committed into a publicly accessibly Github repository.
2. Write a README file that explains how to run your solution.  Also include a short discussion about your assumptions and what simplfications or trade-offs you thought through during your time with this project.
3. You will be presenting your solution in front of the team in the office.  Be prepared with any additional resources you might want available to you for that presentation.

