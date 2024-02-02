import csv
import re
import pathlib
from typing import Iterator

# full record example:          152081,Zootopia (2016),Action|Adventure|Animation|Children|Comedy
# record example to be parsed:  Zootopia (2016)
# desired output:               {title: 'Zootopia',
#                                year: '2016',
#                                genre: ['Action', 'Adventure', 'Animation', 'Children', 'Comedy']}

TITLE_YEAR_PATTERN = r"^(.+)\((\d{4})\)$"
GENRES = "genres"
TITLE = "title"
YEAR = "year"


def read_csv(filepath: pathlib.Path | str) -> Iterator[dict[str, str]]:
    with open(file=filepath, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)  # skip headers
        for line in reader:
            parsed = re.search(TITLE_YEAR_PATTERN, line[1])
            yield {
                TITLE: parsed.group(1).strip(),
                YEAR: parsed.group(2),
                GENRES: line[2].lower().split("|")
            }
