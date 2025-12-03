# 13. Roman to Integer: Thought Process

### Strategy: Reverse Iteration & Rule Matching

**1. Create Mapping**
Define a dictionary (`r_dict`) to map every single Roman character to its integer value (e.g., `'I': 1`, `'V': 5`, etc.).

**2. Iterate Backwards**
Process the input string `s` in **reverse order** (`s[::-1]`).
* *Why?* Roman numerals are usually written largest to smallest. The exceptions (subtraction cases like "IV") happen when a smaller value appears before a larger one. By going backwards (right to left), we process the "larger" value first, making the decision to add or subtract the "smaller" value easier.

**3. Track Previous Character**
Use a variable `lst_char` (last character) to remember the Roman numeral we just processed in the previous iteration.

**4. Apply Logic (Add or Subtract)**
For each character `char` in the reversed string:

* **First Iteration:** If `lst_char` is `None` (start of the loop), simply **add** the value of `char` to the result.
* **Subsequent Iterations:** Compare `char` with `lst_char` to detect subtraction cases explicitly:
    * If `char` is `'I'` and `lst_char` is `'V'` or `'X'` -> **Subtract** value.
    * If `char` is `'X'` and `lst_char` is `'L'` or `'C'` -> **Subtract** value.
    * If `char` is `'C'` and `lst_char` is `'D'` or `'M'` -> **Subtract** value.
    * **Else:** If none of these specific pairs match, simply **add** the value.

**5. Update Tracker**
Update `lst_char` to be the current `char` so it can be used for comparison in the next iteration.