# Creating a Programming Language Assignment
SBL, a programming language created using Python3 and the SLY library.

This was done as an assignment for CSE 307: Principles of Programming Languages at Stony Brook University.

DISCLAIMER: There are a few grammar bugs causing shift/reduce and reduce/reduce errors, causing some programs to not function properly.

## Methods
Using the SLY library, I was able to create a lexer that would tokenize the input file and a parser that would parse the tokens and act according to their structure.

In the lexer, sbllexer.py, I used regex to match parts of a string and turn them into tokens to be used by the parser. For tokens that use similar characters, I had to make sure that the longer and more specific regex matches before the shorter and more broad regex. This was done by simply ordering the more specific one above the more broad one.

In the parser, sblparser.py, I took the tokens generated from the lexer and parsed them to activate a function when a specific set of tokens was found. These functions would then create an AST, which I would evaluate later. Precedence is very important, so when creating the grammar, the operations with the highest precedence would be at the bottom of the grammar and the operations with the lowest precedence would be at the top of the grammar.

sbl.py is used to take input from the user and put it into the lexer and parser.

## Usage
'python sbl.py [filename]'

## Supported Features

### Datatypes
Numbers: Integers and Reals ('10, 4.3, -.34, 23., -1.23e4')

Booleans: ('True, False')

Strings: ('\"Hello\", \'12345\', \"54 cows\"')

Lists: ('[1, 2, 3, 4], ["pie", "pasta"], ["tomato", 34.75]')

Tuples: ('(1, 2, 3, 4), ("pie", "pasta"), ("tomato", 34.75)')

### Operators

'( expression )' - A parenthesized expression

'( expression1, expression2, ... )' - Tuple creation

'#i(tuple)' - Tuple indexing (index starts at 1)

'a[b]' - Indexing

'a ** b' - Exponentiation

'a * b' - Multiplication

'a / b' - Division

'a div b' - Integer division

'a mod b' - Modulus

'a + b' - Addition

'a - b' - Subtraction

'a in b' - Membership

'a::b' - Append a to start of b

'not a' - Not

'a andalso b' - And

'a orelse b' - Or

'a < b' - Less than

'a <= b' - Less than or equal to

'a == b' - Is equal

'a <> b' - Is not equal

'a >= b' - Greater than or equal to

'a > b' - Greater than

### Blocks
A block is defined by an open curly bracket, the contents, and a closing curly bracket. The body of the code must be contained within a block, and only specific definitions can use a block.

```
{
    print("Hello World");
}
```

### Functions and Function Calls
A function is defined by the keyword fun, followed by the name of the function, a left parenthesis, the parameters separated by commas, a right parenthesis, an equal sign, a block statement, and then a return expression.

A function call is defined by the function name, a left parenthesis, the arguments, and a right parenthesis.

```
fun addOne(n) =
{
    output = n + 1;
} output;
{
    print(addOne(1));
}
```

### Print
Print is defined by the keyword print, a left parenthesis, the expression to print, a right parenthesis, and a semicolon.

```
{
    print("Hello World");
}
```

### Assignment
Assign is defined by a variable, an equals sign, an expression, and a semicolon.

```
{
    x = 1 + 2;
}
```

### If Statements
If is defined by the keyword if, a left parenthesis, an expression, a right parenthesis, and a block statement.

```
{
    x = 1;
    if(x == 1){
        print("Hello World");
    }
}
```

### If-else Statements
If-else is defined by the keyword if, a left parenthesis, an expression, a right parenthesis, a block statement, else, and another block statement.

```
{
    x = 1;
    if(x == 1){
        print("Hello World");
    }
    else {
        print("dlroW olleH);
    }
}
```

### While Loops
While is defined by the keyword while, a left parenthesis, an expression, a right parenthesis, and a block statement.

```
{
    x = 1;
    while(x >= 0){
        print("Hello World");
        x = x - 1;
    }
}
```

