# 如何使用mhs2批处理程序
## 环境
- **确保你已经安装了Python3**
- **确保你已经设置`python`环境变量**

## 如何使用？
- ***本程序的使用非常简单***
- 首先进入测试数据的根目录下，如下图所示
![1.png](https://i.loli.net/2021/05/13/ZCXm3LOYgEkIQqW.png)
注意，你的所有测试数据的格式，都必须是非矩阵格式（程序会自动进行转换）
- 然后复制`./prgm_count_and_write/`下的所有文件至该目录。如下图所示
![11.png](https://i.loli.net/2021/05/13/1ZCmgsc9olBDFvn.png)
- 然后你只需要双击运行`run.bat`文件即可，运行之后的效果如下图所示，该目录下多出一个名为`MCS_Matrix`的文件夹
![2.png](https://i.loli.net/2021/05/13/1EI35yzQthB7LOw.png)
- 进入该文件夹，如果测试数据有个，那么该文件夹内应该有2*n+1个文件，其中n个文件是原测试数据转换成的矩阵文件（后缀名`XX_Matrix.txt`）,另外n个文件是每一个`XX_Matrix.txt`文件对应的结果文件（后缀名为`XX_Matrix_res.txt`）,最后一个文件是最终的统计结果，名为`mhs_clock_res.txt`，包含了每一个计算成功的测试数据信息`|测试数据文件名|计算时间|结果行数|`n
![3.png](https://i.loli.net/2021/05/13/oX6dk5wvaejOSKb.png)
![4.png](https://i.loli.net/2021/05/13/H6poeY9NCEK5k1z.png)

## 其他问题
- 我只想得到纯计算时间，不需要输出结果到文件，如何操作？  

  你只需要复制`./prgm_only_count/`文件夹下的所有文件至测试数据目录即可，其他操作均相同
- 如何指定某些文件进行矩阵转换并计算 ？如何指定某些测试数据文件在矩阵转换之前进行数据裁剪（去掉第1行，前3列）？ 
  - 打开`to_matrix.py`文件，修改第2,3行即可（看2,3行注释）  
  > TREE_FILE = ['LTree'] #如果一个文件的文件名包含该列表中任意一个字符串，那么该文件就会被自动裁剪（去掉第1行和前3列）  
    TARGET_FILE = TREE_FILE + ['MCS']#如果一个文件的文件名包含该列表中任意一个字符串，那么该文件就会被转换成矩阵并加入计算队列  
    例如：  
    TREE_FILE = ['LTree'，'MTree','Mj9a']  
    TARGET_FILE = TREE_FILE + ['MCS','MMCCSS','hd8q1']  
    那么包含'LTree'，'MTree','Mj9a','MCS','MMCCSS','hd8q1'中任意一个字符串的的文件名，比如‘A2_Mj9a_qq.txt’，‘828MMCCSSpp12.txt’,都会加入矩阵转换队列  
    此外，包含'LTree'，'MTree','Mj9a'中任意一个字符串的的文件名，比如‘TEST_LTree_27278.txt’,‘DIQ782MTree99.txt’,这些文件都会被自动进行数据裁剪（去掉第1行和前3列）  
    '''
    
## 需要注意
- 测试数据文件的绝对路径中尽量不要包含中文以及中文字符、特殊符号（@#￥%……&*（）-+=/?空格）等等，尽量只包含`数字、字母和下划线`,也许即使你包含了特殊字也可以正常运行，但是作者无法保证它总是正常运行
