def main():
    import dearpygui.dearpygui as dpg
    import time

    dpg.create_context()

    languages = [
        {"name": "C/clang -O3", "time": "0.50s", "color": [70, 130, 180], "y": 100, "logo_y": 0},
        {"name": "Rust", "time": "0.50s", "color": [139, 69, 19], "y": 140, "logo_y": 50},
        {"name": "Java", "time": "0.54s", "color": [255, 140, 0], "y": 180, "logo_y": 100},
        {"name": "Kotlin", "time": "0.56s", "color": [128, 0, 128], "y": 220, "logo_y": 150},
        {"name": "Go", "time": "0.80s", "color": [0, 191, 255], "y": 260, "logo_y": 200},
        {"name": "Js/Bun", "time": "0.80s", "color": [219, 112, 147], "y": 300, "logo_y": 250},
        {"name": "Js/Node", "time": "1.03s", "color": [34, 139, 34], "y": 340, "logo_y": 300},
        {"name": "Js/Deno", "time": "1.06s", "color": [0, 0, 0], "y": 380, "logo_y": 350},
        {"name": "Dart", "time": "1.34s", "color": [0, 191, 255], "y": 420, "logo_y": 400},
        {"name": "PyPy", "time": "1.53s", "color": [169, 169, 169], "y": 460, "logo_y": 450},
        {"name": "PHP", "time": "9.93s", "color": [75, 0, 130], "y": 500, "logo_y": 500},
        {"name": "Ruby", "time": "28.80s", "color": [220, 20, 60], "y": 540, "logo_y": 550},
        {"name": "R", "time": "73.16s", "color": [0, 0, 255], "y": 580, "logo_y": 600},
        {"name": "Python", "time": "74.42s", "color": [255, 215, 0], "y": 620, "logo_y": 650}
    ]

    # Load the logos image
    width, height, channels, data = dpg.load_image("/Users/ediril/Documents/^_PROJ/language-balls/logos.jpeg")
    
    with dpg.texture_registry():
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="logos_texture")

    start_time = time.time()
    WINDOW_WIDTH = 900
    BOX_WIDTH = 280
    BOX_START_X = 100

    def update_animation():
        current_time = time.time() - start_time
        
        for i, lang in enumerate(languages):
            period = float(lang["time"].replace('s', ''))
            cycle_time = current_time % (period * 2)
            
            box_right_edge = BOX_START_X + BOX_WIDTH
            travel_distance = WINDOW_WIDTH - box_right_edge - 40
            
            if cycle_time <= period:
                x = box_right_edge + 20 + travel_distance * (cycle_time / period)
            else:
                x = WINDOW_WIDTH - 20 - travel_distance * ((cycle_time - period) / period)
            
            dpg.configure_item(f"ball_{i}", center=[x, lang["y"]])

    with dpg.window(label="1 Billion nested loop iterations", width=WINDOW_WIDTH, height=700, tag="main"):
        dpg.add_text("1 Billion nested loop iterations", pos=[20, 30], color=[0, 0, 0])
        
        with dpg.drawlist(width=WINDOW_WIDTH, height=650, pos=[0, 60]):
            dpg.draw_rectangle([0, 0], [WINDOW_WIDTH, 650], color=[240, 240, 240], fill=[240, 240, 240])
            
            for i, lang in enumerate(languages):
                logo_size = 40
                uv_min = [0, lang["logo_y"] / height]
                uv_max = [width / width, (lang["logo_y"] + 50) / height]
                
                dpg.draw_image("logos_texture", 
                              [50, lang["y"] - logo_size//2], 
                              [50 + logo_size, lang["y"] + logo_size//2],
                              uv_min=uv_min, uv_max=uv_max)
                
                dpg.draw_rectangle([BOX_START_X, lang["y"] - 15], [BOX_START_X + BOX_WIDTH, lang["y"] + 15], 
                                 color=[100, 100, 100], fill=[60, 60, 60])
                
                text_x = BOX_START_X + (BOX_WIDTH / 2) - len(f"{lang['name']} ({lang['time']})") * 3.5
                dpg.draw_text([text_x, lang["y"] - 5], f"{lang['name']} ({lang['time']})", 
                             color=[255, 255, 255], size=12)
                
                dpg.draw_circle([BOX_START_X + BOX_WIDTH + 20, lang["y"]], 15, 
                              color=lang["color"], fill=lang["color"], tag=f"ball_{i}")

    dpg.create_viewport(title="Language Performance Visualization", width=WINDOW_WIDTH, height=700)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("main", True)

    while dpg.is_dearpygui_running():
        update_animation()
        dpg.render_dearpygui_frame()

    dpg.destroy_context()

if __name__ == "__main__":
    main()