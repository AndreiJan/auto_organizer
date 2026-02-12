import flet as ft
import os
from tkinter import filedialog
import tkinter as tk
import json


script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'data.json')

def load_data():
    with open(json_path, 'r') as f:
        return json.load(f)

home_dir = os.path.expanduser("~")
downloads_path = os.path.join(home_dir, "Downloads")

def main(page: ft.Page):
    def main_page():

        data = load_data()  # Load fresh inside main every time app starts

        # Build state dynamically from JSON - one ft.Text per category
        path_states = {}
        for category in data:
            name = category["name"]
            saved_dir = category.get("directory", downloads_path)
            path_states[name] = ft.Text(value=saved_dir)
            print(f"[LOAD] {name} -> {saved_dir}")

        def save_to_json():
            for category in data:
                name = category["name"]
                new_dir = path_states[name].value
                print(f"[SAVE] {name} -> {new_dir}")
                category["directory"] = new_dir
            with open(json_path, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"[SAVE] Written to {json_path}")

        def make_folder_picker(category_name):
            def pick_folder(e):
                root = tk.Tk()
                root.withdraw()
                root.wm_attributes('-topmost', 1)
                folder = filedialog.askdirectory()
                print(f"[PICK] folder dialog returned: '{folder}'")
                if folder:
                    path_states[category_name].value = folder
                    print(f"[PICK] Set {category_name} -> {folder}")
                    save_to_json()
                page.update()
            return pick_folder
        
        def delete_folder(category_name):
            def on_delete(e):
                nonlocal data
                data = [item for item in data if item['name'] != category_name]
                if category_name in path_states:
                    del path_states[category_name]
                with open(json_path, 'w') as f:
                    json.dump(data, f, indent=4)
                print(f"[DELETE] Removed {category_name}")
                rebuild_ui()
                
            return on_delete
        

        def rebuild_ui():
            """Rebuild the entire UI with current data"""
            page.clean()
            
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
                            ft.ElevatedButton("Delete Folder", on_click=delete_folder(name), color=ft.Colors.RED_400)
                        ]),
                        ft.Divider(height=8, color=ft.Colors.TRANSPARENT),
                    ])
                )

            page.add(
                ft.Text("FILE ORGANIZER", size=24, weight=ft.FontWeight.W_600),

                ft.ElevatedButton("Go to Page 2", on_click=lambda e: new_folder()),
                ft.Divider(),
                ft.Column(rows, scroll=ft.ScrollMode.AUTO, expand=True),
            )
            page.update()
        rebuild_ui()

    def new_folder():
        page.clean()  # Clear everything on the page
        page.add(
            ft.Text("This is Page 2", size=30),
            ft.ElevatedButton("Go back to Page 1", on_click=lambda e: main_page())
        )
        page.update()
    main_page()
ft.app(target=main)