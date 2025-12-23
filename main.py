with open("resume.txt","r") as file:
    lines=file.readlines()

clean_lines=[]
for line in lines:
    line=line.strip()

    if line and line not in clean_lines:
        clean_lines.append(line)

final_lines=[]
for line in clean_lines:
    final_lines.append(line.title())

with open("clean_resume.txt","w") as file:
    for line in final_lines:
        file.write(line+"\n")
print("Resume cleaned successfully!")