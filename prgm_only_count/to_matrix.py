import os
TREE_FILE = ['LTree'] #如果一个文件的文件名包含该列表中任意一个字符串，那么该文件就会被自动裁剪（去掉第1行和前3列）
TARGET_FILE = TREE_FILE + ['MCS']#如果一个文件的文件名包含该列表中任意一个字符串，那么该文件就会被转换成矩阵并加入计算队列
'''
例如：
TREE_FILE = ['LTree'，'MTree','Mj9a']
TARGET_FILE = TREE_FILE + ['MCS','MMCCSS','hd8q1']
那么包含'LTree'，'MTree','Mj9a','MCS','MMCCSS','hd8q1'中任意一个字符串的的文件名，比如‘A2_Mj9a_qq.txt’，‘828MMCCSSpp12.txt’,都会加入矩阵转换队列
此外，包含'LTree'，'MTree','Mj9a'中任意一个字符串的的文件名，比如‘TEST_LTree_27278.txt’,‘DIQ782MTree99.txt’,这些文件都会被自动进行数据裁剪（去掉第1行和前3列）
'''
def is_target_file(fname):
    for t in TARGET_FILE:
        if t in fname:
            return True
    return False
def is_tree_file(fname):
    for t in TREE_FILE:
        if t in fname:
            return True
    return False

def str_num(string):
    vec = string.split(' ')
    for i in range(len(vec)):
        vec[i] = int(vec[i])
    return vec
def str_num_cut(string):
    vec = string.split(' ')
    for i in range(len(vec)):
        vec[i] = int(vec[i])
    vec = vec[3:]
    return vec

#指定benchmark哪些文件被测
def is_target_file(fname):
    target_class = '2670'
    target_fname = [
        '138',
        '042',
        '064',
        '081',
        '013',
        '099',
        '030',
        '054',
        '140',
        '112'
    ]
    for tf in target_fname:
        if target_class in fname and tf in fname :
            return True
    return  False

print(os.getcwd())
filenames = os.listdir('./')
print(filenames)

for fname in filenames:
    if is_target_file(fname):
        continue
    if os.path.isdir(fname):
        continue
    if not is_target_file(fname):
        continue
    col_cnt = 0#the max column value in current file
    with open(fname, 'r') as f:


        lines = f.readlines()
        print(fname, f.readlines())
        line_cnt = 0# the lines count in current file
        data = []
        '''
        decide matrix transfer method
        '''
        if is_tree_file(fname):
            first = False
            for l in lines:
                # l = l[0:-1]  # cut the \n
                if not first:
                    first = True
                    continue
                print(l, end='')
                l = l.strip()
                if not l.strip() == "":  # avoid empty line
                    line_cnt += 1
                    data.append(str_num_cut(l))
                    col_cnt = max(data[-1])
        else:
            for l in lines:
                #l = l[0:-1]  # cut the \n
                print(l, end='')
                l = l.strip()
                if not l.strip() == "":  # avoid empty line
                    line_cnt += 1
                    data.append(str_num(l))
                    col_cnt = max(data[-1])
        print("line cnt = ", line_cnt)
        print("col_cnt = ", col_cnt)

    # write the matrix transformed
    if not os.path.exists("MCS_Matrix"):
        os.mkdir("MCS_Matrix")
    file_matrix = open("MCS_Matrix\\"+fname[:-4]+"_Matrix.txt", 'w')
    file_matrix.write(str(col_cnt)+' ')
    file_matrix.write(str(line_cnt)+'\n')
    for i in range(line_cnt):
        for j in range(col_cnt):
            if (j+1) in data[i]:
                file_matrix.write("1 ")
            else:
                file_matrix.write("0 ")
        file_matrix.write("x\n")
    file_matrix.close()
