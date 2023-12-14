# Testing regular expressions with web scraping.
# End goal of the project is to move onto Selenium based Python scripts.
# For now, this will do.

import re

# Functionally necessary values

parse_point_list = ["<a id"]
search_list = ['ELECTRONIC']

# Static values

find_list = []
flag_for_parse = False
total_document_count = 0
total_document_matches = 0

# Placeholder values follow

arbiter_role = "What"

# The following is the basic search algorithm, and believe me - it's basic
# It will match regular expressions in search_list and append them to find_list

def termsearch(bard_line):
    for search_element in search_list:
        goodmatch = re.search(search_element, bard_line)
        if goodmatch:
            print(bard_line)
            combined_forces = arbiter_role + bard_line
            find_list.append(combined_forces)
            print(combined_forces)
            flag_for_parse == False
        else:
            flag_for_parse == False

# The below open file invocation should be the only part that has to be manually changed
# (for now at least)
# The rationale behind this is my lack of skills with dealing with backslashes:
# I'll probably change it to a more complex input parser because of escape sequences

test_file = open("C:\\Users\\laztu\\documents\\miltest.xml", "r", encoding="utf8")

for xml_line in test_file:
    if flag_for_parse == False:
        for cutting_edge in parse_point_list:
            match = re.search(cutting_edge, xml_line)
            if match:
                print(xml_line)
                flag_for_parse = True
                arbiter_role = xml_line
                total_document_count += 1
                # This is a placeholder for what is to be appended
    elif flag_for_parse == True:
        termsearch(xml_line)
        total_document_matches += 1
    else:
        print("An unknown error has occurred.")

# Everything is appended here.

print(find_list)
print("\n")
print("There were")

# Closing the door after you is polite.

test_file.close()