import flet as ft
import os
from tkinter import filedialog
import tkinter as tk
import platform 



home_dir = os.path.expanduser("~")
downloads_path = os.path.join(home_dir, "Downloads")
def main(page: ft.Page):
    document_path = ft.Text(value=downloads_path)
    videos_path = ft.Text(value=downloads_path)
    installers_path = ft.Text(value=downloads_path)
    pictures_path = ft.Text(value=downloads_path)
    miscs_path = ft.Text(value=downloads_path)
    source_code_path = ft.Text(value=downloads_path)
    miscs_path = ft.Text(value=downloads_path)
    zips_path = ft.Text(value=downloads_path)

    def document_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
        # Positions the text
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        folder = filedialog.askdirectory()
        if folder:
            document_path.value = f"Selected: {folder}"
            print(f"Selected: {folder}")
        else:
            document_path.value = "Selection cancelled"
        page.update()

    def videos_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
        # Positions the text
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        folder = filedialog.askdirectory()
        if folder:
            videos_path.value = f"Selected: {folder}"
            print(f"Selected: {folder}")
        else:
            videos_path.value = "Selection cancelled"
        page.update()


    def installers_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
        # Positions the text
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        folder = filedialog.askdirectory()
        if folder:
            installers_path.value = f"Selected: {folder}"
            print(f"Selected: {folder}")
        else:
            installers_path.value = "Selection cancelled"
        page.update()
    def pictures_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
        # Positions the text
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        folder = filedialog.askdirectory()
        if folder:
            pictures_path.value = f"Selected: {folder}"
            print(f"Selected: {folder}")
        else:
            pictures_path.value = "Selection cancelled"
        page.update()
    def miscs_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
        # Positions the text
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        folder = filedialog.askdirectory()
        if folder:
            miscs_path.value = f"Selected: {folder}"
            print(f"Selected: {folder}")
        else:
            miscs_path.value = "Selection cancelled"
        page.update()
    def source_code_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
        # Positions the text
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        folder = filedialog.askdirectory()
        if folder:
            source_code_path.value = f"Selected: {folder}"
            print(f"Selected: {folder}")
        else:
            source_code_path.value = "Selection cancelled"
        page.update()
    
    def zips_folder(e): # Selects the specified Folder for Documents - if not selected - defaults to Downloads 
        # Positions the text
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        folder = filedialog.askdirectory()
        if folder:
            zips_path.value = f"Selected: {folder}"
            print(f"Selected: {folder}")
        else:
            zips_path.value = "Selection cancelled"
        page.update()
    page.add(
        ft.Text("FILE ORGANIZER", size=24, weight=ft.FontWeight.W_600),
        ft.Column([
            # Document
            ft.Text("Document Files", size=24, weight=ft.FontWeight.W_100),
            ft.Row([
                ft.Button("Select", on_click=document_folder),
                document_path,
            ]),           
            # Video
            ft.Text("Video Files", size=24, weight=ft.FontWeight.W_100),
            ft.Row([
                ft.Button("Select", on_click=videos_folder),
                videos_path,
            ]),

            # Installer
            ft.Text("Installer Files", size=24, weight=ft.FontWeight.W_100),
            ft.Row([
                ft.Button("Select", on_click=installers_folder),
                installers_path,
            ]),
            
            # Pictures
            ft.Text("Pictures Files", size=24, weight=ft.FontWeight.W_100),
            ft.Row([
                ft.Button("Select", on_click=pictures_folder),
                pictures_path,
            ]),
            
            # Misc
            ft.Text("Misc Files", size=24, weight=ft.FontWeight.W_100),
            ft.Row([
                ft.Button("Select", on_click=miscs_folder),
                miscs_path,
            ]),
            
            # Source Code
            ft.Text("Source Code Files", size=24, weight=ft.FontWeight.W_100),
            ft.Row([
                ft.Button("Select", on_click=source_code_folder),
                source_code_path,
            ]), 
            
            # Zip File
            ft.Text("Zip Files", size=24, weight=ft.FontWeight.W_100),
            ft.Row([
                ft.Button("Select", on_click=zips_folder),
                zips_path,
            ]),


        ])
    )

ft.run(main)
