from testmark import parse

from pathlib import Path


testmark_data = {}
for file in Path("testdata").iterdir():
    res = parse(file)
    testmark_data.update(res)

test_string = """the content of this code block is data which can be read,
and *replaced*, by testmark.
"""

assert testmark_data["this-is-the-data-name"] == test_string
assert testmark_data[Path("one/two")] == "foo\n"
