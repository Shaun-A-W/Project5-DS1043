
# A Library of One's Own

### DS-1043 - Project 5

### Shaun W. - 9 Dec. 2024

#

## Prime Factorization -- 'p_factor()'

This function provides a prime factorization list for the inputted integer in the form of: `p_factor(int) -> list[int]`. An error will be raised if the inputted integer is less than one. Additionally, if the inputted integer is already a prime number, the result will be as follows: `p_factor(some_prime) -> [1,some_prime]`. To distinguish between prime and non-prime numbers, a secondary function--is_prime()--was implemented. This function returns Boolean values. If it receives a value < 2, then it returns False. With a keen eye, one may recognize that p_factor(1) may produce a problem. Though, it will return an empty list ( [] ) as '1' does not have a prime factorization. The overall result is achieved by consistent use of is_prime() along with division of the current value such that value a mod prime factor b = 0. Once this is no longer the case, it moves up to the next prime number and repeats this process until the value of the number is 1.

The time complexity of this pair of functions is at best O(n/2), on average around O(n), and at the worst case it approaches O(n^2), sitting around O(n^2/2). In this case, 'n' represents the value chosen to create a prime factorization for. Entirely, this process is possible as all positive integers > 1 as the "Fundamental Theorem of Arithmetic" states. Possible use cases of both p_factor() and is_prime() can be involved in arithmetic with Least Common Multiples and Greatest Common Denominators. Additionally, cryptography makes consistent use of prime numbers for security purposes, making this a relevant tool in the field.

## Flatten Lists -- 'no_nest()'

The no_nest() function flattens list. This means that it returns a single list containing all elements it previously did, but without any nesting involved. One important note is that it will accept other primitive types (i.e. str, int, float, list), but not dictionaries. It is a simple function for the most part, and it has an input/output that appears like this: `no_nest([1,'three',4,[2,6],['one','two']]) -> [1,'three','4',2,6,'one','two']`. As shown, it maintains both the order and elements themselves while removing any nested structuring. 

The time complexity of this function will always be O(n), where n is the size of the list inputted, including all nested elements. While this function has somewhat of a niche use case, though that does not remove its usefulness. It may be particularly useful when trying to output data into a tabular file, like CSV. It will improve performance when writing to the file and be cleaner overall to deal with. On the other hand, you would not want to use this function in cases where the nested structures are important and the data is not viable when completely flattened. Be aware of what structures are necessary for every use of data.

## Table Constructor -- 'view_table()'

This function, and its associated create_table() and max_width() functions, make up many lines of code. However, this does not necessarily mean it is a complex function. Simply put, calling view_table() with its necessary header = list[str] and data = list[list|dict] will output a table to the console. This table is similar to Markdown tables in that it uses dashes and bars to structure itself. An example of calling view_table() is given below:


	input:
		
		data = [{'a': 233, 'two': 'c', 'd': False, 'four': 12222222222222},
              {'one': 12.399, 'two': '3', 'three': True, 'four': False}]
              
    	header = ['a', 'two', 'three', 'four', ]
    
    output:
    
    	| a    | two | three | four     |
		|------|-----|-------|----------|
		|  233 | c   |       | 1.22e+13 |
		|      | 3   | True  | False    |


Take note that the data includes values for keys like 'd' that are not shown in the table. This is because the header does not include 'd' as a column header, so the entry associated with that row and column does not exist. The same goes for the second row under column 'a'. As far as time complexity goes, it can be somewhat estimated by O(a*b), where 'a' is the number of items in total across all data lists/dicts and 'b' is the length of the header. This group of functions and the creation of a table can be useful for many scenarios in this case as it handles all 4 main types of single pieces of data. An obvious use case is the implementation of the table into a Markdown file due to the formatting.

## Text Word Count -- 'file_wordcount()'

file_wordcount() exists to return the word count of a given text file, such as `.md` or `.txt`. It is a simple function for a simple task. First, the file is opened via a 
`with` statement and is read. The text is extracted and cleaned to maximize accuracy in the final result. It utilizes UTF-8 encoding and simply returns an integer once completed. Word counts are somewhat subjective based on the standard or method to count being used. This particular function uses list comprehension with an overall fairly clean item composition for valid words. Then it takes the length of this list as its return value. 

As for complexity, this function runs in roughly O(n) time for all cases. It is useful in the same ways other word counts are useful and may be implemented in future projects for the purpose of file management. 

## Word Frequency -- 'file_search()'

Similar to the previous function, file_search() utilizes file I/O and cleaning methods to produce a list with high accuracy to the original document using pieces as list items. Instead of overall word count, though, this function returns a dictionary containing the frequency of words, which come from the query inputted. The arguments for this function look like this: 

 		def file_search(filename: str, query: list[str], case_sensitive: bool) -> dict[str, int]:

The program will search through the cleaned text and look for matches within `query`, adding dictionary keys and values when encountered or increasing the value if it already exists. Additionally, the function contains a `case_sensitive` argument where it can be turned on/off through True/False. When off, the matching will utilize the string method `str.casefold()` as a way to ignore the case of the query and text entries. 

Overall, the function runs at about O(n) time complexity where n will be the word count of the text file. Potential use cases for this include gauging the complexity of a document based on vocabulary or potentially summarizing key ideas in the text through TF-IDF algorithms as previously implemented.