# 14. Longest Common Prefix: Thought Process

### Strategy: Horizontal Scanning

**1. Initialize Candidate**
Take the **first string** (`strs[0]`) from the list and assume it is the `check_word` (the prefix).

**2. Iterate Through List**
Loop through the rest of the strings in the list one by one.

**3. Compare and Reduce**
Since the strings may be different lengths, we start by comparing the full `check_word`.
* **While** the current string does not start with `check_word`:
    * Shorten (slice) the `check_word` from the end by one character.
    * *Optimization:* If `check_word` becomes empty during this process, return `""` immediately.

**4. Final Result**
After checking all words, return the surviving `check_word`.

***

### Example Trace (`["flower", "flow", "flight"]`)

* **Start:** `check_word` = "flower"
* **Compare with "flow":**
    * Does "flow" start with "flower"? **No.**
    * Shorten `check_word` -> "flowe" -> "flow".
    * Does "flow" start with "flow"? **Yes.**
* **Compare with "flight":**
    * Does "flight" start with "flow"? **No.**
    * Shorten `check_word` -> "flo" -> "fl".
    * Does "flight" start with "fl"? **Yes.**
* **End:** Return `"fl"`.