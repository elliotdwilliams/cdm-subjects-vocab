"""Queries the CONTENTdm Server API to get all controlled vocabularies for fields named 'Subject'

Makes three types of API calls: first, to get a list of all collections on the server; second,
to get the field nickname for the "Subject" field; third, to get the controlled vocab for that
field. Saves output to a file called "all-CDM-subjects.txt".
"""

import requests

# Set base URL to CONTENTdm website URL
BASE_URL = "https://digital.utsa.edu"

# Define field to look for nickname of
FIELD_NAME = "Subject"

def get_aliases():
    """Queries API to get all collection aliases on server"""

    # Make an API request to get collection list
    collection_list_url = (BASE_URL +
                           "/digital/bl/dmwebservices/index.php?q=dmGetCollectionList/json")
    collection_response = requests.get(collection_list_url, timeout=5)

    # Create an empty list to hold collection aliases
    alias_list = []

    # Loop through collection list and add alias to list
    for collection in collection_response.json():
        alias = collection["alias"].lstrip("/")
        alias_list.append(alias)

    #print(alias_list)
    return alias_list


def get_nicknames(alias_list):
    """For each collection, queries API to get the field nickname for "Subject" field"""

    # Create empty list for collection alias/field nickname pairs
    subject_nicknames = []

    # Loop through list of alias and request field info
    for alias in alias_list:
        field_list_url = (BASE_URL +
                          "/digital/bl/dmwebservices/index.php?q=dmGetCollectionFieldInfo/" +
                          alias + "/json")
        field_response = requests.get(field_list_url, timeout=5)

        # Look for field where name is "Subject" and get field nickname
        for field in field_response.json():
            name = field["name"]
            nick = field["nick"]
            #print(name)

            # Add Subject field nickname and collection alias to subject_nicknames
            if name == FIELD_NAME:
                pair = [alias, nick]
                subject_nicknames.append(pair)

    print(subject_nicknames)
    return subject_nicknames


def get_subjects(subject_nicknames):
    """For each collection, queries API to get subject controlled vocabulary"""

    # Create empty list for term/collection pairs
    subjects_combined = []

    for collection in subject_nicknames:
        #alias, nickname = collection.split(',')
        alias = collection[0]
        nickname = collection[1]
        #print(alias + " " + nickname)

        # Make an API request to get collection list
        subject_url = (BASE_URL +
                       "/digital/bl/dmwebservices/index.php?q=dmGetCollectionFieldVocabulary/" +
                       alias + "/" + nickname + "/json")
        collection_subjects = requests.get(subject_url, timeout=5)

        # Loop through subject list and add to term/collection pair list
        for subj in collection_subjects.json():
            pair = [subj, alias]
            #print(pair)
            subjects_combined.append(pair)

    #print(subjects_combined)
    return subjects_combined


def main():

    alias_list = get_aliases()
    subject_nicknames = get_nicknames(alias_list)
    subjects_combined = get_subjects(subject_nicknames)

    # Save the combined subject data to file
    file_name = "all_CDM_subjects.txt"
    with open(file_name, mode="w", encoding="utf-8") as f:
        for pair in subjects_combined:
            f.write(str(pair[1]) + "\t" + str(pair[0]) + "\n")


if __name__ == "__main__":
    main()
