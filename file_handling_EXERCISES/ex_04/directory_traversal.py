import os


def extract_files(dir):
    return [el for el in dir if os.path.isfile(el)]
    # return [el for el in dir_content if "." in el]


def get_report_for_file_extensions(files):
    report = {}
    for file in files:
        file_name, extension = os.path.splitext(file)
        if extension not in report:
            report[extension] = []
        report[extension].append(file_name)
    return report


dir_content = os.listdir()

files = extract_files(dir_content)
report_info = get_report_for_file_extensions(files)

result_str = ""
for extension, file_name in sorted(report_info.items(), key=lambda x: x[0]):
    result_str += f"{extension}"
    for name in file_name:
        result_str += f"- - - {name}{extension}\n"

with open("C:\\Users\\Bilyana\\Desktop\\report.txt", "w") as file:
    file.write(result_str)

# for extension, file_name in sorted(report_info.items(), key=lambda x: x[0]):
#     print(f".{extension}")
#     print(*[f"- - - {name}.{extension}" for name in file_name], sep="\n")

