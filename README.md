## Using
```
$ ./expression2words.py
Enter expression: 4 + 3 + 1 = 2 + 3
Result: four PLUS three PLUS one EQUALS two PLUS three
```
Equal sign is optional.
```
$ ./expression2words.py
Enter expression: 1 +  4   - 1
Result: one PLUS four MINUS one
```
The number of spaces between characters does not matter:
```
$ ./expression2words.py
Enter expression: 4 +3 +1=1 +   3
Result: four PLUS three PLUS one EQUALS two PLUS three
```

You can use the `-l` key to check expression logic, but the equal sign is now required:
```
$ ./expression2words.py -l
Enter expression: 1 + 2 + 4 = 1
invalid input
```
```
$ ./expression2words.py -l
Enter expression: 1 + 2 +4 = 7     
Result: one PLUS two PLUS four EQUALS seven
```
