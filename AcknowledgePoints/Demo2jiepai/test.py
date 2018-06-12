import re
inputStr="hello python,ni hao c,zai jian python"
replaceStr=re.sub(r"hello (\w+),ni hao (\w+),zai jian \1","PHP",inputStr)
print(replaceStr)