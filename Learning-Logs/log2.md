- Question: Still confused on what stable means?
- When Identified: 8/31/26 10:50 am
- Importance: 3
- How to Learn: Ask AI, do some online research 
- Insight/Answer: Stable means that ties won't be determined or moved relative to each other. If there is a tie a stable algorithm would ensure that after being sorted the ties appear in the same order as they were originally relative to each other.
- Hours Spent Learning: 5 min
- Minutes Spent Documenting: 3
- Confidence: 5

- Question/Problem: What is the difference between the Fisher Yates algorithm and selection sort? 
- When Identified: 8/31/26 10:45 am
- Importance: 3
- How to Learn: Do some online research, ask AI, watch a video 
- Insight/Answer: Fisher Yates algorithm isn't used for sorting, it is just used to get a randomized permutation of an array where is permutation is equally likely because you are drawing randomly
- Hours Spent Learning: 3 min
- Minutes Spent Documenting: 4 min
- Confidence: 5

- Question/Problem: What is the big O of merge sort?
- When Identified: 8/31/26 8:20 pm
- Importance: 3
- How to Learn: look it up, see why it is that big O 
- Insight/Answer: merge sort has a big O time of O(nlog(n)) time complexity with a space complexity of O(n). This occurs because splitting an array down to single elements is O(log(n)) and then comparing each of those elements is traversing the array which is O(n) so the two multiplied is O(nlog(n)). Space complexity is O(n) because at worst case you need an entire copy of the array which is O(n)
- Hours Spent Learning: 4 min
- Minutes Spent Documenting: 3 min
- Confidence: 4


- Question/Problem: What is the concept of quicksort?
- When Identified: 8/31/26 8:20 pm
- Importance: 3
- How to Learn: look online, watch a video 
- Insight/Answer: You pick an element of the array to act as your pivot, you traverse the array and put numbers less than it on one side and numbers larger on the other, then you use recursion to do the same thing to the two halves
- Hours Spent Learning: 3 min
- Minutes Spent Documenting: 3 min 
- Confidence: 4

- Question/Problem: What is the big O of quicksort?
- When Identified: 8/31/26 8:20 pm
- Importance: 4
- How to Learn: look it up 
- Insight/Answer: time complexity on average is big O O(nlog(n)) and at worst case O(n^2). with a wort case space complexity of O(n). This is because if it doesn't have anything to split on either the left or the right depending on how bad your pivot is, it has to run more itterations to hit the base case. Space complexity is because once again at most you have to store the entire array
- Hours Spent Learning: 7 min
- Minutes Spent Documenting: 5 min
- Confidence: 3

- Question/Problem: Previously I was using a recursive call on selection_sort with an optional parameter of index_to_start but this exceeded the call stack limit 
- When Identified: 8/31/26 8:44 pm
- Importance: 5
- How to Learn: Examine my code and find another approach
- Insight/Answer: I had to do an outside for loop instead of a recursive call
- Hours Spent Learning: 5 min
- Minutes Spent Documenting: 4 min
- Confidence: 4
