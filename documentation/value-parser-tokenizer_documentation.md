# Parser for Value instances and numeric tokenizer

In this document, the LL1 parser and the numeric tokenizer used to detect Value instances is described.
Apart from some different names, it should be very similar to the final implementation.



## Terminals (=tokens)

- [SNARGF] = FUNCT | SYSOP | MULTIMEDIA
- [STRING] = IDENTIFIER | GARBAGE
- [NOARGF] = NOP | UNSET
- [ACTID] = [INTEGER] | IDENTIFIER
- [KNAME] = [INTEGER] | IDENTIFIER | TRUE | FALSE
- [NUMERIC] = [INTEGER] | FLOAT
- [INTEGER] = BINARY\_INTEGER | OCTAL\_INTEGER | DECIMAL\_INTEGER | HEXADECIMAL\_INTEGER
- TRUE
- FALSE
- RECT
- PRESS
- EXEC
- MOUSE
- KEYS
- (
- )
- +
- ,
- $


Please note that:

- Whitespace is read by the parser, but is discarded;
- "$" is a token indicating the end of input (EOI);
- BINARY\_INTEGER, OCTAL\_INTEGER, DECIMAL\_INTEGER and HEXADECIMAL\_INTEGER are all the types of recognized integers (see section "Numeric tokenizer");



## Non-terminals (=productions)


- 0: \<S\> &rarr; [NOARGF] \<A\> $
- 1: \<A\> &rarr; ( )
- 2: \<A\> &rarr; &epsilon;
- 3: \<S\> &rarr; [SNARGF] ( [ACTID] ) $
- 4: \<S\> &rarr; EXEC ( [STRING] ) $
- 5: \<S\> &rarr; MOUSE ( [ACTID] \<B\> $
- 6: \<B\> &rarr; + [ACTID] \<B\> $
- 7: \<B\> &rarr; ) $
- 8: \<S\> &rarr; KEYS ( [KNAME] \<C\> $
- 9: \<C\> &rarr; + [KNAME] \<C\>
- 10: \<C\> &rarr; )
- 11: \<S\> &rarr; TRUE $
- 12: \<S\> &rarr; FALSE $
- 13: \<S\> &rarr; [INTEGER] $
- 14: \<S\> &rarr; RECT ( [INTEGER], [INTEGER], [INTEGER], [INTEGER] ) $
- 15: \<S\> &rarr; PRESS ( [NUMERIC], [NUMERIC], [NUMERIC], [NUMERIC] ) $
- 16: \<S\> &rarr; [STRING] $
- 17: \<S\> &rarr; &epsilon;
- 18: \<C\> &rarr; , [IDENTIFIER] \<C\>
- 19: \<S\> &rarr; FLOAT $



Please note that "&epsilon;" means that the production produces the empty string (string with no characters, usually denoted as "" in languages);





## Nullable, First, Follow table

This table is needed in order to create the productions table below, a small reminder of what this is all about...

- Nullable: Tells whether a NT (Non-terminal) can "become" the empty string. If a production is of the form "NT &rarr; &epsilon;" or "NT &rarr; NT2" and "NT2 &rarr; &epsilon;" exists, then yes, it is nullable, otherwise, it's not;
- First: A set containing the first tokens encountered by a NT, considering all the productions in which the NT is on the lhs (left hand-side), that is, before \"&rarr;\";
- Follow: A set used only in case of NT being nullable. It contains the tokens that follow NT, when NT appears in any production (not the ones in which NT is on the lhs);

Here's the table:

 NT | NULLABLE | FIRST | FOLLOW
:--:|:--------:|:-----:|:-------:
\<S\> | Yes | \[NOARGF\] \[SNARGF\] EXEC MOUSE KEYS TRUE FALSE [INTEGER] RECT PRESS [STRING] FLOAT | $
\<A\> | Yes | (   | $
\<B\> |  No | + ) |
\<C\> |  No | + ) |


To understand, the \<S\> and \<A\> NTs will be taken as examples, the rest is no-brainer once the logic is understood.

- \<S\> is nullable, as the production "\<S\> &rarr; &epsilon;" exists;

- Considering all productions with \<S\> as lhs (0, 3, 4, 5, 8, 11, 12, 13, 14, 15, 16, 17 and 19), the "first tokens" are the ones reported in the table;

- Being nullable, we must determine the "Follow" set... being \<S\> the "starting point", the only possible token is end of input ("\$"), as if the starting point is empty, then there are no tokens to process and thus EOI is reached. Please note that this way, the empty string ("") is recognized as part of the grammar;

