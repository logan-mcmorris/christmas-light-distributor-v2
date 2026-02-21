# Christmas Light Distributor v2
This distributor takes different amounts of different items in a list and sorts them so they "appear" even when lined up, accounting for looping. **This project is incomplete.** Some code doesn't have a use and some is meant to serve a later, never implemented purpose. Please use the second version; the first is inefficient and is included for historic purposes.

<img width="633" height="70" alt="image" src="https://github.com/user-attachments/assets/6d3b81d8-9dc5-4335-8a65-a96d0b2bbdad" />

## Personal Anecdotes
### Why I made this
I got a set of screw-on Christmas lights that came with 18 red and green bulbs, but only 12 blue and yellow bulbs. The question: how do I order these lights so they look even? After my friend showed me a better solution than I thought was possible, I tried to code an algorithm to solve it. After programming my first version, there were still issues with inaccurate results and an incredibly slow time complexity of O(n!), motivating me to code an improved version.

### What I learned
This project was one of the most beneficial projects from a learning standpoint. I learned:
- Defining and approaching a problem with an ambiguous solution
- Collaborating with others to brainstorm solutions
- How to code recursive functions
- How to utilize the Cartesian product of lists
- How to code greedy algorithms
- Advanced list comparisons
- Approaching problems in different ways to improve efficiency

While this program didn't teach me about time complexity, it helped me understand it later down the road.

### Next steps
This project has been in the works off and on for over a year. I want to code a third version using a greedy algorithm, which would be fast and provide "best" solutions, even if there isn't a perfect one.

### Problems
This project was a nightmare to code due to these main problems:
- "How do you order lights in a way that looks the best?" is ambiguous and can be defined in many ways, yielding different solutions
- It was incredibly difficult to visualize this problem and how it would work
- Iterating and analyzing through different amounts of different objects is inherently slow (hence the second version)
- Making the algorithm work for looping fundamentally changes the entire approach

## How it works
It's worth noting that this program is much more complex than it needs to be, but currently lacks the functionality of analyzing the best solution which would benefit from this complexity.

### New version:
1. Set up the dictionary to include the items and the amount.\
  `mainDict = {'🔴':2, '🟢':2}`<br><br>
2. The program takes the dictionary and distributes them evenly into a list of lists. A placeholder is used to keep the empty space.\
  `[['🔴', 'X', '🔴', 'X'], ['🟢', 'X', '🟢', 'X']]`<br><br>
3. The program generates the every looping configuration of the lists. For optimization, it prevents the first sublist from iterating.\
   `[[['🔴', 'X', '🔴', 'X']], [['🟢', 'X', '🟢', 'X'], ['X', '🟢', 'X', '🟢']]]`<br><br>
4. The cartesian product is taken of the sublists.\
   `[(['🔴', 'X', '🔴', 'X'], ['🟢', 'X', '🟢', 'X']), (['🔴', 'X', '🔴', 'X'], ['X', '🟢', 'X', '🟢'])]`<br><br>
5. The lists are "slid" on top of each other, and if every spot is taken up, we have a perfect solution.
   ```
   These don't slot in.    | These do.
   ['🔴', 'X', '🔴', 'X'] | ['🔴', 'X', '🔴', 'X']  
   ['🟢', 'X', '🟢', 'X'] | ['X', '🟢', 'X', '🟢']
   ```
Output: `Semi-perfect solution found: 🔴🟢🔴🟢🔴🟢🔴🟢`<br><br>
The original plan included finding the best solution if a perfect one didn't exist by sliding individual elements into "slots" nearby. This proved to be difficult and will instead be implemented into version 3.

### Old version:
In the old version, the program generates a list of permutations of all of the lights combined. It then calculates the distances between each item of the same time, then the average of those distances, then the deviation of those averages. If the new candidate has an equal or smaller deviation than the previous candidate, it is printed. This is inefficient, yields answers that are identical (just shifted), and yields imperfect answers.

<img width="997" height="433" alt="image" src="https://github.com/user-attachments/assets/c0d0736b-50a3-4a65-b56e-5a3870ac8879" />
