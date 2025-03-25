import os

def upload_sprint_document():
    file_path = input("Enter the path to your sprint document: ")

    if os.path.exists(file_path):
        print(f"✅ Sprint document '{file_path}' uploaded successfully!")
    else:
        print("❌ File not found. Please check the path and try again.")

if __name__ == "__main__":
    print("Welcome to SmartSprint: AI-Enhanced Kanban Solution")
    upload_sprint_document()
