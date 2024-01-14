import csv
import re
import pathlib
from typing import Iterator

# full record example:          193609,Andrew Dice Clay: Dice Rules (1991),Comedy
# record example to be parsed:  Andrew Dice Clay: Dice Rules (1991)
# desired output:               {title: 'Andrew Dice Clay: Dice Rules', year: '1991'}

TITLE_YEAR_PATTERN = r"^(.+)\((\d{4})\)$"
TITLE_FIELD = "title"
YEAR_FIELD = "year"


def read_csv(filepath: pathlib.Path | str) -> Iterator[dict[str, str]]:
    with open(filepath) as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)  # skip headers
        for line in reader:
            parsed = re.search(TITLE_YEAR_PATTERN, line[1])
            yield {
                TITLE_FIELD: parsed.group(1).strip(),
                YEAR_FIELD: parsed.group(2)
            }
