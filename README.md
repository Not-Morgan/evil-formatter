# evil formatter

it formats your code by placing all curly braces and semicolons in a column to the right of the longest line.

usage:
```
python formatter.py filename
```

### examples of formatted code

before:
```
#include <iostream>

int main() {
    if (true)
    {
        std::cout << "Hello, World!" << std::endl;
    }
    return 0;
}
```

after:
```
#include <iostream>

int main()                                         {
    if (true)                                      {
        std::cout << "Hello, World!" << std::endl  ;}
    return 0                                       ;}
```
