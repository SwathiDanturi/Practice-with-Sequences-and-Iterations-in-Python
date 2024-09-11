## Design of div_nums() core function 

### Ask:###
Return a list whose values are from `num_list`, divided by `term`, and converted to integers.
Here `num_list`, list of integers and `term`, integer are the parameters to the `div_nums()` function

**New Variable:** `new_list` and is expected to hold list of integers
**Accumulator:** `index`, intialized to 0 and is incremented in every iteration which is used as an index to add values to the new variable created.
**Loop variable:** `num` and the data type is integer
**Iterable:** `num_list`, the list of integers
**At each iteration:** The list value retrieved in `num` is divided with the `term` and the quotient is added to the `new_list` using the `index`.
**Returns:**`new_list` containing results from above operation.

### Approach ###
- Create a new list variable `new_list`.
- A new `index` field intialized to 0
- For every number `num` in the `num_list`:
    1. divide the number with the `term` using floor division (//)
    2. assign the value to the `new_list` variable at the index `index`
    3. `index` is incremented by 1
- At the end of the loop, `new_list` variable contains the integer values of `num_list` values divided by the `term`.
- Return the `new_list`.

**NOTE:**Floor division (//) gives the quotient rounded off to the smallest integer.

### Version Control Steps: ### Run these commands in the git bash terminal window of VSCode.
- git status
- git add .
- git status
- git commit -m 'design div_nums()`
- git status



## Design of last_chars() core function
### Ask:###
Return a list of characters that represent the last chararcter of each word in `word_list`
Here `word_list`, list of strings is the parameter to the `last_chars()` function

**New Variable:** `new_word_list` and is expected to hold list of strings
**Accumulator:** `index`, intialized to 0 and is incremented in every iteration which is used as an index to add values to the new variable created.
**Loop variable:** `each_word` and the data type is string
**Iterable:** `word_list`, the list of strings
**At each iteration:** The list value retrieved in `each_word` and the last character of the word is added to the `new_word_list` at index `index` using reverse indexing of `each_word`.
**Returns:**`new_word_list` containing results from above operation.

### Approach ###
- Create a new list variable `new_word_list`.
- A new `index` field intialized to 0
- For every string `each_word` in the `word_list`:
    1. get the last character of `each_word` using reverse indexing i.e, -1
    2. assign the value to the `new_word_list` variable at index `index`
    3. `index` is incremented by 1
- At the end of the loop, `new_word_list` variable contains the last characters of `word_list` strings.
- Return the `new_word_list`.

### Version Control Steps: ### Run these commands in the git bash terminal window of VSCode.
- git status
- git add .
- git status
- git commit -m 'design last_chars()`
- git status