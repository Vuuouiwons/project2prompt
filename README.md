# Promtizer
Promptizer is a lightweight developer tool that bundles your entire project into a single file — perfect for sharing with large language models (LLMs) for debugging, refactoring, or documentation help.

No more copy-pasting files one by one. Just run Promptizer and get your entire project in one compact, prompt-ready text file.
What could possibly go wrong, right?

## Usage
```ps1
promptizer.exe <source_path>
```
### Example:
```ps1
promptizer.exe ./my_project/src
```
This will create a single text file (e.g., prompt_output.txt) containing all source code from the specified directory.
#### Output:
```text
===
./main.py
print("Hello World")
===
./utils/helpers.py
def add(a, b):
    return a + b
```

## Security
Promptizer is designed for LLM code analysis, but be careful when sharing compiled output — it may contain:
- API keys or secrets
- Private data or credentials
- Proprietary code

## build
If you want to build Promptizer yourself:
```bash
pyinstaller --onefile --name promptizer ./src/main.py
```
