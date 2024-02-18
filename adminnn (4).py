
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import csv

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSignal

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    def mousePressEvent(self, event):
        self.clicked.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Learning System')
        self.setGeometry(0, 0, 2000, 1000)

        self.content_widgets = {
            "Home": Home(),
            "Admin": Admin(),
            "Classes": Classes(),
            "Students": Students(),
            "Stuff": Stuff()
        }
        
        self.UiComponents()
        self.show()
        self.show_content("Home")

    def UiComponents(self):
        layout = QHBoxLayout()
        
        
        

        navbar = QWidget()
        
        

        self.home_label = ClickableLabel("Home", navbar)
        self.home_label.clicked.connect(lambda: self.show_content("Home")) 
        self.home_label.setFont(QFont("Broadway", 25))
        self.home_label.move(80,170)
        self.home_label.setStyleSheet("color: #E1D7EB")
        
    


        
        
        self.admin_label = ClickableLabel("Admin", navbar)
        self.admin_label.clicked.connect(lambda: self.show_content("Admin")) 
        self.admin_label.setFont(QFont("Broadway", 25))
        self.admin_label.move(80,250)
        self.admin_label.setStyleSheet("color: #E1D7EB")
        
       
        
    
        self.classes_label = ClickableLabel("Classes", navbar)
        self.classes_label.clicked.connect(lambda: self.show_content("Classes"))
        self.classes_label.setFont(QFont("Broadway", 25))
        self.classes_label.move(80,330)  
        self.classes_label.setStyleSheet("color: #E1D7EB")
        

        self.students_label = ClickableLabel("Students", navbar)
        self.students_label.clicked.connect(lambda: self.show_content("Students"))  
        self.students_label.setFont(QFont(" Broadway", 25))
        self.students_label.move(80,410)
        self.students_label.setStyleSheet("color: #E1D7EB")
        

        self.stuff_label = ClickableLabel("Staff", navbar)
        self.stuff_label.clicked.connect(lambda: self.show_content("Staff"))  
      
        self.stuff_label.setFont(QFont("Broadway", 25))
        self.stuff_label.move(80,490)
        self.stuff_label.setStyleSheet("color: #E1D7EB")
        
        

        
      



        
        
        
       



    
        navbar.setStyleSheet("background-color: #492971")
        pic1 = QPixmap("images/home.png")  # Replace "image.jpg" with your image file path
        pic1_label=QLabel(navbar)
        pic1_label.setPixmap(pic1.scaled(50, 50)) 
        pic1_label.move(10,170)

        pic2 = QPixmap("images/admin.png")
        pic2_label = QLabel(navbar)
        pic2_label.setPixmap(pic2.scaled(50, 50)) 
        pic2_label.move(10,250)

        pic3 = QPixmap("images/classes.png")
        pic3_label = QLabel(navbar)
        pic3_label.setPixmap(pic3.scaled(50, 50)) 
        pic3_label.move(10,330)

        pic4 = QPixmap("images/students.png")
        pic4_label = QLabel(navbar)
        pic4_label.setPixmap(pic4.scaled(50, 50)) 
        pic4_label.move(10,410)

        pic5 = QPixmap("images/staff.png")
        pic5_label = QLabel(navbar)
        pic5_label.setPixmap(pic5.scaled(50, 50)) 
        pic5_label.move(10,490)
        
        layout.addWidget(navbar, 1)
        
        


        

        self.page = QWidget()
        self.page.setStyleSheet("background-color: white")
        layout.addWidget(self.page, 5)



        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.content_layout = QVBoxLayout(self.page)
        self.current_content = None
      

    def show_content(self, content):
        if self.current_content == content:
            return

        self.clear_content_layout()
        content_widget = self.content_widgets.get(content)
        if content_widget:
            self.content_layout.addWidget(content_widget)
            content_widget.show()

        self.current_content = content

    def clear_content_layout(self):
     if self.content_layout.count() > 0:
        item = self.content_layout.takeAt(0)
        widget = item.widget()
        widget.hide()

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Home Page", self)
        self.label.setStyleSheet("font-size: 50px; color:#492971")
        self.label1 = QLabel("Additional Content", self)
        self.label1.setStyleSheet("background-color: #eadade;")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.label1)

