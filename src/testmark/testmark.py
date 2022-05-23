from pathlib import Path


def parse(file: str) -> dict:
    """
    parse(file: str) -> dict:
    input a markdown(.md) filepath

    parses all testmarkformatted codeblocks.
        returns -> a dictionairy with
            - data-names as key
            - codeblock content as value
    """

    code_line = "```"
    testmark_line = "[testmark]:# "
    testmark_blocks = {}

    with open(file) as f:
        lines = f.readlines()

    # create all codeblock indicators
    blocks = [idx for idx, line in enumerate(lines) if line.startswith(code_line)]
    if len(blocks) % 2 == 1:
        print("Uneven amount of codeblocks indicate wrongly formated markdown")
        raise ImportError

    for block_start, block_end in zip(blocks[::2], blocks[1::2]):

        # check if testmark-codeblock
        if lines[block_start - 1].startswith(testmark_line):

            # build data-name string
            codeblock_title = (
                lines[block_start - 1]
                .replace(testmark_line, "")
                .replace("(", "")
                .replace(")", "")
                .replace("\n", "")
            )
            # build PATH if codeblock_title looks like one
            if "/" in codeblock_title:
                codeblock_title = Path(codeblock_title)

            # get content of codeblock and add
            testmark_block_content = "".join(lines[block_start + 1 : block_end])
            testmark_blocks[codeblock_title] = testmark_block_content

    return testmark_blocks
