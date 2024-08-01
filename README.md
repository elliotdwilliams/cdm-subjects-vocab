# cdm-subject-vocabs

Python script for downloading controlled vocabularies for the Subject field for all collections on a CONTENTdm site.

First, the script gets a list of all collections on the CDM site. Then, for each collection, it gets a list of all fields in each collection, and looks for the field whose name is "Subject" and gets its field nickname.  Lastly, it then uses that nickname to get the controlled vocabulary for each Subject field.  Results are saved to a text file called "all-CDM-subjects.txt", and include all subject terms in the controlled vocabularies, along with the collection ID where that term is found.

Uses the dmwebservices wrapper for the CONTENTdm Server API: https://help.oclc.org/Metadata_Services/CONTENTdm/Advanced_website_customization/API_Reference/CONTENTdm_API/CONTENTdm_Server_API_Functions_dmwebservices

To use the script with a different CONTENTdm site, change the "base_URL" variable to the desired CONTENTdm URL.  To download CV's for a different field name, change the "field_name" variable.
