def findMaxRec(A, n):
    if (n == 1):
        return A[0]
    return max(A[n - 1], findMaxRec(A, n - 1))
 
# Driver Code

A = [1, 4, 45, 6, -50, 10, 2]
n = len(A)
print(findMaxRec(A, n))

'''The `if __name__ == "__main__":` block is used in Python to determine whether a script is being run as 
the main program or if it's being imported as a module into another script. Let's discuss what happens 
if you don't use it and why you should use it:

1. **If you don't use `if __name__ == "__main__":`**:

   When you don't use this block, any code you have at the top level of your script will be executed as soon as the script is imported as a module by another script. This can lead to unintended consequences if you have code that you only want to run when the script is executed directly, not when it's imported as a module.

   For example, if you have code like this at the top level of your script:

   ```python
   A = [1, 4, 45, 6, -50, 10, 2]
   n = len(A)
   print(findMaxRec(A, n))
   ```

   If another script imports this script, it will execute these lines immediately, which may not be what you want. It's generally a best practice to avoid executing code upon import unless it's intended to be a part of the module's functionality.

2. **Why you should use `if __name__ == "__main__":`**:

   By using this block, you ensure that the code inside it is only executed when the script is run directly, not when it's imported as a module. This allows you to create reusable modules and scripts that can be used in various contexts without unexpected side effects.

   In the context of your code snippet, if you don't use `if __name__ == "__main__":`, the code that calculates the maximum value and prints it will run as soon as the script is imported, which might not be desirable if you want to use the `findMaxRec` function in other scripts without immediately printing the result.

In summary, using `if __name__ == "__main__":` is a good practice to ensure that the code inside the block only runs when the script is executed directly and not when it's imported as a module, making your code more modular and reusable.'''