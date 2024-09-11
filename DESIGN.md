## Design of div_nums() core function 
    ### Ask: Return a list whose values are from `num_list`, divided by `term`, and
    converted to integers. ###
    Here `num_list` and `term` are the parameters to the `div_nums()` function

    ### Accumulator: ### `new_list`
    ### Loop variable: ### `num`
    ### Iterable: ### `num_list`
    ### At each iteration: ### a list value retrieved in `num` is divided with the `term` and quotient is added to the `new_list`
    ### Returns: ### `new_list` containing results from above operation.

    ### Approach ###
    - Create a `new_list` variable.
    - For every number `num` in the `num_list`:
       1. divide the number with the `term` using floor division (//)
       2. append the value to the `new_list` variable
    - At the end of the loop, `new_list` variable contains the integer values of `num_list` values divided by the `term`
    - Return the `new_list`

    ** NOTE: **Floor division (//) gives the quotient rounded off to the smallest integer.

    ### Version Control Steps: ### Run these commands in the git bash terminal window of VSCode.
    - git status
    - git add .
    - git status
    - git commit -m 'design div_nums()`
    - git status

## Design of last_chars() core function
