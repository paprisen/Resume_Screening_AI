from resume_parser import extract_text
from ranking import calculate_score

resume_path = input("Enter Resume PDF Path: ")

job_desc = input("Enter Job Description: ")

resume_text = extract_text(resume_path)

score = calculate_score(job_desc, resume_text)

print(f"\nMatch Score: {score}%")
