import tkinter as tk
import random
import time


class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting and Searching Algorithms Visualizer")
        self.root.geometry("800x600")

        self.array = []
        self.bar_width = 4
        self.max_height = 500
        self.speed = 0.05  # Delay in sorting

        # Create the UI elements
        self.canvas = tk.Canvas(self.root, width=800, height=500, bg="white")
        self.canvas.pack()

        self.generate_button = tk.Button(self.root, text="Generate New Array", command=self.generate_array)
        self.generate_button.pack()

        self.sort_button = tk.Button(self.root, text="Sort Array (Bubble Sort)", command=self.bubble_sort)
        self.sort_button.pack()

        self.search_button = tk.Button(self.root, text="Search for Element (Linear Search)", command=self.linear_search)
        self.search_button.pack()

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack()

        self.info_label = tk.Label(self.root, text="")
        self.info_label.pack()

        self.generate_array()

    def generate_array(self):
        self.array = [random.randint(1, self.max_height) for _ in range(150)]
        self.draw_array()

    def draw_array(self, highlighted_idx=None, color="blue"):
        if not hasattr(self, 'canvas') or self.canvas is None:
            return  # Make sure canvas exists before trying to draw on it
        self.canvas.delete("all")
        for i, val in enumerate(self.array):
            x0 = i * self.bar_width
            y0 = self.max_height - val
            x1 = x0 + self.bar_width
            y1 = self.max_height
            color_bar = color if i != highlighted_idx else "red"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_bar)
        self.root.update()

    def bubble_sort(self):
        for i in range(len(self.array)):
            for j in range(len(self.array) - 1 - i):
                self.draw_array(highlighted_idx=j)
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    time.sleep(self.speed)
                    self.draw_array()
        self.info_label.config(text="Array Sorted!")

    def linear_search(self):
        try:
            target = int(self.input_entry.get())
        except ValueError:
            self.info_label.config(text="Please enter a valid number.")
            return

        self.info_label.config(text=f"Searching for {target}...")
        found_idx = self.linear_search_algo(target)
        if found_idx != -1:
            self.draw_array(highlighted_idx=found_idx, color="green")
            self.info_label.config(text=f"Element {target} found at index {found_idx}")
        else:
            self.info_label.config(text=f"Element {target} not found.")

    def linear_search_algo(self, target):
        for i in range(len(self.array)):
            if self.array[i] == target:
                return i
            self.draw_array(highlighted_idx=i, color="yellow")
            time.sleep(0.05)
        return -1


# Run the application
root = tk.Tk()
app = SortingVisualizer(root)
root.mainloop()
