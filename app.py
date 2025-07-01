import pyttsx3
import os

# Diccionario con títulos como nombre de archivo y el texto como contenido
audios = {
    "Código fuente - Source Code": "Human-readable instructions written in a programming language. It is the base from which programs are built and can be compiled or interpreted to create executable software.",
    "Compilador - Compiler": "A tool that translates source code into machine code or bytecode. It checks for syntax errors and transforms high-level instructions into a format the computer can execute.",
    "Depuración - Debugging": "The process of identifying, analyzing, and fixing bugs or errors in code. It's essential for ensuring software reliability and is often done using specialized tools or IDEs.",
    "Variable - Variable": "A named memory location used to store data that can change during program execution. Variables are fundamental for logic, flow control, and data manipulation.",
    "Función - Function": "A reusable block of code that performs a specific task. Functions help break programs into smaller, manageable parts, improving readability, reuse, and testing.",
    "Objeto - Object": "An instance of a class that encapsulates data (attributes) and behavior (methods). Objects are central to object-oriented programming and model real-world entities.",
    "Clase - Class": "A blueprint for creating objects, defining their structure and behavior. Classes support encapsulation, inheritance, and abstraction in object-oriented programming.",
    "Interfaz gráfica - Graphical User Interface (GUI)": "Visual components like buttons, windows, and icons that allow users to interact with software. It enhances usability by providing intuitive controls.",
    "Algoritmo - Algorithm": "A precise sequence of steps to solve a specific problem or perform a task. Algorithms are the foundation of programming logic and performance optimization.",
    "Estructura de datos - Data Structure": "A specific way to organize, manage, and store data for efficient access and modification. Examples include arrays, lists, stacks, and trees.",
    "Base de datos - Database": "A structured collection of data, often managed by a DBMS. It allows for efficient storage, retrieval, and manipulation of large volumes of information.",
    "API - API (Application Programming Interface)": "A set of rules and functions that allow different software components to communicate. APIs enable integration between systems and abstraction of complex operations.",
    "Framework - Framework": "A pre-built structure of tools, libraries, and conventions that simplifies software development. Frameworks provide a foundation to build scalable and maintainable applications.",
    "Biblioteca - Library": "A collection of reusable code routines and functions that solve common problems. Libraries save time by offering tested and optimized functionality.",
    "Repositorio - Repository": "A centralized location where code, documentation, and resources are stored. Often used with version control systems like Git to manage development history.",
    "Control de versiones - Version Control": "A system that records changes to code over time, allowing developers to track revisions, revert changes, and collaborate efficiently.",
    "IDE - IDE (Integrated Development Environment)": "A software application that provides tools like a code editor, debugger, and compiler in one place. It improves development speed and code quality.",
    "Commit - Commit": "An action in version control that saves a snapshot of the current code. Each commit includes a message describing the changes and helps track development progress.",
    "Pull request - Pull Request": "A method for proposing changes in a codebase, typically reviewed by peers before merging. Pull requests help maintain code quality and encourage collaboration.",
    "Branch - Branch": "A separate version of the codebase where developers can add features or fix bugs without affecting the main code. Branching enables parallel development.",
    "Bug - Bug": "A defect or error in software that causes incorrect or unintended behavior. Bugs must be identified and fixed during testing or debugging.",
    "Refactorización - Refactoring": "The process of restructuring existing code without changing its external behavior. It improves readability, maintainability, and performance.",
    "Testing - Testing": "The process of evaluating software to ensure it meets requirements and functions correctly. Includes unit tests, integration tests, and user acceptance tests.",
    "CI/CD - CI/CD (Continuous Integration/Continuous Deployment)": "A DevOps practice that automates code integration, testing, and deployment. It helps detect errors early and deliver updates faster.",
    "Documentación - Documentation": "Written descriptions that explain code usage, structure, and design. It helps developers understand, use, and maintain the software over time."
}

# Inicializa pyttsx3
engine = pyttsx3.init()
 
# Configura una voz en inglés si está disponible
voices = engine.getProperty('voices')
for voice in voices:
    if "english" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Asegura la carpeta de salida

# Genera los audios
for titulo, texto in audios.items():
    filename = f"{titulo}.mp3".replace(":", "").replace("/", "-")
    print(f"Creando: {filename}")
    engine.save_to_file(texto, filename)

engine.runAndWait()
print("✅ Audios generados.")
