from docx import Document
import json, re, os

files = [
    "Training Plan.docx",
    "CDC_UP_Test_Case_Template.doc",
    "EPLC_SLA_MOU_Template (1).doc",
    "CDC_UP_Operation_Maintenance_Manual_Template.doc"
]

def parse_doc_to_json(filepath):
    doc = Document(filepath)
    sections = {}
    current_section = None
    record = False

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue

        # Start capturing once first section (1.0 or 1.) appears
        if re.match(r"^1(\.|\.0)?\s+", text):
            record = True

        if not record:
            continue

        # Detect numbered section headers (e.g. 1., 1.1, 2.0, etc.)
        if re.match(r"^\d+(\.\d+)*\s+", text):
            current_section = text
            sections[current_section] = []
        elif current_section:
            sections[current_section].append(text)

    document = {
        "document_title": os.path.splitext(os.path.basename(filepath))[0],
        "source_filename": os.path.basename(filepath),
        "sections": []
    }

    for title, content in sections.items():
        section_number = title.split(" ")[0]
        section_title = " ".join(title.split(" ")[1:])
        document["sections"].append({
            "number": section_number,
            "title": section_title,
            "content": " ".join(content)
        })

    output_file = os.path.splitext(filepath)[0] + ".json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(document, f, indent=2, ensure_ascii=False)
    print(f"✅ Created {output_file}")

for f in files:
    parse_doc_to_json(f)
