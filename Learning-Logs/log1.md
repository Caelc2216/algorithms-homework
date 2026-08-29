<!-- Template, Don't use -->
- Question/Problem: 
- When Identified: 
- Importance: 
- How to Learn: 
- Insight/Answer:
- Hours Spent Learning: 
- Minutes Spent Documenting: 
- Confidence:


- Question/Problem: You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
- When Identified: 8/27/26 4:50PM
- Importance: 2, I can't think of a real scenerio in which I would need this
- How to Learn: I want to try brute forcing it first and then see if I can come up with a better method
- Insight/Answer: Finished brute forcing it using a nested for loop at 5pm. To make it faster I want to try adding a check to make sure we don't check the the second for loop on values that have already been run through the outside for loop. To solve this I have the inside loop start at the outer loop i+1, this drops the time but not significantly. 
- Hours Spent Learning: 1
- Minutes Spent Documenting: 5
- Confidence: 3

- Question/Problem: What is a HashMap and how does it work? 
- When Identified: 8/27/26 6:03 PM
- Importance: 4, I think it is important to understand the different data structures since they can help us improve algorithms
- How to Learn: Do some research using the internet and AI and practice using the data structure
- Insight/Answer: A HashMap is like what a dictionary is, it uses a hash function to compute the 'index' of an array so when given the key that was used to create the hash originally it gets the index and can look it up that way. I was able to return back to the question above and solve it with a lower big O using HashMaps aka a Dictionary.
- Hours Spent Learning: 1
- Minutes Spent Documenting: 8 
- Confidence: 4

- Question/Problem: How you can test agentic prompting?
- When Identified: 8/28/26 9:00 am 
- Importance: 2
- How to Learn: Do some online research and watch a video, ask others what they use
- Insight/Answer: In the conference someone mentioned a software called promptfoo
- Hours Spent Learning: 1
- Minutes Spent Documenting: 7
- Confidence: 2

- Question/Problem: What is vertical slice architecture?
- When Identified: 8/28/26 9:30 am
- Importance: 3
- How to Learn: Do some online research, watch some videos and look at some diagrams
- Insight/Answer: Vertical Slice architecture is when you structure your code base so that each 'slice' contains all of the files that it needs. A slice is a specific use case or functionality. This architecture means you develop across different traditional architecture layers frontend,backend,UI,databases all at once to implement that one feature, then continue. 
- Hours Spent Learning: 20 min
- Minutes Spent Documenting: 3 
- Confidence: 4

- Question/Problem: What is XP in programming? The term was used in the conference and I want to have a deeper understanding of what it means
- When Identified: 8/28/26 1:00 pm
- Importance: 3
- How to Learn: Do some research, ask AI, watch some videos
- Insight/Answer: I must've learned this before but have since forgotton the vocabulary of the phrase XP. XP is an agile workflow that focuses on communication, simplicity, feedback, courage, and respect. Some of the things that are often associated with XP programming are pair programming, continuous integration, simple design, TDD, and refactoring.
- Hours Spent Learning: 0.5
- Minutes Spent Documenting: 3
- Confidence: 5

- Question/Problem: How do I track the base case of a selection sort?
- When Identified: 8/28/26 8:16 pm
- Importance: 3
- How to Learn: Think about what the base case is and try different implementations until it works properly 
- Insight/Answer: I decided to add an optional parameter called index_to_start at who's default value is 0, on a recursive call if index_to_start != length_of_array - 1 it increments index_to_start before calling the function again. This added it's own problem of an out of index error because I wasn't checking if the length of the array was 0 before trying to subtract from it.
- Hours Spent Learning: 20 min
- Minutes Spent Documenting: 5
- Confidence: 3

- Question/Problem: 
- When Identified: 
- Importance: 
- How to Learn: 
- Insight/Answer:
- Hours Spent Learning: 
- Minutes Spent Documenting: 
- Confidence:
