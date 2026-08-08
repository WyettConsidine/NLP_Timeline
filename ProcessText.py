
import os
from dateparser.search import search_dates

import json




def read_markdown_file(filepath):   #make function with input parameter filepath
    timelineList = []
    with open(filepath, 'r', encoding="utf-8") as f: 
        lines_list = f.readlines()
        for line in lines_list:
            if '#timeline' in line:
                timelineList.append(line.replace('\t','').replace('\n','').replace('#timeline',''))
    return timelineList

def read_markdown_file_denoted(filepath):   #make function with input parameter filepath
    filename = filepath.split('\\')[-1]
    timelineList = []
    with open(filepath, 'r', encoding="utf-8") as f: 
        lines_list = f.readlines()
        for line in lines_list:
            if '#timeline' in line:
                timelineList.append((line.replace('\t','').replace('\n','').replace('#timeline',''), filename))
    return timelineList


def read_markdown_file_denoted_withDates(filepath):   #make function with input parameter filepath
    filename = filepath.split('\\')[-1]
    timelineList = []
    with open(filepath, 'r', encoding="utf-8") as f: 
        lines_list = f.readlines()
        for line in lines_list:
            if '#timeline' in line:
                nline = line.replace('\t','').replace('\n','').replace('#timeline','')
                dateline = get_dates_from_line(nline)
                timelineList.append((dateline, filename))
    return timelineList

def get_all_files(dirPath):
    files_list = []
    for entry in os.listdir(dirPath):
        full_path = os.path.join(dirPath, entry)
        if os.path.isfile(full_path):  #is this a file frfr?
            files_list.append(full_path)
    return files_list


def read_multi_file(FilePathList, denoted = 0):  
    timelineList = []
    for filepath in FilePathList:
        print(filepath)
        if denoted == 1:
            timelineList.extend(read_markdown_file_denoted(filepath))
        else:
            timelineList.extend(read_markdown_file(filepath))
    return timelineList

def write_to_txt(fileName, lines):
    with open( fileName, "w") as file:
        for l in lines:
            file.write(l + '\n')


def write_to_JSON(FileName, lines):

    dictLines = []

    for line in lines:
        if line[0] != []:
            dictLines.append({"Date":str(line[0][0]),"File":line[1],"Text":line[2] })
    js = json.dumps(dictLines)
    with open(FileName, "w") as f:
        json.dump(js, f, indent=4)
    print('Json written to file ' + FileName )

def get_dates_from_line(line, sortbydate = 0):
    string = line.split('-')
    dates = []
    out = ''
    for word in string:
        out = search_dates(word,settings={'PREFER_DAY_OF_MONTH': 'first','PREFER_MONTH_OF_YEAR': 'first'})
        if out != None:
            dates.append(search_dates(word,settings={'PREFER_DAY_OF_MONTH': 'first','PREFER_MONTH_OF_YEAR': 'first'})[0][1])
    if sortbydate==1:
        dates.sort()
    return (line, dates)

def sort_dateline_output ( datelines):
    newlist = []
    for item in datelines:
        newlist.append((item[0][1], item[1], item[0][0]))
    newlist.sort()
    return newlist



def main():
    ret = read_markdown_file_denoted_withDates(r".\TextData\Trautmann.md")
    ret = sort_dateline_output(ret)
    for line in ret:
        #print(line)
        if line[0] != []:
            print(str(line[0][0]), line[1], line[2])
    write_to_JSON(r".\JSON_Output\TrauntTest.json", ret)

if __name__ == "__main__":
    main()






# Example usage:
##print('starting')
#file_content = read_markdown_file(r"C:\Users\wyett\OneDrive\Documents\EvanNLP\Trautmann.md")
#print(file_content)
#write_to_txt('timelineLines.txt', file_content)

##Example usage:
#print('starting')
#file_content = read_markdown_file_denoted(r"C:\Users\wyett\OneDrive\Documents\EvanNLP\TextData\Trautmann.md")
#print(file_content)
##write_to_txt('timelineLines.txt', file_content)


#files = get_all_files(r"C:\Users\wyett\OneDrive\Documents\EvanNLP\TextData")
#lines = read_multi_file(files)
#write_to_txt('CompleteList.txt', lines)
#print(lines)

# - 1237-1502  part of the mongol empire
# - Dominated the western steppes from 1054-1236  
# - In 1236-1240 themongols conquered both the Russians and Kipchak Turks building an empire called the Golden Horde  
# - In 1257 the Golden Horde converted to Sunni Islam  

# ##Next time: split the lines to get the numbers, then order the lines by the numbers. 
# string = '- Babur 1530-1526' 
# string = string.split('-')

# for word in string:
#     print(search_dates(word,settings={'PREFER_DAY_OF_MONTH': 'first','PREFER_MONTH_OF_YEAR': 'first'}))





# #split on TH, take the list substring and do :(str-1) * 100