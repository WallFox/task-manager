import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                            QWidget, QPushButton, QLineEdit, QListWidget, 
                            QListWidgetItem, QMessageBox, QInputDialog)
from PyQt6.QtCore import Qt

class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de tareas - CRUD")
        self.setGeometry(100,100,1024,600)
        
        # Widget principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Input para nueva tarea
        input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Escribe una nueva tarea...")
        self.task_input.returnPressed.connect(self.create_task)  # Enter para crear
        
        create_button = QPushButton("Crear Tarea")
        create_button.clicked.connect(self.create_task)
        
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(create_button)
        
        # Lista de tareas
        self.task_list = QListWidget()
        self.task_list.itemDoubleClicked.connect(self.update_task)
        
        # BOTONES CRUD
        button_layout = QHBoxLayout()
        
        update_button = QPushButton("Editar")
        update_button.clicked.connect(self.update_task)
        
        delete_button = QPushButton("Eliminar")
        delete_button.clicked.connect(self.delete_task)
        
        clear_all_button = QPushButton("Limpiar Todo")
        clear_all_button.clicked.connect(self.clear_all_tasks)
        
        button_layout.addWidget(update_button)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(clear_all_button)
        
        # Agregar todo al layout principal
        layout.addLayout(input_layout)
        layout.addWidget(self.task_list)
        layout.addLayout(button_layout)
        
    # CREATE - Crear tarea
    def create_task(self):
        task_text = self.task_input.text().strip()
        if task_text:
            self.task_list.addItem(task_text)
            self.task_input.clear()
            self.show_message("Tarea creada exitosamente")
        else:
            self.show_message("Por favor ingresa una tarea", "warning")
    
    # READ - Las tareas se ven en la lista automáticamente
    
    # UPDATE - Editar tarea
    def update_task(self):
        current_item = self.task_list.currentItem()
        if current_item:
            old_text = current_item.text()
            new_text, ok = QInputDialog.getText(
                self, 
                "Editar Tarea", 
                "Editar tarea:", 
                text=old_text
            )
            
            if ok and new_text.strip():
                current_item.setText(new_text.strip())
                self.show_message("Tarea actualizada exitosamente")
        else:
            self.show_message("Selecciona una tarea para editar", "warning")
    
    # DELETE - Eliminar tarea
    def delete_task(self):
        current_item = self.task_list.currentItem()
        if current_item:
            reply = QMessageBox.question(
                self,
                "Confirmar eliminación",
                f"¿Estás seguro de eliminar la tarea: '{current_item.text()}'?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                row = self.task_list.row(current_item)
                self.task_list.takeItem(row)
                self.show_message("Tarea eliminada exitosamente")
        else:
            self.show_message("Selecciona una tarea para eliminar", "warning")
    
    # Limpiar todas las tareas
    def clear_all_tasks(self):
        if self.task_list.count() > 0:
            reply = QMessageBox.question(
                self,
                "Confirmar limpieza",
                "¿Estás seguro de eliminar TODAS las tareas?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                self.task_list.clear()
                self.show_message("Todas las tareas eliminadas")
        else:
            self.show_message("No hay tareas para eliminar", "info")
    
    # Mostrar mensajes
    def show_message(self, message, msg_type="info"):
        msg_box = QMessageBox()
        
        if msg_type == "warning":
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setWindowTitle("Advertencia")
        elif msg_type == "error":
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setWindowTitle("Error")
        else:
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle("Información")
        
        msg_box.setText(message)
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManager()
    window.show()
    sys.exit(app.exec())