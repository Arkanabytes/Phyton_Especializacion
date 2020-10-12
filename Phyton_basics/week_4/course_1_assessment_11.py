#Arkanabytes

#Questions
#1.-seqmut-1-1: Which of these is a correct reference diagram following the execution of the following code?
lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]

A. I.

#2.-seqmut-1-4: What will be the value of a after the following code has executed?
a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")

['holiday', 'celebrate!', 'company'] 

#3.-seqmut-1-5: Could aliasing cause potential confusion in this problem?
b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)

A.yes

#4.-seqmut-1-13: Given that we want to accumulate the total sum of a list of numbers, which of the following accumulator patterns would be appropriate?
nums = [4, 5, 2, 93, 3, 5]
s = 0
for n in nums:
    s = s + n

C.III

#5.-seqmut-1-14: Given that we want to accumulate the total number of strings in the list, which of the following accumulator patterns would be appropriate?
lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = 0
for item in lst:
    if type(item) == type("string"):
        s = s + 1
        
 D.4
 
 #6.-seqmut-1-15: Which of these are good names for an accumulator variable? Select as many as apply.
 C. total
 D. accum

 #7.-seqmut-1-16: Which of these are good names for an iterator (loop) variable? Select as many as apply.
 A. item
 C. elem
 D. char
 
 #8.-seqmut-1-17: Which of these are good names for a sequence variable? Select as many as apply.
 A. num_lst
 C. sentence
 D. names
 
 #9.-seqmut-1-18: Given the following scenario, what are good names for the accumulator variable, iterator variable, and sequence variable? You are writing code 
 that uses a list of sentences and accumulates the total number of sentences that have the word ‘happy’ in them.
 D. accumulator variable: total | iterator variable: sentence |sequence variable: sentence_lst

 #Week 4 Assessment: Accumulating Lists and Strings
 #Question from Reading 9.11 The Accumulator Pattern with Strings
 #Assign an empty string to the variable output. Using the range function, write code to make it so that the variable output has 35 a s inside it (like 
# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"). Hint: use the accumulation pattern!

ael = "python!"
app = []
for i in ael:
    app.append(i)

#Question 1
#Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1. Each character in str1 
#should be its own element in the list chars.
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []
for i in wrds:
    i = i + "ed"
    past_wrds.append(i)
