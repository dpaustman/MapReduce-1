# MapReduce
Project implementation for FINKI
<br />
<br />
It has 2 different Python files, with each performing its own task.<br />

1. <b>list_friends.py</b> : Given a simple social network dataset consisting of a set of key-value pairs (person, friend) representing a friend relationship between two people. This python program implements a MapReduce algorithm to produce a complete list of friends for each person.<br />
2. <b>pairs_of_friends.py</b> : A python program implements a MapReduce algorithm to identify symmetric friendships in the input data. The program will output pairs of friends where personA is a friend of personB and personB is also a friend of personA. If the friendship is asymmetric (only one person in the pair considers the other person a friend), do not emit any output for that pair.<br/>

# Map Input 
The input is a 2 element list: [personA, personB]
personA: Name of a person formatted as a string
personB: Name of one of personA’s friends formatted as a string
This implies that personB is a friend of personA, but it does not imply that personA is a friend of personB. 
# Reduce Output
The output should be a (person, friend count) tuple.
person is a string and friend count is an integer describing the number of friends ‘person’ has.



