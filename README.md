
# Frequency Analysis of Words  
  
This script could be helpful to you to find the most frequent words in a text file.

## Usage from code
```python
>>> from lang_frequency import get_most_frequent_words
>>> get_most_frequent_words('Your long text string ...', top=5)
[('the', 71755), ('of', 39634), ('and', 36549), ('to', 27965), ('a', 19811)]
```

## Usage from bash
```bash
$ python3 lang_frequency.py -f path/to/big_text_file.txt
Top 10 most common words in the file:

Word       | Occurrences
-----------------------
the        |      71755
of         |      39634
and        |      36549
to         |      27965
a          |      19811
in         |      19691
that       |      11437
was        |      11238
he         |       9599
his        |       9575

```
  
# Project Goals  
  
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)