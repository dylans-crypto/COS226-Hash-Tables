# COS226-Hash-Tables
5 different hash function methods including in order of commits; linked list (bad hash fuction), linked list (good hash fuction), linear probing (bad hash function), linear probing (good hash function), and linear probing (good hash function and good table size). 

1. Results/what happened
Linked list (bad hash fuction)
Title Hash Table
Wasted space: 6544 wasted spaces , Collisions: 50410
Time taken: 0.015581846237182617 seconds

Quote Hash Table
Wasted space: 7116 wasted spaces , Collisions: 59621
Time taken: 0.021618366241455078 seconds

This approach allowed for a large number of collisions and a decent amount of wasted spaces. 
The linked list approach does cause collisions very easily, but the poor hash function seems to have clustered a lot of data into the same spots.

Linked list (good hash fuction)
Title Hash Table
Wasted space: 3240 wasted spaces , Collisions: 15711
Time taken: 0.027266502380371094 seconds

Quote Hash Table
Wasted space: 3037 wasted spaces , Collisions: 25303
Time taken: 0.04059338569641113 seconds

Swapping to a better hash function seems to have reduced the number of wasted space and collisions by a great deal.
Even though the wasted space and collisions have been reduced the time to complete has increased by a bit.

Linear probing (bad hash function)
Title Hash Table
Wasted space: 3749 wasted spaces , Collisions: 56165481
Time taken: 4.993705749511719 seconds

Quote Hash Table
Wasted space: 3023 wasted spaces , Collisions: 51111873
Time taken: 4.413541078567505 seconds

This approach was the worst out of all the methods. The amount of collisions and time to complete were entirely larger than the other methods. 
However the wasted spaces weren't to bad, but thats kind of expected from the linear probing idea. 

Linear probing (good hash function)
Title Hash Table
Wasted space: 3749 wasted spaces , Collisions: 21069
Time taken: 0.027713537216186523 seconds

Quote Hash Table
Wasted space: 3023 wasted spaces , Collisions: 34951
Time taken: 0.04388689994812012 seconds

This method was an extreme improvement from the first unoptimized linear probing approach. 
The good hash function reduced the amount of collisions by an insane amount in turn causing the time to complete to drop as well. 
However wasted spaces didn't actually change at all due to the function that created the table size and the linear probing approach.

Linear probing (good hash function and good table size)
Title Hash Table
Wasted space: 10181 wasted spaces , Collisions: 7128
Time taken: 0.025095462799072266 seconds

Quote Hash Table
Wasted space: 9455 wasted spaces , Collisions: 9041
Time taken: 0.03741860389709473 seconds

With a good hash function and a larger prime number table size this approach was able to reduce collisions a lot from the previous method.
However the tradeoff for more wasted space can kind of be countered by the time to complete still being decreased.

2. Comparison
When looking between the linked list and linear probing approach there are a good bit of differences and reasons as to why it is that way.
First between the 2 functions the way to get the table size was different and the linear probing method didn't have a ton of space to work with.
However this is something that the linked list approach doesn't have to worry much about as it will just continue to push the data in.
So looking more at collisions, when both had bad hash functions linked list was the clear winner. However when both had good hash functions they both produced very similar results.
Overall in this case linked list seems to be better, but how I did the table size between the 2 probably didn't help.

The difference between a bad and good hash function was huge. Without a good hash function (at least in my result) linear probing was terrible.
No matter which approach the hash function made a huge impact on the amount of collisions and helped both approaches a good bit.

The final optimization that I did was to the linear probing approach because I didn't feel like I really gave it enough space to work with.
So when I gave it a larger table size and made sure it was a prime number there was a good difference. 
Of course the amount of empty spaces increased, but the amount of collisions became the best out of any of the methods and the time to complete was only beat by one.

3. Overall Most Effective
The best methods overall were linear probing with a good hash function and table size, and linked list with a good hash function.
While the linear probing had the least collisions and a very good runtime the linked list was very good overall without anything being to crazy.

4. Conclusion
In conclusion the linked list method seems to be far more forgiving for everything that can effect it.
Where as the linear probing method seems to require a good hash function and a good table size.
However no matter the method used they will see a great improvement when a good hash function is used.

