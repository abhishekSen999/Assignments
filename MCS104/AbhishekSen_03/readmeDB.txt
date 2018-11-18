MCS 104 DBMS Assignment
Submitted By : Abhishek Sen
Roll:03
_____________________________________________________________________________________________________________________________________________________

Given a set of attributes and functional dependencies. We have to find the following:
1.Closure of an attribute 
	The set of all those attributes which we can functionally determine from an attribute set is called as a closure of 
	that attribute set. Closure of attribute set {X} is denoted as {X}+.
	
2.Candidate Key 
	Candidate Key is minimal set of attributes of a relation which can be used to identify a tuple uniquely.  Each table 
	may have one or more candidate keys, but one candidate key is unique, and it is called the primary key.

3.Equivalent fds 
	Let FD1 and FD2 are two FD sets for a relation R.
	a . If all FDs of FD1 can be derived from FDs present in FD2, we can say that FD2 ? FD1.
    	b . If all FDs of FD2 can be derived from FDs present in FD1, we can say that FD1 ? FD2.
    	c . If a and b both are true, then we say that FD1 and FD2 are equivalent.

4.Canonical Cover
	A canonical cover of a set of functional dependencies is such that it logically implies all dependencies and no functional 
	dependency in canonical cover contains an extraneous attribute.

5.Normal Form
	The stage at which a table is organized is known as its normal form (or a stage of normalization). There are 4 basic 
	normal forms.  
		a. First normal form (1NF) 
		b. Second normal form (2NF)
		c. Third normal form (3NF)
		d. Boyce-Codd normal form (BCNF)

---------------
Functions used:
---------------
closure                            : To find the closure of given attributes.Takes 'attribute(s)' and set of fds as input
candidate_key                      : To find all the candidate keys.Takes FDs and set_of_attributes as input
equivalent_functional_dependencies : Returns true when two FDs are equivalent. takes Two FDs as input
canonical_cover                    : Returns canonical cover. Takes FD as input
two_nf                             : Returns true if FDs are in 2NF
three_nf                           : Returns true if FDs are in 3NF
bcnf                               : Returns true if FDs are in BCNF

---------------------------------------------------------------------------------------------------------------
Logic is explained in the Jupyter file with the code flow(kindly execute all the cell ones before testing to avoid name error). 
if Jupyter Notebook is not present then a HTML version of the file is available with few tested inputs.
---------------------------------------------------------------------------------------------------------------
 