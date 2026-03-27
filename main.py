import os
import random
import time

class Student:
    #创建数据类，用来储存学生的相关信息
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
        return f"学号{self.serial_number},姓名：{self.name}, 性别：{self.gender}, 班级：{self.class_name}, 学号：{self.student_id}, 学院：{self.college}"

class ExamSystem:
    #创建考场系统
    def __init__(self, data_file):#data_file=“.txt文件名”
        self.students = []
        self.data_file = data_file
        # 启动时自动加载数据
        self.load_data()

    @staticmethod
    def validate_student_id(student_id):
        return student_id.isdigit()

#从文本中读取学生信息
    def load_data(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            if len(lines) <= 1:
                print("警告：文件内容为空或仅有表头，无有效数据。")
                return

            lines = lines[1:]#防止读取数据时将表头当成学生信息

            for line in lines:
                parts = line.strip().split()#以空格分割
                if len(parts) >= 5:
                    # 文件格式为：序号 姓名 性别 班级 学号 学院
                    serial_number=parts[0]
                    name = parts[1]
                    gender = parts[2]
                    class_name = parts[3]
                    student_id = parts[4]
                    college = parts[5]
                    
                    student = Student(serial_number, name, gender, class_name, student_id, college)
                    self.students.append(student)
                else:
                    print(f"警告：跳过格式错误的行 -> {line.strip()}")#如果格式有问题就跳过
                    
            print(f"成功加载 {len(self.students)} 名学生信息。")

        except FileNotFoundError:
            print(f"错误：找不到文件 '{self.data_file}'，请确认文件路径是否正确。")
        except Exception as e:
            print(f"发生未知错误：{e}")


#学号查找学生信息
    def find_student(self, target_id):
        if not self.validate_student_id(target_id):
            print("输入错误：学号必须为数字。")
            return

        found = False
        for student in self.students:
            if student.student_id == target_id:
                print("找到学生信息：")
                print(student)
                found = True
                break
        
        if not found:
            print(f"未找到学号为 {target_id} 的学生。")

#随机点名系统
    def random_roll_call(self, count_str):
        pass

#生成考场安排表
    def generate_seating_chart(self):
        pass

#生成准考证文件
    def generate_admission_tickets(self, seated_students):
        pass

def main():
     data_file = "人工智能编程语言学生名单.txt"
     system = ExamSystem(data_file)
#按照需求选择1-5
     while True:
        print("\n=== 学生信息与考场管理系统 ===")
        print("1. 查询学生信息")
        print("2. 随机点名")
        print("3. 生成考场安排表")
        print("4. 生成准考证")
        print("5. 退出")

        choice = input("请选择功能 (1-5): ")

        if choice == '1':
            sid = input("请输入要查询的学号: ")
            system.find_student(sid)
        elif choice == '2':
            num = input("请输入需要点名的学生数量: ")
            system.random_roll_call(num)
        elif choice == '3':
            system.generate_seating_chart()
        elif choice == '4':
            print("提示：生成准考证需要先有考场安排。正在临时生成座位数据...")
            seated = system.generate_seating_chart()
            if seated:
                system.generate_admission_tickets(seated)
        elif choice == '5':
            print("退出系统。")
            break
        else:
            print("无效的选择，请重新输入。")