# 21. Merge Two Sorted Lists: Thought Process

### Strategy: Two Pointers with Dummy Head

**1. Handle Edge Cases**
First, check if either input list is empty.
* If `list1` is empty, return `list2` immediately.
* If `list2` is empty, return `list1` immediately.
* *Why?* There is no need to merge if one side is missing; the answer is just the other list.

**2. Initialize Dummy Node**
Create a `rslt` (dummy) node with value `0`.
* Keep a reference `check_point` pointing to this dummy head.
* *Why?* This simplifies the logic. We can always blindly attach nodes to `rslt.next` without worrying if the result list is currently empty.

**3. Iterate with Two Pointers**
Use a `while` loop that continues as long as **either** `i1` or `i2` has nodes left (`while i1 or i2`).

**4. Compare and Attach**
In every iteration, compare the current values of `i1` and `i2`:
* **One side empty?** If `i1` is `None`, take from `i2` (and vice versa).
* **Comparison:** If both exist, compare `i1.val` and `i2.val`.
    * If `i1.val <= i2.val`: Create a new node with `i1`'s value and attach it. Move pointer `i1` forward.
    * If `i2.val < i1.val`: Create a new node with `i2`'s value and attach it. Move pointer `i2` forward.

**5. Advance Result Pointer**
After attaching a node, move the `rslt` pointer forward (`rslt = rslt.next`) to be ready for the next attachment.

**6. Return Result**
Return `check_point.next`.
* *Why?* `check_point` is the dummy head (0). The actual merged list starts at the *next* node.

### Better solution

**1. Initialize Dummy Node**
Start by creating a dummy head node (`head`) and a pointer `cur` to track the current position in the new list.
* *Why?* This simplifies edge cases (like inserting the first element) so we don't need extra `if` checks for the head of the return list.

**2. Handle Edge Cases**
Check if either input list is initially empty.
* If `list1` is empty, return `list2`.
* If `list2` is empty, return `list1`.

**3. Main Loop (Compare & Copy)**
Loop **while both `list1` and `list2` are not None**.
* Compare the current values:
    * If `list1.val <= list2.val`: Create a **new node** with `list1`'s value. Attach it to `cur.next`. Move `list1` forward.
    * Else: Create a **new node** with `list2`'s value. Attach it to `cur.next`. Move `list2` forward.
* Move `cur` forward to the newly created node.

**4. Process Leftovers**
After the main loop, one list might still have items. Determine which one is left (`extra_list`).
* **Loop through the remaining items:** Iterate through `extra_list`, creating a **new node** for each value and attaching it to `cur.next`.
* *Note:* This approach creates a completely new independent list rather than linking to the existing nodes.

**5. Return Result**
Return `head.next` (skipping the dummy node to return the real start of the merged list).