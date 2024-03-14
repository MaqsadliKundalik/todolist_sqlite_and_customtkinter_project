import customtkinter
import sqlPrompts

root = customtkinter.CTk()
root.title("To Do List")
root.geometry("1000x600")
def close_program():
    sqlPrompts.close_db()
    root.destroy()

def add_item():
    sqlPrompts.add_item(
        create_item_title.get(),
        create_item_description.get()
    )
    refresh_items()

def del_item(id):
    sqlPrompts.del_item(id)
    refresh_items()

def refresh_items():
    global todolist
    data = sqlPrompts.get_items()
    todolist.grid_forget()
    todolist = customtkinter.CTkFrame(main)

    if data:
        for i in data:
            todo_item = customtkinter.CTkFrame(todolist)
            todo_item_title = customtkinter.CTkLabel(todo_item, text=i[1])
            todo_item_description = customtkinter.CTkLabel(todo_item, text=i[2])
            todo_item_del = customtkinter.CTkButton(todo_item, text="Del", command=lambda : del_item(i[0]))

            todo_item.pack(padx=10, pady=10)
            todo_item_title.grid(row=0, column=0, padx=10, pady=10)
            todo_item_description.grid(row=1, column=0, pady=10, padx=10)
            todo_item_del.grid(row=0, rowspan=2, column=1, padx=10, pady=10)

    else:
        emptyLabel = customtkinter.CTkLabel(todolist, text="List is empty")
        emptyLabel.pack(pady=180, padx=200)    
    
    todolist.grid(row=0, column=1)


root.protocol("WM_DELETE_WINDOW", close_program)

header_title = customtkinter.CTkLabel(root, text="To Do List", font=("Arial", 30, "bold"))

main = customtkinter.CTkFrame(root)

# create
create = customtkinter.CTkFrame(main)

create_title = customtkinter.CTkLabel(create, text="Add item", font=("arial", 30, "bold"))
create_item_title_definition = customtkinter.CTkLabel(create, text="Sarlavhani kiriting.")
create_item_title = customtkinter.CTkEntry(create, width=200)
create_item_description_definition = customtkinter.CTkLabel(create, text="Qo'shimchani kiriting.")
create_item_description = customtkinter.CTkEntry(create, width=200, height=100) 
create_item_send = customtkinter.CTkButton(create, text="Yuborish", command=add_item)



todolist = customtkinter.CTkFrame(main)
refresh_items()



# pack and grid
header_title.pack()
main.pack()
create.grid(row=0, column=0)
todolist.grid(row=0, column=1)

create_title.pack(pady=30)
create_item_title_definition.pack()
create_item_title.pack(pady=(0, 30))
create_item_description_definition.pack()
create_item_description.pack(pady=(0, 30), padx=50)
create_item_send.pack(pady=(0, 30))

root.mainloop()