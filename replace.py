import re

with open('Michael_Jackson.mscx', 'r') as f:
    s = f.read()
    pattern = re.compile("<StaffText>.*?<\/StaffText>", re.DOTALL)
    s = re.sub(pattern, '', s)
    print(len(re.findall(pattern, s)))
    with open('Michael_Jackson1.mscx', 'w') as f1:
        f1.write(s)
