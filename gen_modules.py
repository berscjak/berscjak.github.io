import glob, os
from mkdocs_gen_files import open as gen_open

MODULES = glob.glob("src/silkmoth/*.py")
for path in MODULES:
    name = os.path.splitext(os.path.basename(path))[0]
    if name == "__init__":
        continue

    doc_path = f"pages/{name}.md"
    with gen_open(doc_path, "w") as f:
#        f.write(f"# {name}\n\n")
        f.write(f"::: silkmoth.{name}\n")
        f.write("    rendering:\n")
        f.write("      show_signature: true\n")
        f.write("      show_source: true\n")