- \<A\> is nullable, as the production "\<A\> &rarr; &epsilon;" exists;

- Considering all productions with \<A\> as lhs (1 and 2), the only "first token" is "(";

- As for the "Follow" set, in this case, \<A\> is NOT a starting point, but the production "\<S\> &rarr; [NOARGF] \<A\> \$" exists, and whatever \<A\>'s transformation is, it will always be followed by \"\$\", so, the "Follow" set will only contain \"\$\";

The others are more straightforward as they aren't nullable, so only the "First" set must be determined.



## LL1 table

This table is the one used by the parsing algorithm, in order to properly detect the correct sentences of this small language.

LL1 stands for "Left-to-right" "Leftmost derivation" "1 (lookahead)", it's a type of parser/grammar which:

- Scans the input from left to right;
- It reads the leftmost symbol first;
- It uses 1 token to make parsing decisions;


If you're unfamiliar with this, this comes from formal languages theory in Computer science, a field that explains the mathematical foundations for lexers (tokenizers) and parsers.
A tokenizer is a module capable of distinguishing the valid tokens of a language, the parser is capable of detecting if said tokens are laid out in a way that respects the language's grammar.
LL1 is the easiest type of parser to build, but also the weakest in terms of capabilities.


To make this table, the columns will contain the used terminals, the rows will contain the used NTs, then, for every pair "(NT, T)":

- If the single terminal T is in the "First" set of NT (=NT is in "First" column of the previous table), then fill the corresponding cell with the production's number in which the terminal T is found as first token. That situation is encountered if a production of the form "NT &rarr; T ... " exists or both "NT &rarr; NT2 ..." and "NT2 &rarr; T..." exist as productions;
- If the single terminal T is not in the "First" set of NT, then leave the corresponding cell empty, as that's a syntax error;
- If NT is nullable, then consider the tokens that follow it (Those that are reported in the "Follow" column of the previous table) and for each of them, fill their corresponding cell with the NT's production number which produces the empty string (the production with form "NT &rarr; &epsilon;");


The result is the following:


|     | \[NOARGF\] | \[SNARGF\] | [INTEGER] | IDENTIFIER | FLOAT | KEYS | MOUSE | EXEC | ( |  , |  ) | + | TRUE | FALSE | RECT | PRESS | GARBAGE | \$
:----:|:----------:|:----------:|:---------:|:----------:|:-----:|:----:|:-----:|:----:|:-:|:--:|:--:|:-:|:----:|:-----:|:----:|:-----:|:-------:|:---:
\<S\> |          0 |          3 |        13 |         16 |    19 |    8 |     5 |    4 |   |    |    |   |   11 |    12 |   14 |    15 |      16 | 17
\<A\> |            |            |           |            |       |      |       |      | 1 |    |    |   |      |       |      |       |         |  2
\<B\> |            |            |           |            |       |      |       |      |   |    |  7 | 6 |      |       |      |       |         |
\<C\> |            |            |           |            |       |      |       |      |   | 18 | 10 | 9 |      |       |      |       |         |


In this situation, \<S\> has multiple tokens in the "First" set, so the respective production number is put in the cell related to the particular (NT, T) pair. The parentheses, the plus and the comma produce a syntax error instead.

Since \<S\> is nullable and is followed by \"\$\", it's empty string production number (17) is put in the cell (\<S\>, "\$"). If multiple tokens were in the "Follow" set, that had to be done for each token.

The rest of them are very easy to get, once you understand the logic.



## Numeric tokenizer


In the file [integer-automaton-for-tokenizer.png](integer-automaton-for-tokenizer.png) it is reported the automaton for the integer values.
In the implementation, this was transformed into a TokenReader child class.

Some of the transitions are reported as "(src, 'symbol') -> dest" in order to not complicate the drawing further.


The automaton recognizes:

- Standard decimal integers (e.g. 0, 1234, 52);
- 0d/0i prefixed decimal integers (e.g. 0d1234, 0i1234);
- 0b prefixed binary integers (e.g. 0b101010);
- 0o/0 prefixed octal integers (e.g. 0o12375, 0123474);
- 0x/0h prefixed hexadecimal integers (e.g. 0x123Af, 0h1234aF);
- i/d suffixed decimal integers (e.g. 1234d, 31i);
- b suffixed binary integers (e.g. 1010101b);
- o suffixed octal integers (e.g. 12367o);
- h/x suffixed hexadecimal integers (e.g. 128Abx, 128Abh);