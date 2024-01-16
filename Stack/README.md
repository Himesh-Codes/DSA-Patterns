# Stack

LIFO based data structure.

# Here are some common use cases of stacks in Data Structures and Algorithms (DSA):

1. If recursion is banned then use Stack instead.

2. Undo/Redo Operations:

Reversing Actions: Stacks provide the underlying mechanism for implementing undo/redo functionality in software applications. Each action is pushed onto a stack, and undoing involves popping actions off the stack and reversing their effects.

3. Expression Evaluation and Syntax Parsing:

Infix to Postfix/Prefix Conversion: Stacks are used to convert infix expressions (e.g., A + B \* C) to postfix (e.g., ABC+) or prefix (e.g., +AB) notation, which are often easier for computers to evaluate.

Balancing Parentheses: Stacks are used to verify proper matching of parentheses, brackets, and braces in expressions and code, ensuring syntactic correctness.

4. Backtracking Algorithms:

Exploring Possible Solutions: Stacks are essential for implementing backtracking algorithms, which involve exploring multiple solution paths and backtracking when a path doesn't lead to a solution. They store intermediate states and choices to efficiently backtrack when needed.

5. Depth-First Search (DFS):

Graph Traversal: Stacks are used to implement DFS, a graph traversal algorithm that explores a graph in depth-first order. It involves pushing vertices onto a stack to visit their neighbors recursively.

6. Tree Traversal:

Preorder, Inorder, Postorder: Stacks can be used to implement different tree traversal orders, such as preorder, inorder, and postorder, each visiting nodes in a specific sequence based on their relationships.

7. Memory Management:

Function Calls and Local Variables: Stacks are used to manage memory for function calls and local variables in low-level programming languages. They allocate and deallocate memory as functions are called and returned.

8. Browser History and Navigation:

Back and Forward Buttons: Web browsers use stacks to implement the back and forward buttons, storing visited web pages in a stack-like structure to allow for navigation history.

9. Calculator Operations:

Evaluating Expressions: Calculators use stacks to evaluate expressions entered by the user, storing operands and operators in the correct order for computation.

10. String Reversal:

Reversing Order of Characters: Stacks can be used to reverse the order of characters in a string, pushing each character onto a stack and then popping them in reverse order to form the reversed string.

11. Function Calls:

Storing Call History: Stacks are crucial for managing function calls in programming languages. They store local variables, return addresses, and other information for each active function call, enabling proper execution and return to the correct point in the code after a function completes.

12. Balancing Parentheses:

Checking for balanced parentheses, brackets, or braces in an expression is a classic use case for a stack. As you encounter opening and closing symbols, you can use a stack to ensure that they are matched correctly.

13. Next Greater Element:

Finding the next greater (or smaller) element in an array for each element is a common problem where a stack can be utilized. It helps in maintaining a decreasing order (or increasing order) of elements in the stack as you traverse the array.

14. Histogram Area:

Calculating the maximum area under a histogram involves finding the nearest smaller elements for each bar. A stack can be used to efficiently determine the boundaries of each rectangle.

15. Monotonic Stack:

In some problems, maintaining a monotonic stack (either increasing or decreasing) can simplify the solution. This is particularly useful for finding the nearest greater or smaller element in an array.

In summary, the stack data structure is versatile and finds application in various scenarios in competitive programming. Its Last-In-First-Out (LIFO) property makes it suitable for handling situations where elements need to be processed in a specific order, such as reversing or tracking nested structures.
