### Jose-Antonio Rubio
### CS 325-400
### Homework 5

# Premise
Suppose there are two types of professional wrestlers: “Babyfaces” (“good guys”) and “Heels” (“bad guys”). Between any pair of professional wrestlers, there may or may not be a rivalry. Suppose we have n wrestlers and we have a list of r pairs of rivalries.

# How to Run
wrestler.py works using Python 2.7.10
It requires a file with formatting like the wrestler.txt, wrestler1.txt, ... wrestler5.txt which are supplied
It will build a graph of wrestlers and rivalries and determines whether it is possible to designate some of the wrestlers as Babyfaces and the remainder as Heels such that each rivalry is between a Babyface and a Heel.  If it is possible it will console out to the terminal along with the names of the babyfaces and the heels.  If it is not possible it will console to the terminal as such

To run wrestler.py run the following command in your command line
```
python wrestler.py {text_file_name.extension}
```
Example
```
python wrestler.py wrestler4.py
```