import json
from sentence_transformers import SentenceTransformer

data = {
  "document_title": "Lessons Learned Log",
  "sections": [
    {
      "section_number": "1",
      "section_title": "Instructions for Completing This Document",
      "text": "Complete the Project Name, NC, Project Manager Name, and Project Description fields.\nFor each change request identified, complete the following:\n\nA. ID: A unique ID number used to identify the lesson learned in the lesson learned log.\nB. Date Identified: This column should be populated with the date that the lesson learned was identified.\nC. Entered By: This column should be populated with the name of the individual who identified the lesson learned.\nD. Subject: This column should be populated with a brief attention-grabbing headline that describes the subject of the lesson learned.\nE. Situation: This column should be populated with a detailed description of the situation learned from.\nF. Lesson Learned & Recommendations: This column should be populated with a description of the lesson learned from the situation described in column E and the corrective action taken. Include recommendations regarding the outcome of the corrective action, good or bad, to help guide future projects.\nG. Follow-Up Needed: Indicates whether or not additional follow-up is needed."
    },
    {
      "section_number": "2",
      "section_title": "Instructions for Changing the Contents of Drop-Down Menus",
      "text": "Highlight the cell where you wish to change the content of the drop-down menu.\nFrom the file menu click 'Data' -> 'Validation' and change the content of the source field."
    },
    {
      "section_number": "3",
      "section_title": "Instructions for Filtering Data",
      "text": "Highlight the header of the cell you wish to filter data on.\nFrom the file menu click 'Data' -> 'Filter' -> 'Auto Filter'.\nThen select your filter criteria from the drop-down menu that appears on your header cell."
    },
    {
      "section_number": "4",
      "section_title": "Example Lesson Entry",
      "text": "Project Name:<> \nNational Center:<> \nProject Manager Name:<> \nProject Description:<> \nDate Identified: 01/01/01\nEntered By: John Doe\nSubject: Issue escalation\nSituation: Issue escalation took too long\nRecommendations & Comments: Have in place a solid communication plan that outlines the escalation process, the roles & responsibilities of individuals involved in that process, and a required response time.\nFollow-Up Needed: Yes"
    }
  ]
}

model = SentenceTransformer("BAAI/bge-large-en-v1.5")

for section in data["sections"]:
    section["embedding"] = model.encode(section["text"]).tolist()

with open("Lessons_Learned_Log_embedding.json", "w", encoding="utf-8") as f:
    json.dump(data["sections"], f, indent=2, ensure_ascii=False)

