import ast
import os
from typing import List, Dict, Union

def read_file(file_path: str) -> str:
    "Read Python file content."
    with open(file_path, "r") as file:
        return file.read()

def parse_ast(content: str) -> ast.AST:
    "Parse Python content into AST."
    return ast.parse(content)

def get_total_lines(content: str) -> int:
    "Count total lines in file."
    return len(content.splitlines())

def extract_imports(tree: ast.AST) -> List[str]:
    "Extract imported packages."
    return [
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    ]

def extract_classes(tree: ast.AST) -> List[str]:
    "Extract class names."
    return [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]

def extract_functions(tree: ast.AST) -> List[str]:
    "Extract function names (excluding class methods)."
    return [
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and not any(isinstance(parent, ast.ClassDef) for parent in ast.iter_parent_nodes(node))
    ]

def get_docstrings(tree: ast.AST) -> Dict[str, str]:
    "Extract docstrings for classes and functions."
    def docstring(node, node_type):
        ds = ast.get_docstring(node)
        return ds if ds else f"{node_type} {node.name}: DocString not found."

    docstrings = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.ClassDef, ast.FunctionDef)):
            node_type = "class" if isinstance(node, ast.ClassDef) else "function"
            docstrings[node.name] = docstring(node, node_type)
    return docstrings

def functions_missing_annotations(tree: ast.AST) -> List[str]:
    "List functions missing type annotations."
    def has_annotations(node: ast.FunctionDef) -> bool:
        return all(arg.annotation is not None for arg in node.args.args) and node.returns is not None

    return [
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and not has_annotations(node)
    ]

def invalid_class_names(tree: ast.AST) -> List[str]:
    "List classes not following CamelCase."
    return [
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef) and (not node.name[0].isupper() or "_" in node.name)
    ]

def invalid_function_names(tree: ast.AST) -> List[str]:
    "List functions/methods not following snake_case."
    return [
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and (not node.name.islower() or " " in node.name)
    ]

def generate_report(file_path: str) -> str:
    "Generate the style report as a string."
    content = read_file(file_path)
    tree = parse_ast(content)

    total_lines = get_total_lines(content)
    imports = extract_imports(tree)
    classes = extract_classes(tree)
    functions = extract_functions(tree)
    docstrings = get_docstrings(tree)
    missing_annotations = functions_missing_annotations(tree)
    invalid_classes = invalid_class_names(tree)
    invalid_functions = invalid_function_names(tree)

    lines = []

    # File Structure
    lines.append(" File Structure ")
    lines.append(f"Total lines of code: {total_lines}")
    lines.append(f"Imported packages: {', '.join(imports) if imports else 'None'}")
    lines.append(f"Classes: {', '.join(classes) if classes else 'None'}")
    lines.append(f"Functions: {', '.join(functions) if functions else 'None'}")
    lines.append("")

    # DocStrings
    lines.append(" DocStrings ")
    for name, docstring in docstrings.items():
        lines.append(f"{name}:\n{docstring}\n")

    # Type Annotations
    lines.append(" Type Annotation ")
    if not missing_annotations:
        lines.append("All functions and methods use type annotations.")
    else:
        lines.append(f"Functions/methods without type annotations: {', '.join(missing_annotations)}")
    lines.append("")

    # Naming Conventions
    lines.append(" Naming Convention ")
    if not invalid_classes and not invalid_functions:
        lines.append("All names adhere to the specified naming conventions.")
    else:
        if invalid_classes:
            lines.append(f"Classes not in CamelCase: {', '.join(invalid_classes)}")
        if invalid_functions:
            lines.append(f"Functions or methods not in snake_case: {', '.join(invalid_functions)}")
    lines.append("")

    return "\n".join(lines)

def save_report(file_path: str, report: str) -> None:
    "save the generated report."
    directory = os.path.dirname(file_path)
    base_name = os.path.basename(file_path).replace(".py", "")
    report_file_path = os.path.join(directory, f"style_report_{base_name}.txt")

    with open(report_file_path, "w") as f:
        f.write(report)

    print(f"Report saved to: {report_file_path}")

def main() -> None:
    "Main function to run style checker."
    input_path = input("Type the path to the Python (.py) file: ").strip()
    if not os.path.isfile(input_path):
        print("wrong file path given.")
        return

    report = generate_report(input_path)
    save_report(input_path, report)

if __name__ == "__main__":
    main()
## ya done now