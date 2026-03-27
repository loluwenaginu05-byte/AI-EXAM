#何鑫-25361025-第二次人工智能编程作业

Installation：
```bash
#下载代码
    git clone https://github.com/loluwenaginu05-byte/AI-EXAM.git
    cd tltl
    #这里我使用的是ubuntu24.04+python13版本，windows应该是python
    python3 main.py
```

#一、 任务拆解与 AI 协作策略
    系统功能核心分为4个板块：
        1.信息初始化与查找
        2.随机点名
        3.生成考场安排表
        4.生成准考证目录与文件
    
    AI协作策略：
        1.AI帮助我生成创建数据类（用来储存学生的相关信息）与考场系统类两个类函数
        2.AI帮我按照4个功能创建相应函数
        3.创建主函数，调用4个核心功能
        4.补全相应函数功能
        5.生成完成逻辑代码（但有debug）



#二、 核心 Prompt 迭代记录
    初代Prompt：帮我创建一个学生类的代码，读取.txt文件中的信息
    AI 生成的问题/缺陷：代码读取顺序有误，读取内容有缺陷，缺少信息
    优化后的 Prompt：帮我按照序号	姓名	性别	班级	学号	学院的顺序读取学生相关信息（but代码仍然有一些问题，后续人工修改）
```bash
#错误代码！！！
#优化后的代码输出，AI忽略了序号
    def __init__(self, serial_number, name, gender, class_name, student_id, college):#姓名	性别	班级	学号	学院
        # 初始化学生属性
        self.name = name
        self.gender = gender
        self.class_name = class_name
        self.student_id = student_id
        self.college = college

    def __str__(self):
        # 定义函数直接打印学生信息
        return f"姓名：{self.name}, 性别：{self.gender}, 班级：{self.class_name}, 学号：{self.student_id}, 学院：{self.college}"

```

```bash
#人工修改后的代码
    def __init__(self, serial_number, name, gender, class_name, student_id, college):#序号	姓名	性别	班级	学号	学院
        # 初始化学生属性
        self.serial_number=serial_number
        self.name = name
        self.gender = gender
        self.class_name = class_name
        self.student_id = student_id
        self.college = college

    def __str__(self):
        # 定义函数直接打印学生信息
        return f"序号{self.serial_number},姓名：{self.name}, 性别：{self.gender}, 班级：{self.class_name}, 学号：{self.student_id}, 学院：{self.college}"
```



#三、 Debug 与异常处理记录
      1.AI在初次处理时忽略了序号，后续仍然出现此问题：
```bash
    for line in lines:
                    parts = line.strip().split()#以空格分割
                    if len(parts) >= 5:
                        # 文件格式为：姓名 性别 班级 学号 学院
                        name = parts[0]
                        gender = parts[1]
                        class_name = parts[2]
                        student_id = parts[3]
                        college = parts[4]
                        
                        student = Student(serial_number, name, gender, class_name, student_id, college)
```

        2.人工智能编程语言学生名单.txt路径错误：
            初始我将人工智能编程语言学生名单.txt放在main.py文件夹中

```bash
    #AI生成路径
     data_file = " 人工智能编程语言学生名单/人工智能编程语言学生名单.txt"
```

            发现路径报错之后自己调整代码

```
     data_file = "人工智能编程语言学生名单.txt"
```


#四、 人工代码审查
```bash
    #创建函数安排考场函数
    def generate_seating_chart(self):
        #确认数据来源
        if not self.students:
            print("没有学生数据，无法生成考场表。")
            return

        # 复制一份列表并打乱，避免影响原始数据
        shuffled_students = self.students[:]
        random.shuffle(shuffled_students)
        
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        filename = "考场安排表.txt"
        #创建考场安排表.txt文件，将考场安排信息写入
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"生成时间：{current_time}\n")
                f.write("-" * 30 + "\n")
                f.write(f"{'座位号':<10}{'姓名':<10}{'学号':<15}\n")
                f.write("-" * 30 + "\n")
                
                for index, student in enumerate(shuffled_students, 1):
                    f.write(f"{index:<10}{student.name:<10}{student.student_id:<15}\n")
            
            print(f"成功生成考场安排表：{filename}")
            return shuffled_students # 返回打乱后的列表供生成准考证使用
        #返回说明
        except Exception as e:
            print(f"生成考场安排表失败：{e}")
            return None
```