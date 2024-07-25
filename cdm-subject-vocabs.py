import requests

# Set base URL to CONTENTdm website URL
BASE_URL = "https://digital.utsa.edu"

# Set file with collection aliases and field nicknames
COLLECTION_FILE = "alias-test.txt"

# Create empty list for collection info
collection_info = []

# Create empty list for term/collection pairs
subjects_combined = []

# Read collection info from file into list
with open(COLLECTION_FILE) as f:
    for line in f:
        collection_info.append(line.strip())

print(collection_info)

for collection in collection_info:
    alias, nickname = collection.split(',')
    print(alias + " " + nickname)

    # # Make an API request to get collection list
    subject_url = BASE_URL + "/digital/bl/dmwebservices/index.php?q=dmGetCollectionFieldVocabulary/" + alias + "/" + nickname + "/json"
    collection_subjects = requests.get(subject_url, timeout=5)

    # Loop through subject list and add to term/collection pair list
    for subj in collection_subjects.json():
        pair = [subj, alias]
        #print(pair)
        subjects_combined.append(pair)

#print(subjects_combined)

# Save the combined subject data to file
file_name = "all_CDM_subjects.txt"
with open(file_name, mode="w", encoding="utf-8") as f:
    for pair in subjects_combined:
        f.write(str(pair[1]) + "\t" + str(pair[0]) + "\n")