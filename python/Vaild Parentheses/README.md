# 20. Valid Parentheses: Thought Process

### Strategy: Stack (LIFO) & Dictionary Mapping

**1. Define Relationships**
Create a hash map (dictionary) `check_dict` to define valid pairs.
* **Key:** Closing bracket (e.g., `')'`, `'}'`).
* **Value:** Corresponding opening bracket (e.g., `'('`, `'{'`).
* *Why?* This allows O(1) lookups to see if a character is a closing bracket and what its "partner" should be.

**2. Initialize Stack**
Create an empty list `placeholder` to act as a **Stack** (Last-In, First-Out).
* *Concept:* The most recently opened bracket must be the first one to be closed.

**3. Iterate Through String**
Loop through every character `b` in the string `s`.

**4. Check Character Type**
* **Opening Bracket:** If `b` is *not* a key in our dictionary (meaning it is `(`, `{`, or `[`), push it onto the stack. We are waiting for its partner.
* **Closing Bracket:** If `b` *is* a key in the dictionary:
    * **Check Match:** Verify two conditions:
        1.  The stack is not empty (`placeholder` exists).
        2.  The top item on the stack (`pop()`) matches the required opening bracket (`check_dict[b]`).
    * **Failure:** If the stack is empty OR the top item doesn't match, return `False` immediately.

**5. Final Validation**
After the loop finishes, check if the stack is empty.
* **Empty:** All brackets were matched and closed. Return `True`.
* **Not Empty:** Some opening brackets were left unclosed. Return `False`.