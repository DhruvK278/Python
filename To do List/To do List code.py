import msvcrt
import os
import sys

def move_cursor(row, col):
    print(f"\033[{row};{col}H", end="")

def clear_screen():
    os.system("cls")

def Add_Task():
    clear_screen()
    move_cursor(2, 20)
    print("Enter The Task")
    move_cursor(4, 20)
    print("(Enter to finish)")
    file_name = "Task.txt"
    with open(file_name, "a") as file:
         while True:
            text = input()
            if not text:
                break   
            file.write(text + '\n')
         clear_screen()
         main_screen(user_name)

def completed():
    with open("Task.txt", "r") as file:
        tasks = file.readlines()

    clear_screen()
    move_cursor(2, 20)
    print("Completed Tasks:")
    
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.strip()}")

    move_cursor(len(tasks) + 4, 20)
    print("Enter the task number to delete (or '0' to cancel): ")

    choice = None
    while choice is None:
        try:
            choice = int(msvcrt.getch())
        except ValueError:
            pass

    if choice == 0:
        clear_screen()
        main_screen(user_name)
    elif 1 <= choice <= len(tasks):
        tasks.pop(choice - 1)
        with open("Task.txt", "w") as file:
            file.writelines(tasks)
        completed()  
    else:
        print("Invalid task number.")


def main_screen(user_name):
    move_cursor(2, 20)
    print(f"{user_name}'s To do list!")
    move_cursor(4, 20)
    print("1.Add Task")
    move_cursor(6, 20)
    print("2.completed")
    move_cursor(8, 20)
    print("3.Exit")

def Exit():
    clear_screen()
    sys.exit(0)

user_name = input("Enter your name: ")
clear_screen()
main_screen(user_name)

while True:  
    choice = msvcrt.getch().decode('utf-8')
    if choice == '1':
        Add_Task()
    elif choice == '2':
        completed()
    elif choice == '3':
        Exit()
    else:
        print("Please choose between 1, 2, 3")
