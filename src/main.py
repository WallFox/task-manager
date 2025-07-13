import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QListWidget

class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de tareas")
        self.setGeometry(100,100,400,300)
        
        # Widget principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Input para nueva tarea
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Nueva tarea")
        
        # Boton para agregar
        add_button = QPushButton("Agregar")
        add_button.clicked.connect(self.add_task)
        
        # Lista de tareas
        self.task_list = QListWidget()
        
        # Agregar todo al layout
        layout.addWidget(self.task_input)
        layout.addWidget(add_button)
        layout.addWidget(self.task_list)
        
    def add_task(self):
        task_text = self.task_input.text()
        if task_text:
            self.task_list.addItem(task_text)
            self.task_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManager()
    window.show()
    sys.exit(app.exec())