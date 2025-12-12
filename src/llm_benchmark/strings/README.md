# Strings Module

This module contains string manipulation operations for benchmarking purposes.

## Modules

### StrOps (`strops.py`)

String operations implemented using explicit loops.

#### Methods

- **`str_reverse(s: str) -> str`**
  - Reverse a string
  - Args: `s` - String to reverse
  - Returns: Reversed string
  - Example:
    ```python
    from llm_benchmark.strings.strops import StrOps
    StrOps.str_reverse("hello")  # Returns: "olleh"
    StrOps.str_reverse("Python")  # Returns: "nohtyP"
    ```

- **`palindrome(s: str) -> bool`**
  - Check if a string is a palindrome
  - A palindrome reads the same forwards and backwards
  - Args: `s` - String to check
  - Returns: `True` if the string is a palindrome, `False` otherwise
  - Example:
    ```python
    StrOps.palindrome("racecar")  # Returns: True
    StrOps.palindrome("hello")    # Returns: False
    StrOps.palindrome("madam")    # Returns: True
    StrOps.palindrome("A")        # Returns: True
    ```

## Usage Example

```python
from llm_benchmark.strings.strops import StrOps

# String reversal
text = "Hello, World!"
reversed_text = StrOps.str_reverse(text)
print(reversed_text)  # "!dlroW ,olleH"

# Palindrome checking
words = ["racecar", "hello", "madam", "python", "noon"]
for word in words:
    is_palindrome = StrOps.palindrome(word)
    print(f"{word}: {is_palindrome}")

# Output:
# racecar: True
# hello: False
# madam: True
# python: False
# noon: True
```

## Performance Notes

- Both methods use explicit character-by-character loops
- No built-in string reversal functions are used
- Designed to benchmark LLM code generation for string manipulation
- The palindrome check has O(n) time complexity where n is the string length
- Case-sensitive comparison (e.g., "Racecar" would return False)
