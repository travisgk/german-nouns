# german-nouns
Thousands of German nouns sorted by their grammatical gender into five alphabetical text lists: 
- Masculine Nouns
- Feminine Nouns
- Neutral Nouns
- Infinitive Verbs (as nouns that lack plurals).
- Plural-only Nouns.

## Data Sources

Each singular noun has its plural form(s) provided. Many plurals were scraped from [Wiktionary](https://de.wiktionary.org/).

Most of these lists are adapted from [Chris Posselt’s](https://github.com/cpos)  repository [AlleDeutschenWoerter](https://github.com/cpos/AlleDeutschenWoerter). 
Additional words, including those with umlauts (ä, ö, ü) or an eszett (ß), have been added to expand coverage.

The list of infinitive verbs was originally based on [Stan James’s](https://github.com/wanderingstan) gist [top-german-verbs.csv](https://gist.github.com/wanderingstan/7eaaf0e22461b505c749e268c0b72bc4). 

However, the dataset here has been transformed and split into two files by cross-referencing it with the project's other files, with only raw infinitives retained.
Frequency, ranking information, and conjugations from the original dataset are **not** used.

<br>

## Usage
`Junge	Jungen	Jungs	Jungens`

Simply grab a line from the file and split it by `"\t"`.

`... = ["Junge", "Jungen", "Jungs", "Jungens"]`

The first element will be the singular form, while any following elements will be the plural forms, with the most frequently-used plurals showing up earlier in the list than others.

If the plural element is `"—"`, then that means that the noun is only used in the singular.

<br>

## Notes

- There could be a few nouns which are created by modifying the ending of an existing adjective. **These need to be removed**, since "der Vorsitzende" and "ein Vorsitzender" each require different endings depending on the article.
- The "das" nouns contain many infinitives made into verbs. Those that have a plural form seemingly *do* have a plural form given on Wiktionary, so these may not be of concern.
