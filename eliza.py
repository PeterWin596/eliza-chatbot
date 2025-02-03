# eliza.py
# Author: Peter Nguyen
# Class: CMSC 437
# Date: 1/29/2025

"""
OVERALL COMMENT:

1) Problem Description:
This program implements a simple chatbot named Eliza, designed to simulate a conversation with a psychotherapist. 
The goal is to engage the user in a dialogue, spot keywords in their input, and respond in a way that mimics human-like interaction. 
The program uses regular expressions to identify patterns in the user's input and transforms statements into questions to keep the conversation flowing.

2) Example Input and Output:
Input:
-> [eliza] Hi, I'm a psychotherapist. What is your name?
=> [user] My name is Peter.
-> [eliza] Hi Peter. What troubles you?
=> [Peter] My dog is freaking me out.
-> [eliza] Why is your dog freaking you out, Peter?
=> [Peter] My dog keeps barking at the corner of my room at night.
-> [eliza] Why do you think your dog is barking, Peter?
=> [Peter] I think my room is haunted.
-> [eliza] What makes you believe your room is haunted, Peter?

Usage Instructions:
1. Run the program using the command: `python3 eliza.py`.
2. Follow the prompts and type your responses.
3. To exit the program, type "quit", "exit", or "bye".

3) Algorithm:
- Step 1: Greet the user and ask for their name.
- Step 2: Extract the user's name using regular expressions.
- Step 3: Ask the user what troubles them.
- Step 4: Enter a loop to continuously read user input.
  - Step 4.1: Check for exit conditions (e.g., "quit", "exit", "bye").
  - Step 4.2: Use regular expressions to spot keywords in the user's input.
  - Step 4.3: Respond with a related question or statement based on the spotted keyword.
  - Step 4.4: If no keywords are found, use a default response to keep the conversation going.
- Step 5: Exit the program when the user types an exit command.
"""

import re
import random

def eliza():
    print("-> [eliza] Hi, I'm a psychotherapist. What is your name?")
    name = input("=> [user] ").strip()
    
    # Extract the name using regex (e.g., "My name is Peter" -> "Peter")
    name_match = re.search(r"(?:my name is|i am|im|i'm) (\w+)", name, re.IGNORECASE)
    if name_match:
        name = name_match.group(1)
    else:
        name = "friend"  # Default if no name is provided
    
    print(f"-> [eliza] Hi {name}. What troubles you?")
    
    while True:
        user_input = input(f"=> [{name}] ").strip().lower()
        
        # Exit condition
        if user_input in ["quit", "exit", "bye"]:
            print(f"-> [eliza] Goodbye, {name}. Take care!")
            break
        
        # Word spotting and responses
        if re.search(r"\bcrave\b", user_input):
            responses = [
                f"Why do you think you crave that, {name}?",
                f"What do you think would happen if you satisfied your craving?",
                f"Tell me more about your cravings, {name}."
            ]
            print(f"-> [eliza] {random.choice(responses)}")
        
        elif re.search(r"\bfeel\b", user_input):
            responses = [
                f"Why do you feel that way, {name}?",
                f"What do you think is causing you to feel this way?",
                f"How long have you been feeling this way, {name}?"
            ]
            print(f"-> [eliza] {random.choice(responses)}")
        
        elif re.search(r"\bfamily\b", user_input):
            responses = [
                f"Tell me more about your family, {name}.",
                f"How does your family make you feel?",
                f"What role does your family play in your life, {name}?"
            ]
            print(f"-> [eliza] {random.choice(responses)}")
        
        elif re.search(r"\bhate\b", user_input):
            responses = [
                f"Why do you hate that, {name}?",
                f"What do you think would happen if you didn't hate it?",
                f"How does hating that affect you, {name}?"
            ]
            print(f"-> [eliza] {random.choice(responses)}")
        
        elif re.search(r"\blove\b", user_input):
            responses = [
                f"Why do you love that, {name}?",
                f"How does loving that make you feel?",
                f"What does loving that mean to you, {name}?"
            ]
            print(f"-> [eliza] {random.choice(responses)}")
        
        elif re.search(r"\bwant\b", user_input):
            # Transform statements like "I want X" into "Why do you want X?"
            match = re.search(r"i want (.*)", user_input)
            if match:
                responses = [
                    f"Why do you want {match.group(1)}, {name}?",
                    f"What would it mean to you if you got {match.group(1)}?",
                    f"How would getting {match.group(1)} change your life, {name}?"
                ]
                print(f"-> [eliza] {random.choice(responses)}")
            else:
                print(f"-> [eliza] I didn't quite understand. Can you say that another way?")
        
        elif re.search(r"\bsad\b", user_input):
            responses = [
                f"Why do you feel sad, {name}?",
                f"What do you think is making you feel this way?",
                f"How can I help you feel better, {name}?"
            ]
            print(f"-> [eliza] {random.choice(responses)}")
        
        elif re.search(r"\bhappy\b", user_input):
            responses = [
                f"Why do you feel happy, {name}?",
                f"What do you think is causing this happiness?",
                f"How can you hold onto this feeling, {name}?"
            ]
            print(f"-> [eliza] {random.choice(responses)}")
        
        # New rules for dog, barking, and haunted
        elif re.search(r"\bdog\b", user_input):
            responses = [
                f"Why is your dog freaking you out, {name}?",
                f"What do you think is bothering your dog?",
                f"How does your dog's behavior affect you, {name}?"
            ]
            print(f"-> [eliza] {random.choice(responses)}")
        
        elif re.search(r"\bbarking\b", user_input):
            responses = [
                f"Why do you think your dog is barking, {name}?",
                f"What do you think your dog is trying to tell you?",
                f"How do you feel when your dog barks at night, {name}?"
            ]
            print(f"-> [eliza] {random.choice(responses)}")
        
        elif re.search(r"\bhaunted\b", user_input):
            responses = [
                f"Why do you think your room is haunted, {name}?",
                f"What makes you believe your room is haunted?",
                f"How does the idea of a haunted room make you feel, {name}?"
            ]
            print(f"-> [eliza] {random.choice(responses)}")
        
        else:
            # Default response if no keywords are spotted
            responses = [
                "I'm not sure I understand. Can you elaborate?",
                "Can you tell me more about that?",
                "Why do you say that?",
                "What do you mean by that?",
                "How does that make you feel?"
            ]
            print(f"-> [eliza] {random.choice(responses)}")

if __name__ == "__main__":
    eliza()