class Admin(QWidget):
    def __init__(self):
        super().__init__()
        self.UiComponents()

    def UiComponents(self):
        self.title = QLabel("Admins", self)
        self.title.setFont(QFont("Broadway"))
        self.title.setStyleSheet("font-size: 60px; color:#492971")
        self.title.setGeometry(70, 40, 300, 100)
      
        self.searchbar = QLineEdit(self)
        self.searchbar.setPlaceholderText("Search")
        
        self.searchbar.setStyleSheet(
            "border-radius : 20px; background-color: #F0EEFA; color: #536e8f; padding-left: 20px ; padding-right:30px ;font-size: 15px"
        )
        self.searchbar.setGeometry(600,75,200,40)
        
        
       

        
        
      


        box=QLabel(self)
        
        box.setGeometry(30, 250, 870, 300)
        box.setStyleSheet("background-color:#F0EEFA; border-radius : 15px;")
    
        pic6 = QPixmap("images/for_admin.png")
        pic6_label = QLabel(box)
        pic6_label.setPixmap(pic6.scaled(200, 200)) 
        pic6_label.move(10,10)
        self.content_label1=QLabel("Manage the data by exporting and importing\nCSV files from here!",box)
        self.content_label1.setFont(QFont("Broadway"))
        self.content_label1.setStyleSheet("font-size: 25px; color:black ;")
        self.content_label1.move(210,50)


        self.exporting_csv=QPushButton("Export",box)
        self.importing_csv=QPushButton("Import",box)
        self.importing_csv.setGeometry(250,150,150,40)
        self.exporting_csv.setGeometry(500,150,150,40)
        self.exporting_csv.setStyleSheet("border-radius : 15px; background-color:#492971 ; color: #D2C3E1;")
        self.importing_csv.setStyleSheet("""
                                border-radius: 15px;
                                background-color: #492971;
                                color: #D2C3E1;
                            }
                            QPushButton:hover {
                                background-color: #D2C3E1;color: #492971;
                            }
                            """)
        self.exporting_csv.setStyleSheet("""
                                border-radius: 15px;
                                background-color: #492971;
                                color: #D2C3E1;
                            }
                            QPushButton:hover {
                                background-color: #D2C3E1;color: #492971;
                            }
                            """)
        self.importing_csv.setFont(QFont("Arial", 15))
        self.exporting_csv.setFont(QFont("Arial", 15))
        self.importing_csv.clicked.connect(self.open_file_dialog)
        
        
        
        headertabel = QTableWidget(self)
        headertabel.setColumnCount(3)
        headertabel.setRowCount(1)
        headertabel.setItem(0,0, QTableWidgetItem("Admin ID"))
        headertabel.setItem(0,1, QTableWidgetItem("Admin Name"))
        headertabel.setItem(0,2, QTableWidgetItem("Admin Username"))
       

        headertabel.setFont(QFont("arial", 12))
        headertabel.setGeometry(30, 630, 870, 50)
        
        
        


        headertabel.setStyleSheet("QTableWidget { border: 0px; color:black  ; background-color:#FAEEFA  ; border-radius : 20px;}")
        headertabel.horizontalHeader().setVisible(False)
        headertabel.verticalHeader().setVisible(False)
        headertabel.setShowGrid(False)
        headertabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        

        tableWidget = QTableWidget(self)
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(3)
        tableWidget.setItem(0,0, QTableWidgetItem("11067"))
        tableWidget.setItem(0,1, QTableWidgetItem("Shahd Ahmed Ragab"))
        tableWidget.setItem(1,0, QTableWidgetItem("14675"))
        tableWidget.setItem(1,1, QTableWidgetItem("Hassnaa hussam"))
        tableWidget.setItem(2,0, QTableWidgetItem("14789"))
        tableWidget.setItem(2,1, QTableWidgetItem("Ayat Tarek"))
        tableWidget.setItem(3,0, QTableWidgetItem("10923"))
        tableWidget.setItem(3,1, QTableWidgetItem("Eman Abd El-Azeem"))

        tableWidget.setItem(0,2, QTableWidgetItem("shahdd"))
        tableWidget.setItem(1,2, QTableWidgetItem("hasnaa4"))
        tableWidget.setItem(2,2, QTableWidgetItem("Ayatt"))
        tableWidget.setItem(3,2, QTableWidgetItem("Eman304"))
       

        tableWidget.setFont(QFont("Arial", 12))
        tableWidget.horizontalHeader().setVisible(False)
        tableWidget.verticalHeader().setVisible(False)
        tableWidget.setShowGrid(False)
       


        # Table will fit the screen horizontally
        tableWidget.setGeometry(30, 700, 870, 200)
        tableWidget.setStyleSheet("QTableWidget { border: 0px; background-color:#FAEEFA; color: black ; border-radius : 15px;}")
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

     


    def open_file_dialog(self):
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            file_dialog.setNameFilter("All Files (*.*)")  # You can set specific file filters here
            if file_dialog.exec_():
                selected_files = file_dialog.selectedFiles()
                for file_path in selected_files:
                    # Process the selected file
                    self.process_file(file_path)
                        
                    for row in file_path:
                         print(row)

    def process_file(self, file_path):
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    file_path.append(row)
            return file_path

        
  
                
        
        
        
       

       

