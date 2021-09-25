import os

files = [
    "Fields",
    "Structs",
    "DelegatesEventsLambdas",
    "Generics",
    "Interfaces",
    "LINQ",
    #"Reflection",
    #"Attributes",
    "Enums",
]

result_file_name = 'FullConsultation.ipynb'

top = """{
 "cells": ["""

me = """  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Консультация 2021\\n",
    "## Подготовил Махнач Фёдор, tg: @fmakhnach"
   ]
  },
"""

bottom = """],
 "metadata": {
  "kernelspec": {
   "display_name": ".NET (C#)",
   "language": "C#",
   "name": ".net-csharp"
  },
  "language_info": {
   "file_extension": ".cs",
   "mimetype": "text/x-csharp",
   "name": "C#",
   "pygments_lexer": "csharp",
   "version": "8.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}"""

existing_files = [file + ".ipynb" for file in files if os.path.exists(file + ".ipynb")]
print(*existing_files)

start_id = len(top)
end_id = -len(bottom) - 1
with open(result_file_name, 'w', encoding='utf-8') as result:
    result.write(top)
    result.write(me)
    for i, file in enumerate(existing_files):
        with open(file, 'r', encoding="utf-8") as f:
            all_text = f.read()
            result.write(all_text[start_id:end_id])
            if i + 1 != len(existing_files):
                result.write(',\n')
    result.write(bottom)
