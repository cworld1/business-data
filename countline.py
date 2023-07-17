import nbformat


def count_python_code_lines(notebook_file):
    with open(notebook_file, "r") as f:
        nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

    code_lines = 0
    for cell in nb.cells:
        if cell.cell_type == "code":
            if (
                "metadata" in cell
                and "tags" in cell.metadata
                and "hide-output" in cell.metadata.tags
            ):
                # Skip cells tagged with 'hide-output'
                continue
            lines = cell.source.split("\n")
            for line in lines:
                if line.strip() and not line.strip().startswith("#") and line != "\n":
                    code_lines += 1

    return code_lines


notebook_file = "main.ipynb"
total_lines = count_python_code_lines(notebook_file)
print(f"Total Python code lines (excluding comments and empty lines): {total_lines}")