class Classes(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Classes Page", self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


        # more Font
        QFontDatabase.addApplicationFont("./ProtestRiot-Regular.ttf")
        QFontDatabase.addApplicationFont("./Exo2-Regular.ttf")
        QFontDatabase.addApplicationFont("./Exo2-SemiBold.ttf")
        self.setWindowTitle("Classes ")
        self.setStyleSheet("background-color:  #5558AC; border-radius:40px;")
        self.UiComponents()


    def UiComponents(self):
        # back ground
        back_ground = QLabel(self)
        back_ground.setStyleSheet(
            "background-color: #F9F8FD; border-radius:30px; margin:15px "
        )
        back_ground.setGeometry(0, 0, 1620, 994)

        self.showAddedCourse("Data Structures & Algorithms", "CMP 2210",110,355)
        self.showAddedCourse("Database", "CMP 2242", 110, 470)
        self.showAddedCourse("Chemistry", "CHE 1241", 110, 585)
        self.showAddedCourse("Circuits", "EPE 1241", 110, 700)
        self.showAddedCourse("OOP Principles", "CMP 1242", 110, 815)

        self.showAddedCourse("Linear Algebra", "MTH 1242", 890,355)
        self.showAddedCourse("Elctronics", "ELC 2242", 890, 470)
        self.showAddedCourse("Bio-Measurements", "SBE 2230", 890, 585)
        self.showAddedCourse("Bio-Statistics", "SBE 2240", 890, 700)
        self.showAddedCourse("Fluids & Thermo Dynamics", "MEC 102", 890, 815)

        self.hello("Hassnaa")

        # # the side bar
        # side_bar = QLabel(self)
        # side_bar.setStyleSheet("background-color: #5558AC; ")
        # side_bar.setGeometry(0, 0, 300, 1000)

        # courses word label
        courses_label = QLabel(self)
        courses_label.setText("Courses")
        courses_label.setFont(QFont("Protest Riot", 25))
        courses_label.setStyleSheet("color: rgba(63,71,105); background-color:#F9F8FD")
        courses_label.resize(500, 60)
        courses_label.move(80,270)
        courses_label.setBold = True

        # search textbox
        searchBox = QLineEdit(self)
        searchBox.setPlaceholderText("Search")
        searchBox.setFont(QFont("Arial", 12))
        searchBox.setGeometry(1250,95,280, 40)
        searchBox.setStyleSheet(
            "border-radius : 10px; background-color: #EDE1F7; color: black; padding-left: 55px"
        )

        # search icon
        search_label = QLabel(self)
        pixmap = QPixmap("images/icons8-search-30.png")
        search_label.setPixmap(pixmap)
        search_label.move(970,100)
        search_label.resize(30, 30)
        search_label.setStyleSheet("background-color: transparent;")

        # number of courses
        num_label = QLabel(self)
        num_label.setText("Courses \ncompleted")
        num_label.setFont(QFont("Arial", 14))
        num_label.move(950,160)
        num_label.resize(280, 120)
        num_label.setStyleSheet(
            "border-radius : 10px; background-color: #EDE1F7;padding-left:125px;"
        )
        num10_label = QLabel(self)
        num10_label.setText("10")
        num10_label.setFont(QFont("Protest Riot", 60))
        num10_label.move(970,160)
        num10_label.resize(120, 100)
        num10_label.setStyleSheet("background-color: transparent;")

        # courses in progress
        inprogress_label = QLabel(self)
        inprogress_label.setText("Courses \nin progress")
        inprogress_label.setFont(QFont("Arial", 14))
        inprogress_label.move(1250,160)
        inprogress_label.resize(280, 120)
        inprogress_label.setStyleSheet(
            "border-radius : 10px; background-color: #EDE1F7; padding-left:125px;"
        )
        num4_label = QLabel(self)
        num4_label.setText("4")
        num4_label.setFont(QFont("Protest Riot", 60))
        num4_label.move(1290,160)
        num4_label.resize(120, 100)
        num4_label.setStyleSheet("background-color: transparent;")


    def showAddedCourse(self, name, code, x, y):
        # rectangle of course
        course_rect = QLabel(self)
        course_rect.setStyleSheet("background-color: #F4F4FE; border-radius : 15px; ")
        course_rect.resize(640, 90)
        course_rect.move(x, y)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        course_rect.setGraphicsEffect(shadow)

        # course name
        course_name = QLabel(self)
        course_name.setText(f"{name}\n")
        course_name.setFont(QFont("Exo2", 15))
        course_name.setStyleSheet("background-color: transparent; ")
        course_name.resize(400, 50)
        course_name.move(x + 20, y + 17)
        course_name.setBold = True

        # course code
        course_code = QLabel(self)
        course_code.setText(f"{code}\n")
        course_code.setFont(QFont("Exo2", 10))
        course_code.setStyleSheet("background-color: transparent; ")
        course_code.resize(100, 50)
        course_code.move(x + 20, y + 51)

        # view course button
        view_btn = QPushButton(self)
        view_btn.setText(" View Course")
        view_btn.setFont(QFont("Exo2", 12))
        view_btn.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #393984;"
            "};background-color: #5558AC; border-radius : 15px; padding: 10px; color:white;  "
        )
        view_btn.resize(160, 50)
        view_btn.move(x + 420, y + 20)
        view_btn.setCursor(Qt.PointingHandCursor)

        match code:
            case "CMP 2210":
                self.code1 = "CMP 2210"
                view_btn.clicked.connect(self.showCourse1)
            case "CMP 2242":
                self.code2 = "CMP 2242"
                view_btn.clicked.connect(self.showCourse2)
            case "CHE 1241":
                view_btn.clicked.connect(self.showCourse3)
            case "EPE 1241":
                view_btn.clicked.connect(self.showCourse4)
            case "CMP 1242":
                view_btn.clicked.connect(self.showCourse5)
            case "MTH 1242":
                view_btn.clicked.connect(self.showCourse6)
            case "ELC 2242":
                view_btn.clicked.connect(self.showCourse7)
            case "SBE 2230":
                view_btn.clicked.connect(self.showCourse8)
            case "SBE 2240":
                view_btn.clicked.connect(self.showCourse9)
            case "MEC 102":
                view_btn.clicked.connect(self.showCourse10)
        # view_btn.clicked.connect(self.showCourse)

    def showCourse1(self):
        # dialog appear when button is clicked
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        # tabel contains basic info
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        # tabel content
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Data Structures & Algorithms"))
        info_tabel.setItem(1, 1, QTableWidgetItem("CMP 2210"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3201"))
        info_tabel.setItem(3, 1, QTableWidgetItem("10 Am"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            " background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        # adding tabel to dialog
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse2(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Database"))
        info_tabel.setItem(1, 1, QTableWidgetItem("CMP 2242"))
        info_tabel.setItem(2, 1, QTableWidgetItem("14200"))
        info_tabel.setItem(3, 1, QTableWidgetItem("8 Am"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse3(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Chemistry"))
        info_tabel.setItem(1, 1, QTableWidgetItem("CHE 1241"))
        info_tabel.setItem(2, 1, QTableWidgetItem("17102"))
        info_tabel.setItem(3, 1, QTableWidgetItem("12 pm"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse4(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Circuits"))
        info_tabel.setItem(1, 1, QTableWidgetItem("EPE 1241"))
        info_tabel.setItem(2, 1, QTableWidgetItem("1125"))
        info_tabel.setItem(3, 1, QTableWidgetItem("1 pm"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse5(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("OOP Principles"))
        info_tabel.setItem(1, 1, QTableWidgetItem("CMP 1242"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3102"))
        info_tabel.setItem(3, 1, QTableWidgetItem("8 Am"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse6(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Linear Algebra"))
        info_tabel.setItem(1, 1, QTableWidgetItem("MTH 1242"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3202"))
        info_tabel.setItem(3, 1, QTableWidgetItem("10 Am"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse7(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Elctronics"))
        info_tabel.setItem(1, 1, QTableWidgetItem("ELC 2242"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3201"))
        info_tabel.setItem(3, 1, QTableWidgetItem("10:30 Am"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse8(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Bio-Measurements"))
        info_tabel.setItem(1, 1, QTableWidgetItem("SBE 2230"))
        info_tabel.setItem(2, 1, QTableWidgetItem("1204"))
        info_tabel.setItem(3, 1, QTableWidgetItem("12 pm"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse9(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Bio-Statistics"))
        info_tabel.setItem(1, 1, QTableWidgetItem("SBE 2240"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3103"))
        info_tabel.setItem(3, 1, QTableWidgetItem("2 pm"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse10(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(800, 500)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(600, 800)
        info_tabel.move(500, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6)
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        info_tabel.setItem(5, 0, QTableWidgetItem("Students"))
        info_tabel.setItem(5, 1, QTableWidgetItem("Grade"))
        info_tabel.setItem(0, 1, QTableWidgetItem("Fluids & Thermo Dynamics"))
        info_tabel.setItem(1, 1, QTableWidgetItem("MEC 102"))
        info_tabel.setItem(2, 1, QTableWidgetItem("17102"))
        info_tabel.setItem(3, 1, QTableWidgetItem("8 Am"))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def hello(self, name):
        # hello label
        hello_label = QLabel(self)
        hello_label.resize(800, 150)
        hello_label.setStyleSheet(
            "background-color: #EDE1F7; border-radius:20px; padding-left:25px; padding-top:15px  "
        )
        hello_label.move(110,95)
        hello_label.setText(f"Hello {name}!\n")
        hello_label.setFont(QFont("Protest Riot", 28))

        # It's good to see you again label
        label2 = QLabel(self)
        label2.resize(300, 150)
        label2.move(80, 123)
        label2.setText(" It's good to see you again.")
        label2.setFont(QFont("Protest Riot", 14))
        label2.setStyleSheet(
            "background-color: transparent; border-radius:20px; padding-left:25px;margin-top:0px ;"
        )

        # image label
        img_label = QLabel(self)
        img_label.resize(200, 210)
        img_label.move(880, 35)
        img_label.setStyleSheet(
            "background-color: transparent; margin:0px; padding:0px"
        )
        pixmap = QPixmap("images/student1.png")
        img_label.setPixmap(pixmap)




class Students(QWidget):
    def __init__(self):
        super().__init__()
        self.UiComponents()

        self.setWindowTitle("Students ")

        self.setStyleSheet("background-color: #5558AC;")



    def UiComponents(self):

        # for corners

        pinkLabel = QLabel(self)
        pinkLabel.setStyleSheet("border-radius : 50px; background-color: white;")
        pinkLabel.setGeometry(0,8, 1200, 975)

        pinkLabel2 = QLabel(self)
        pinkLabel2.setStyleSheet("border-radius : 50px; background-color: #F9F8FD;")
        pinkLabel2.setGeometry(1100,8, 550, 975)


        # student word label

        studentWordLabel = QLabel(self)
        studentWordLabel.setText("Students")
        studentWordLabel.setFont(QFont("Exo2", 25))
        studentWordLabel.setStyleSheet("background-color: transparent; color: #867FE0;")
        studentWordLabel.setGeometry(380, 40, 400, 60)


        # statistic word label

        statisticWordLabel = QLabel(self)
        statisticWordLabel.setText("Statistics")
        statisticWordLabel.setFont(QFont("Exo2", 25))
        statisticWordLabel.setStyleSheet("background-color: transparent;  color: #867FE0;")
        statisticWordLabel.setGeometry(1550, 40, 400, 60)


        # the two buttons label above

        btLabel = QLabel(self)
        btLabel.setStyleSheet("border-radius : 20px; background-color: #867FE0;")
        btLabel.setGeometry(1200, 130, 105, 40)


        self.filter = QPushButton(self)
        self.filter.setFont(QFont("Protest Riot", 15))
        self.filter.resize(32, 32)
        self.filter.move(1215, 135)
        self.filter.setStyleSheet(
            "border-radius : 10px;background-color:#5C56B0 ;color:white; bold"
        )
        self.filter.setCursor(Qt.PointingHandCursor)
        self.icon = QIcon('icons8-filter-50.png')  # Replace 'icon.png' with the path to your icon file
        self.filter.setIcon(self.icon)
        # self.filter.clicked(self.go_to_anotherWindow())


        self.list = QPushButton(self)
        self.list.setFont(QFont("Protest Riot", 15))
        self.list.resize(32, 32)
        self.list.move(1260, 135)
        self.list.setStyleSheet(
            "border-radius : 10px;background-color: #5C56B0 ;color:white; bold"
        )
        self.list.setCursor(Qt.PointingHandCursor)
        self.icon = QIcon('icons8-list-30.png')  # Replace 'icon.png' with the path to your icon file
        self.list.setIcon(self.icon)


        # add student butten

        addStudent = QPushButton(self)
        addStudent.setText("Add Student")
        addStudent.setFont(QFont("Exo2", 11))
        addStudent.setGeometry(1050, 130, 120, 40)
        addStudent.setStyleSheet("border-radius : 20px; background-color: #867FE0; color: white;")




        # search textbox

        searchBox = QLineEdit(self)
        searchBox.setPlaceholderText("Search")
        searchBox.setFont(QFont('Arial', 12))
        searchBox.move(620, 405)
        searchBox.setGeometry(1050, 70, 280, 40)
        searchBox.setStyleSheet("border-radius : 20px; background-color: #F7ECFC; color: black; padding-left: 20px")


        # the table

        headertabel = QTableWidget(self)
        headertabel.setColumnCount(4)
        headertabel.setRowCount(1)
        headertabel.setItem(0,0, QTableWidgetItem("Student ID"))
        headertabel.setItem(0,1, QTableWidgetItem("Student Name"))
        headertabel.setItem(0,2, QTableWidgetItem("Student Year"))
        headertabel.setItem(0,3, QTableWidgetItem("Student Department"))
        headertabel.resizeRowToContents(4)
        headertabel.setFont(QFont("Times", 10))
        headertabel.setGeometry(340, 250, 1010, 46)
        headertabel.setStyleSheet("QTableWidget { border: 0px; background-color: #F9F8FD; color: #536e8f; border-radius : 20px;}")
        headertabel.horizontalHeader().setVisible(False)
        headertabel.verticalHeader().setVisible(False)
        headertabel.setShowGrid(False)
        headertabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        headertabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        tableWidget = QTableWidget(self)
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(4)
        tableWidget.setItem(0,0, QTableWidgetItem("11067"))
        tableWidget.setItem(0,1, QTableWidgetItem("Shahd Ahmed Ragab"))
        tableWidget.setItem(1,0, QTableWidgetItem("14675"))
        tableWidget.setItem(1,1, QTableWidgetItem("Hassnaa hussam"))
        tableWidget.setItem(2,0, QTableWidgetItem("14789"))
        tableWidget.setItem(2,1, QTableWidgetItem("Ayat Tarek"))
        tableWidget.setItem(3,0, QTableWidgetItem("10923"))
        tableWidget.setItem(3,1, QTableWidgetItem("Eman Abd El-Azeem"))

        tableWidget.setItem(0,2, QTableWidgetItem("second"))
        tableWidget.setItem(1,2, QTableWidgetItem("third"))
        tableWidget.setItem(2,2, QTableWidgetItem("first"))
        tableWidget.setItem(3,2, QTableWidgetItem("fourth"))
        tableWidget.setItem(0,3, QTableWidgetItem("SBE"))
        tableWidget.setItem(2,3, QTableWidgetItem("ARC"))
        tableWidget.setItem(1,3, QTableWidgetItem("CMP"))
        tableWidget.setItem(3,3, QTableWidgetItem("CVE"))
        tableWidget.resizeColumnToContents(10)
        tableWidget.resizeColumnToContents(5)

        tableWidget.setFont(QFont("Times", 10))
        tableWidget.horizontalHeader().setVisible(False)
        tableWidget.verticalHeader().setVisible(False)
        tableWidget.setShowGrid(False)


        # Table will fit the screen horizontally
        tableWidget.setGeometry(340, 310, 1010, 600)
        tableWidget.setStyleSheet("QTableWidget { border: 0px; background-color: #F9F8FD; color: #536e8f; border-radius : 15px;}")
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)






# def go_to_anotherWindow(self):

#self.addstudent = AddStudent()
# self.addstudent.show()
# self.hide()





class Stuff(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Stuff Page", self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

