import ast
import os
import re


class PythonStyleChecker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.imports = []
        self.classes = []
        self.functions = []
        self.errors = []
        self.total_lines = 0

    def analyze(self):
        with open(self.file_path, 'r') as file:
            source = file.read()
            self.total_lines = len(source.splitlines())

        tree = ast.parse(source)
        self._extract_imports(tree)
        self._extract_classes_and_functions(tree)
        self._check_docstrings(tree)
        self._check_type_annotations()
        self._check_naming_conventions()

    def _extract_imports(self, tree):
        """Extract imports from the AST."""
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for n in node.names:
                    self.imports.append(n.name)
            elif isinstance(node, ast.ImportFrom):
                self.imports.append(f"{node.module} ({', '.join([n.name for n in node.names])})")

    def _extract_classes_and_functions(self, tree):
        """Extract all classes and functions from the AST."""
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                self.classes.append(node.name)
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        self.functions.append((node.name, item))
            elif isinstance(node, ast.FunctionDef):
                self.functions.append((None, node))

    def _check_docstrings(self, tree):
        """Check for missing docstrings in classes and functions."""
        # Check for missing docstring in classes
        for class_name in self.classes:
            class_node = next(node for node in ast.walk(tree) if isinstance(node, ast.ClassDef) and node.name == class_name)
            docstring = ast.get_docstring(class_node)
            if not docstring:
                self.errors.append(f"class {class_name}: DocString not found.")

        # Check for missing docstring in functions and methods
        for class_name, func_node in self.functions:
            docstring = ast.get_docstring(func_node)
            if not docstring:
                if class_name:
                    self.errors.append(f"{class_name}_{func_node.name}: DocString not found.")
                else:
                    self.errors.append(f"function {func_node.name}: DocString not found.")

    def _check_type_annotations(self):
        """Check for functions/methods that lack type annotations."""
        for class_name, func_node in self.functions:
            if any(isinstance(arg, ast.arg) and arg.annotation is None for arg in func_node.args.args):
                if class_name:
                    self.errors.append(f"{class_name}_{func_node.name}: Type annotation missing.")
                else:
                    self.errors.append(f"{func_node.name}: Type annotation missing.")
        if not any(isinstance(arg, ast.arg) and arg.annotation is None for class_name, func_node in self.functions for arg in func_node.args.args):
            self.errors.append("All functions and methods have type annotations.")

    def _check_naming_conventions(self):
        """Check naming conventions for classes and functions."""
        for class_name in self.classes:
            if not re.match(r'^[A-Z][a-zA-Z0-9]*$', class_name):
                self.errors.append(f"{class_name}: Does not follow CamelCase convention.")

        for class_name, func_node in self.functions:
            if class_name:
                method_name = f"{class_name}_{func_node.name}"
            else:
                method_name = func_node.name

            if not re.match(r'^[a-z_][a-z0-9_]*$', method_name):
                self.errors.append(f"{method_name}: Does not follow snake_case convention.")

        if not self.errors:
            self.errors.append("All names adhere to the naming convention.")

    def generate_report(self):
        """Generate a style report."""
        report_filename = f"style_report_{os.path.basename(self.file_path)}.txt"
        with open(report_filename, 'w') as report:
            report.write(f"File: {self.file_path}\n")
            report.write(f"Total lines of code: {self.total_lines}\n")
            report.write(f"Imports: {', '.join(self.imports) if self.imports else 'No imports found'}\n")
            report.write(f"Classes: {', '.join(self.classes) if self.classes else 'No classes found'}\n")
            report.write(f"Functions: {', '.join([f'{(class_name + '_' if class_name else '') + func.name}' for class_name, func in self.functions]) if self.functions else 'No functions found'}\n")
            report.write("\nDocstrings:\n")
            for error in self.errors:
                report.write(f"{error}\n")


if __name__ == "__main__":
    file_path = "Assignment01/example.py"
    checker = PythonStyleChecker(file_path)
    checker.analyze()
    checker.generate_report()
