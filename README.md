> **COMP 801 Integrated  Computing Practice**
## Lab 1
### Due Dates
- Assigned week 2
- Due before midnight before week 3 class

### Topic
- Learn some basics about DevOps tools:
  - terminal utility (Windows, MacOS, Linux), bash shell, VS Code
  - Python package installer `pip` (or `pip3` for MacOS)
  - Python package `pytest` installation and use
- Develop two functions using Python language
- Get exposure to test-driven development and version control

### Prerequisites
- Python 3 and VS Code are installed
- Terminal utility in VS Code and/or terminal utility in your account
  - Can deactivate `conda`
  - See **Terminal Utility Basics** resource in Canvas

### Getting Started
#### In a terminal utility of your operating system
- Change directory from `home directory` to `comp801` folder
  - If you don't have a `comp801` folder, create one.
- Clone the remote repo from the GitHub org for the course into your `comp801` folder
  - `git clone <remote-repo-url> lab1`
- Verify that `lab1` folder was created: `ls -al`
- Inspect the content of the folder: `ls -al lab1`
- Verify that `pytest` is installed and on the `$PATH`

#### In VS Code
Open VS Code
- Select **File --> Open Folder ...** from the top menu bar
- Locate the cloned `lab1` folder on your laptop and open it
- Inspect the content of `lab1` folder
  - `README.md` has the lab description and requirements
- Open each `.py` file and run it
  - Select the Run icon (upper right corner), OR
  - In VS Code terminal window
    - Run the command `python xxx.py`, where `xxx.py` is the name of the file.
    - **NOTE**: On MacOS, the command is `python3 xxx.py`

### Develop Solution to lab1
#### Start with Documentation 
In the module docstring for `core.py`:
- Enter your name as developer of the program
- Enter the name of your collaborator(s) to give attribution to their participation

For all the other modules (`client.py`, `test_div_nums.py`, and `test_last_chars.py`):
- Write a module docstring with all the required information.

**Version control Step 1**: In the terminal window, run the commands:
```
git status
git add .
git status
git commit -m 'write module docstrings`
git status
```

#### Write Test Cases
There are two **testing modules**, each for each function in `core.py`
  - `test_div_nums.py`
  - `test_last_chars.py`
Each **testing module** must have 2 testing functions
- Follow the testing function example in `test_div_nums.py` to:
  - Write the 2nd testing function for `test_div_nums.py`

**Version control Step 2**: 
- Run the `git` commands as shown at the previous step
- The commit message is 'implement test case for div_nums()`

**NOTE**: You'll write the other 2 testing functions for `test_last_chars.py` AFTER 
  you complete the development cycle for the `div_nums()` funcction.

#### Design
DESING.md file is a Markdown file in which we write the problem solving steps for each function in `core.py`. 
- Start with the design for `div_nums()`

**NOTE**: You'll write the design for `last_chars()` AFTER you complete the 
development cycle for `div_nums()`. 

**Guideline**: Apply the accumulation pattern
  - What's the accumulator? 
  - What are the components of the iteration? 
    - What's the loop variable (or iterator)? 
      - What's a suggestive name for the loop variable? 
      - What's the data type of the loop variable?
    - What's the iterable? 
    - What happens at each iteration step?

**Version control Step 3**:
- Run the `git` commands as shown at the previous step
- The commit message is 'design div_nums()`

#### Implementation
Use the design to write the implementation.
- Start with the implementation of `div_nums()`
- Run the tests for this function
- If there are errors, find the fix, correct the code, and updated the design 
(if needs clarification or updating)
- When no more errors, commit the changes. 

**Version control Step 4**:
- Run the `git` commands as shown at the previous step
- The commit message is 'implement div_nums()`

#### Style and Code Analysis
- Check whether VS Code reports problems in the **Problems** window
- Fix all of them, and make another commit with meaningful commit message

The development cycle for the first function is completed. 

#### Incremental development
- At the completion of each development step, commit your changes:
  - Step 1: document all the modules
  - Step 2: test the 1st function
  - Step 3: design the 1st function
  - Step 4: implementat the 1st function
  - Step 5: verify if there are Problems reported by VS Codea and fix them. 
  - Step 6: test the 2nd function
  - Step 7: design the 2nd function
  - Step 8: implement the 2nd function
  - Step 9: verify if there are Problems reported by VS Codea and fix them. 

There is a minimum of 7 commits that evidence your incremental development 
process (Steps 5 and 9 might not be necessary if all problems were fixed at previous steps). 

When the lab is completed, 
- Push the local repo to the remote location with the command `git push origin main`
  - Do NOT push after every single commit
  - It's sufficient to push when done with all the commits locally.

### Collaboration
Collaboration is allowed. It means you are allowed to:
- Ask questions of your collaborator, CAs, and instructor
- Answer questions and give advice 
- Discuss and clarify concepts 
- Show or practice concepts on simple examples. 

You are NOT allowed to:
- Give your work on this lab or do it for someone else
- Ask and/or get designs and code for this lab from someone else or something else  (e.g., Copilot) WITHOUT clearly documenting:
  - What the source is
  - What your "ask" of the source was.

### Evaluation
- Documentation: 10 pts
- Testing: 20 pts (5 pts for each testing function)
- Design: 30 pts (15 pts for each core function)
- Implementation: 20 pts (10 pts for each core function)
- Incremental development: 20 pts (~3 pts for each commit)
  - Commit message must be meaningful (1 pt/commit)
  - The order of commits is followed (2 pts/commit)
  - A commit tracks changes that correspond to the following workflow: test first, design, implement based on the design.
- Style and code analysis: priceless!

### Submission
#### GitHub
- Has your remote repo

#### Canvas
- Convert DESIGN.md to Word or PDF using VS Code MD->PDF converter
- Upload converted file to Canvas submission link.

