# german-word-lists
German words sorted by their grammatical gender into four text lists: masculine, feminine, neutral and plural-only nouns.

Each singular noun has its plural form(s) provided. Many plurals were scraped from [Wiktionary](https://de.wiktionary.org/).

Simply grab a line from the file and split it by `"\t"`; the first element will be the singular form, while any following elements will be the plural forms, with the most frequently-used plurals showing up earlier in the list than others.

<br>

# Notes
There could be a few nouns which are created by modifying the ending of an existing adjective. These need to be removed, since "der Vorsitzende" and "ein Vorsitzender" each require different endings depending on the article.


# Special Thanks
These lists are based off of the lists found in Chriss Posselt's repository [AlleDeutschenWoerter](https://github.com/cpos/AlleDeutschenWoerter). Words with umlauts (äöü) or an eszett (ß) have been added to the lists.
