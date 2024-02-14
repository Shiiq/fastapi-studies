import csv
import pathlib
import re
from sys import stdout
from typing import Any, Iterator

# full record example:          152081,Zootopia (2016),Action|Adventure|Animation|Children|Comedy
# record example to be parsed:  Zootopia (2016)
# desired output:               {title: 'Zootopia',
#                                year: '2016',
#                                genre: ['Action', 'Adventure', 'Animation', 'Children', 'Comedy']}

TITLE_YEAR_PATTERN = r"^(.+)\((\d{4})\)$"
GENRES = "genres"
TITLE = "title"
YEAR = "year"


def read_csv(filepath: pathlib.Path | str) -> Iterator[dict[str, Any]]:

    stdout.write(f"\nStarting to read <{filepath}>\n")
    with open(file=filepath, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")

        # skip headers
        next(reader)

        for line in reader:
            parsed = re.search(TITLE_YEAR_PATTERN, line[1])
            assert parsed is not None
            yield {
                TITLE: parsed.group(1).strip(),
                YEAR: parsed.group(2),
                GENRES: line[2].lower().split("|")
            }
