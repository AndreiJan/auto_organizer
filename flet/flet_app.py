import flet as ft
import os
from tkinter import filedialog
import tkinter as tk
import platform 
import json


# JSON file 
# Reads JSON file 
# Contains FOLDERS and more 

with open('./data/data.json', 'r') as f:
    data = json.load(f)
    print(data)


home_dir = os.path.expanduser("~")
downloads_path = os.path.join(home_dir, "Downloads")
def main(page: ft.Page):
    # document_path = ft.Text(value=downloads_path)
    # videos_path = ft.Text(value=downloads_path)
    # installers_path = ft.Text(value=downloads_path)
    # pictures_path = ft.Text(value=downloads_path)
    # miscs_path = ft.Text(value=downloads_path)
    # source_code_path = ft.Text(value=downloads_path)
    # miscs_path = ft.Text(value=downloads_path)
    # zips_path = ft.Text(value=downloads_path)

    # def document_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
    #     # Positions the text
    #     root = tk.Tk()
    #     root.withdraw()
    #     root.wm_attributes('-topmost', 1)
    #     folder = filedialog.askdirectory()
    #     if folder:
    #         document_path.value = f"Selected: {folder}"
    #         print(f"Selected: {folder}")
    #     else:
    #         document_path.value = "Selection cancelled"
    #     page.update()

    # def videos_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
    #     # Positions the text
    #     root = tk.Tk()
    #     root.withdraw()
    #     root.wm_attributes('-topmost', 1)
    #     folder = filedialog.askdirectory()
    #     if folder:
    #         videos_path.value = f"Selected: {folder}"
    #         print(f"Selected: {folder}")
    #     else:
    #         videos_path.value = "Selection cancelled"
    #     page.update()


    # def installers_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
    #     # Positions the text
    #     root = tk.Tk()
    #     root.withdraw()
    #     root.wm_attributes('-topmost', 1)
    #     folder = filedialog.askdirectory()
    #     if folder:
    #         installers_path.value = f"Selected: {folder}"
    #         print(f"Selected: {folder}")
    #     else:
    #         installers_path.value = "Selection cancelled"
    #     page.update()
    # def pictures_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
    #     # Positions the text
    #     root = tk.Tk()
    #     root.withdraw()
    #     root.wm_attributes('-topmost', 1)
    #     folder = filedialog.askdirectory()
    #     if folder:
    #         pictures_path.value = f"Selected: {folder}"
    #         print(f"Selected: {folder}")
    #     else:
    #         pictures_path.value = "Selection cancelled"
    #     page.update()
    # def miscs_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
    #     # Positions the text
    #     root = tk.Tk()
    #     root.withdraw()
    #     root.wm_attributes('-topmost', 1)
    #     folder = filedialog.askdirectory()
    #     if folder:
    #         miscs_path.value = f"Selected: {folder}"
    #         print(f"Selected: {folder}")
    #     else:
    #         miscs_path.value = "Selection cancelled"
    #     page.update()
    # def source_code_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
    #     # Positions the text
    #     root = tk.Tk()
    #     root.withdraw()
    #     root.wm_attributes('-topmost', 1)
    #     folder = filedialog.askdirectory()
    #     if folder:
    #         source_code_path.value = f"Selected: {folder}"
    #         print(f"Selected: {folder}")
    #     else:
    #         source_code_path.value = "Selection cancelled"
    #     page.update()
    
    # def zips_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
    #     # Positions the text
    #     root = tk.Tk()
    #     root.withdraw()
    #     root.wm_attributes('-topmost', 1)
    #     folder = filedialog.askdirectory()
    #     if folder:
    #         zips_path.value = f"Selected: {folder}"
    #         print(f"Selected: {folder}")
    #     else:
    #         zips_path.value = "Selection cancelled"
    #     page.update()
    # page.add(
    #     ft.Text("FILE ORGANIZER", size=24, weight=ft.FontWeight.W_600),
    #     ft.Column([
    #         # Document
    #         ft.Text("Document Files", size=24, weight=ft.FontWeight.W_100),
    #         ft.Row([
    #             ft.Button("Select", on_click=document_folder),
    #             document_path,
    #         ]),           
    #         # Video
    #         ft.Text("Video Files", size=24, weight=ft.FontWeight.W_100),
    #         ft.Row([
    #             ft.Button("Select", on_click=videos_folder),
    #             videos_path,
    #         ]),

    #         # Installer
    #         ft.Text("Installer Files", size=24, weight=ft.FontWeight.W_100),
    #         ft.Row([
    #             ft.Button("Select", on_click=installers_folder),
    #             installers_path,
    #         ]),
            
    #         # Pictures
    #         ft.Text("Pictures Files", size=24, weight=ft.FontWeight.W_100),
    #         ft.Row([
    #             ft.Button("Select", on_click=pictures_folder),
    #             pictures_path,
    #         ]),
            
    #         # Misc
    #         ft.Text("Misc Files", size=24, weight=ft.FontWeight.W_100),
    #         ft.Row([
    #             ft.Button("Select", on_click=miscs_folder),
    #             miscs_path,
    #         ]),
            
    #         # Source Code
    #         ft.Text("Source Code Files", size=24, weight=ft.FontWeight.W_100),
    #         ft.Row([
    #             ft.Button("Select", on_click=source_code_folder),
    #             source_code_path,
    #         ]), 
            
    #         # Zip File
    #         ft.Text("Zip Files", size=24, weight=ft.FontWeight.W_100),
    #         ft.Row([
    #             ft.Button("Select", on_click=zips_folder),
    #             zips_path,
    #         ]),


    #     ])
    # )

    #  =====================================================
    path_states = {}
    for category in data:
        name = category["name"]
        saved_dir = category.get("directory", downloads_path)
        path_states[name] = ft.Text(value=saved_dir)

    def make_folder_picker(category_name):
        def pick_folder(e):
            root = tk.Tk()
            root.withdraw()
            root.wm_attributes('-topmost', 1)
            folder = filedialog.askdirectory()
            if folder:
                path_states[category_name].value = folder
            else:
                path_states[category_name].value = path_states[category_name].value  # keep existing
            page.update()
        return pick_folder

    # Build UI rows dynamically
    rows = []
    for category in data:
        name = category["name"]
        extensions = category.get("extensions", [])
        ext_preview = ", ".join(f".{e}" for e in extensions[:6])
        if len(extensions) > 6:
            ext_preview += f"  (+{len(extensions) - 6} more)"

        rows.append(
            ft.Column([
                ft.Text(f"{name} Files", size=20, weight=ft.FontWeight.W_500),
                ft.Text(ext_preview, size=11, color=ft.Colors.GREY_500, italic=True),
                ft.Row([
                    ft.ElevatedButton("Select Folder", on_click=make_folder_picker(name)),
                    path_states[name],
                ]),
                ft.Divider(height=8, color=ft.Colors.TRANSPARENT),
            ])
        )

    page.add(
        ft.Text("FILE ORGANIZER", size=24, weight=ft.FontWeight.W_600),
        ft.Divider(),
        ft.Column(rows, scroll=ft.ScrollMode.AUTO, expand=True),
    )
ft.run(main)
