import sys
import yaml
from yamllint import linter
from yamllint.config import YamlLintConfig

def validate_yaml_structure(file_path):
    try:
        with open(file_path, 'r') as f:
            yaml.safe_load(f)
        print(f"✅ YAML structure is valid: {file_path}")
    except yaml.YAMLError as e:
        print(f"❌ YAML syntax error in {file_path}:\n{e}")
        return False
    return True

def lint_yaml(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    config = YamlLintConfig('extends: default')
    problems = list(linter.run(content, config, file_path))

    if problems:
        print(f"⚠️  Lint issues in {file_path}:")
        for problem in problems:
            print(f"  {problem}")
    else:
        print(f"✅ No lint issues in: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_yaml.py <file.yaml>")
        sys.exit(1)

    filepath = sys.argv[1]

    if validate_yaml_structure(filepath):
        lint_yaml(filepath)
