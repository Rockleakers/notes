import os

path = ".\\"

file_list = []

for root, dirs, files in os.walk(path):
    for index, filename in enumerate(files):
        #print(os.path.join(root, filename))
        if '.pdf' in filename:
            # print("<tr>")
            # print("\t<td></td>")
            # print("\t<td></td>")
            print("\t<td><a href=\"", os.path.join(root, filename), "\">", f'{filename}', "</a></td>", sep="")
            # print("</tr>")
            file_list.append(filename)

#print(file_list)