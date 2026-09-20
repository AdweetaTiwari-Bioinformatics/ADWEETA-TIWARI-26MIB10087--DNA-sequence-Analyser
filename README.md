# ADWEETA-TIWARI-26MIB10087--DNA-sequence-Analyser
#DNA sequence Analyser
## 1. About The Project
A Python based Bioinformatics tool Used to analyze DNA sequences of two DNA strands, which includes nucleotide composition and GC content, further it analyzes whether the two strands are complementary or not
The program essentially accepts two DNA strands as the user inputs them.
The program further more it performs a detailed analysis on each strand. It calculates the length of the sequence, nucleotide count, nucleotide percentage, GC and AT content in percentage
The program also generates the complementary sequence of the first DNA strand and compares it with the second DNA strand to determine whether the two strands are complementary

## 2. Features
The program provides the following features. 
Accepts two DNA sequence from the user starting with one strand at a time 
starting from input of strand1.
converts the inputs into uppercase
calculates the length of the strand 
counts the number of the A , T , G , C nucleotides
calculates the percentage of the nucleotides individually 
then calculates the GC content
calculates the AT content
Repeats the same analysis for strand 2
Generates the complementary strand of the first DNA strand 
Compares the complementary strand with the second input strand
Displays whether the two strands are complementary or not

## 3. Technologies Used
-Python 3 
-No external Python libraries are required

## 4. Requirements
-python 3.x
-command prompt / terminal 
## 5. Environment Setup and  Dependencies 
### Step 1: Install Python

Install Python 3.x on the system.

After installation, verify that Python is available from the command line by
running:

   python --version

A Python version number should be displayed.

### Step 2: Obtain the Project

Download or clone this GitHub repository to the computer.

### Step 3: Open the Project Directory

Open Command Prompt or Terminal and navigate to the directory containing the
Python program.

### Dependencies 

This project does not require any external Python packages 
All operations are performed using python's built in functionality
Therefore, no additional `pip install` commands are required.

## 6. Running the Program
After navigating to the project directory , run:

python dna_sequence_analyser_adweeta26mib10087,py

The program will Start and ask the user to enter the first DNA strand.

The user must then enter the second DNA strand when prompted.

## 7. Input Format

The DNA sequence should contain the standard DNA nucleotide bases:
#### A - Adenine
#### T - Thymine
#### G - Guanine
#### C - Cytosine 
for example : Enter first DNA Strand : ATGC

## 8. Analysis Performed 
For each DNA strand , the program calculates:

### sequence length
The total number of the nucleotide present in the sequence

### GC Content 
The combined Percentage of guanine and cytosine:

GC Content = ((G count + C count) / sequence length) * 100

### AT Content

The combined percentage of Adenine and Thymine:

AT Content = ((A Count + T count) / sequence length) * 100

## 9. Complementary Strand Analysis
The program generates the complementary sequence of the first DNA Strand using the standard DNA base pair relationship:
##### A - T
##### T - A
##### G - C
##### C - G

The generated complementary sequence is then compared with the second input strand 

If the second strand matches the complement of the first sequence , the program reports the two strands complementary or else invalid 

## 10. Example 
### Input

Enter first DNA strand: ATGC

Enter second DNA strand: TACG

### Output
 Strand 1: ATGC
  
 Strand 2: TACG
  
Complement of Strand 1: TACG
  
Result: The two strands are complementary.

The program also displays the nucleotide counts, nucleotide percentages,
GC content and AT content for each strand.

## 11. Execution Summary

To run the project:

1. Install Python 3.x.
    2. Download or clone the repository.
    3. Open Command Prompt or Terminal.
    4. Navigate to the project directory.
    5. Run the Python file.
    6. Enter the first DNA strand.
    7. Enter the second DNA strand.
    8. View the sequence analysis and compatibility result.

## 12. Author

Adweeta Tiwari
26MIB 10087
VIT BHOPAL UNIVERSITY
