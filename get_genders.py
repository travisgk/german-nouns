"""
Filename: get_genders.py
---
Author: TravisGK
Date: 29 August 2025

Description: This contains the function to return 
             a list of strings indicating a word's possible gender(s).

    Key:
        "sm" = singular masculine.
        "sf" = singular feminine.
        "sn" = singular neutral.
        "pm" = plural masculine.
        "pf" = plural feminine.
        "pn" = plural neutral.
        "po" = plural-only.

        "(L)" = "list"; determined from text list (most reliable).
        "(A)" = "absolute"; follows a very consistent pattern.
        "(G)" = "guess"; follows somewhat consistent patterns (less reliable).

"""

import sys
from pathlib import Path

LISTS_DIR = Path(__file__).parent / "words"


def _load_words(article: str, singulars: list, plurals: list) -> None:
    file_path = LISTS_DIR / f"{article}.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip().lower()
            elements = clean_line.split("\t")
            if elements[0] == "—" and len(elements) > 1:
                plurals.append(elements[1])
                continue

            singulars.append(elements[0])

            for element in elements[1:]:
                if element == "—":
                    break
                plurals.append(element)


_der_singulars = []
_der_plurals = []
_die_singulars = []
_die_plurals = []
_das_singulars = []
_das_plurals = []
_plural_onlys = []


def _load_sets():
    global _der_singulars, _der_plurals
    global _die_singulars, _die_plurals
    global _das_singulars, _das_plurals
    global _plural_onlys
    if len(_der_singulars) == 0:
        _load_words("der", _der_singulars, _der_plurals)
        _load_words("die", _die_singulars, _die_plurals)
        _load_words("das", _das_singulars, _das_plurals)
        _load_words("plural-only", [], _plural_onlys)

        _der_singulars = set(_der_singulars)
        _der_plurals = set(_der_plurals)

        _die_singulars = set(_die_singulars)
        _die_plurals = set(_die_plurals)

        _das_singulars = set(_das_singulars)
        _das_plurals = set(_das_plurals)

        _plural_onlys = set(_plural_onlys)


def _find_results(
    word: str, grade: str, s_der, s_die, s_das, prior_chen: str, p_der, p_die, p_das
) -> list:
    results = []
    is_chen_word = False
    if word.endswith("chen") and word[-5] in prior_chen:
        results.append(f"sn({grade})")
        is_chen_word = True
    elif any(word.endswith(end) for end in s_der):
        results.append(f"sm({grade})")
    elif any(word.endswith(end) for end in s_die):
        results.append(f"sf({grade})")
    elif any(word.endswith(end) for end in s_das):
        results.append(f"sn({grade})")

    if is_chen_word:
        results.append(f"pn({grade})")
    elif any(word.endswith(end) for end in p_der):
        results.append(f"pm({grade})")
    elif any(word.endswith(end) for end in p_die):
        results.append(f"pf({grade})")
    elif any(word.endswith(end) for end in p_das):
        results.append(f"pn({grade})")

    return results


def _get_gender_by_absolutes(word: str) -> list:
    return _find_results(
        word=word,
        grade="A",  # absolute
        s_der=["ant", "ast", "eich", "ismus", "wert"],
        s_die=[
            "enz",
            "heit",
            "ie",
            "schaft",
            "sion",
            "tion",
            "tät",
            "ung",
            "macht",
            "firma",
        ],
        s_das=["lein", "ing", "ment", "tum", "thema", "schema"],
        prior_chen="dfghkmptvwxzß",
        p_der=["eiche", "ismen", "werte"],
        p_die=[
            "enzen",
            "heiten",
            "ien",
            "schaften",
            "sionen",
            "tionen",
            "täten",
            "ungen",
            "mächte",
            "firmen",
        ],
        p_das=["inge", "mente", "tümer", "themen", "schemen"],
    )


def _get_gender_by_guessing(word: str) -> list:
    return _find_results(
        word=word,
        grade="G",  # guessing
        s_der=["er", "ich", "ig", "eig", "or"],
        s_die=["anz", "ur"],
        s_das=["il", "ma", "nis"],
        prior_chen="n",
        p_der=["er", "oren"],
        p_die=["anzen", "uren"],
        p_das=["nisse"],
    )


def get_genders(word: str) -> list:
    """
    Returns a list of strings,
    each representing the kind of article the noun could have,
    along with a grade of certainty from the program itself.

    Key:
        "sm" = singular masculine.
        "sf" = singular feminine.
        "sn" = singular neutral.
        "pm" = plural masculine.
        "pf" = plural feminine.
        "pn" = plural neutral.
        "po" = plural-only.

        "(L)" = "list"; determined from text list (most reliable).
        "(A)" = "absolute"; follows a very consistent pattern.
        "(G)" = "guess"; follows somewhat consistent patterns (less reliable).
    """
    if not word[0].isalpha() or not word[0].isupper():
        return []

    word = word.lower()

    _load_sets()
    results = []

    if any(word.endswith(plural) for plural in _plural_onlys):
        return [
            "po(L)",
        ]

    if word in _der_singulars:
        results.append("sm(L)")
    if word in _die_singulars:
        results.append("sf(L)")
    if word in _das_singulars:
        results.append("sn(L)")

    if word in _der_plurals:
        results.append("pm(L)")
    if word in _die_plurals:
        results.append("pf(L)")
    if word in _das_plurals:
        results.append("pn(L)")

    if word in _plural_onlys:
        results.append("po(L)")

    if len(results) == 0:
        results = _get_gender_by_absolutes(word)
        if len(results) == 0:
            results = _get_gender_by_guessing(word)
    return results


def main():
    word = sys.argv[1] if len(sys.argv) > 1 else "Kaninchen"
    if word[0].islower():
        word = word[0].upper() + word[1:]
    print(get_genders(word))


if __name__ == "__main__":
    main()
