import tabula
import json

def convert_pdf_to_json(pdfFile):
    tbl_list = tabula.read_pdf(pdfFile)
    if len(tbl_list) == 0:
        return "No Tables found..."
    out_arr = []
    for tbl in tbl_list:
        row_arr = []
        for i, row in tbl.iterrows():
            row_arr.append(json.loads(row.to_json()))
        out_arr.append(row_arr)
  
    return json.dumps(out_arr, indent=2)

print(convert_pdf_to_json("test.pdf"))