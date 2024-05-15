import re
import subprocess

def run_terminal_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def clean_and_format_line(line):
    # Remove non-ASCII characters
    cleaned_line = re.sub(r'[^\x00-\x7F]+', ' ', line).strip()
    # Split on whitespace to isolate package and version
    parts = cleaned_line.split()
    if len(parts) >= 2:
        # Assume the last part is the version, the first part is the package name
        package = parts[0]
        version = parts[-1]
        return f"{package}=={version}"
    return None

""" HOW TO UPDATE:
1) install the new py version from https://www.python.org/
2) set old_version and new_version
"""
old_version = '3.12'
new_version = '3.12'

"""
3) run this script
4) uninstall old py version
"""



old_python_path = run_terminal_command(f'py -{old_version} -c "import sys; print(sys.executable)"')
print(f"Python executable path for version {old_version}: {old_python_path}")
new_python_path = run_terminal_command(f'py -{new_version} -c "import sys; print(sys.executable)"')
print(f"Python executable path for version {new_version}: {new_python_path}")
input('aa')
package_list = run_terminal_command(f'{old_python_path} -m pip list')
formatted_package_list = [clean_and_format_line(line) for line in package_list.split('\n') if clean_and_format_line(line)]
formatted_package_list = formatted_package_list[2:]

# Write formatted_package_list to a new file        
with open('formatted-package-list.txt', 'w') as file:
    for item in formatted_package_list:
        file.write(item + '\n')


install_command = f'{new_python_path} -m pip install -r formatted-package-list.txt'
install_result = run_terminal_command(install_command)
print(install_result)




