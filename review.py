import tkinter as tk
from threading import Thread

from prompts import apply_review_feedback


def main() -> None:
    window = tk.Tk()
    window.title("Apply Review Feedback")

    frame = tk.Frame(window, padx=10, pady=10)
    frame.pack()

    label1 = tk.Label(frame, text="Tutorial Fragment:")
    label1.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
    text_area1 = tk.Text(frame, wrap="word", width=80, height=10)
    text_area1.grid(row=1, column=0, padx=5, pady=5)

    label2 = tk.Label(frame, text="Review Feedback:")
    label2.grid(row=2, column=0, padx=5, pady=5, sticky="nw")
    text_area2 = tk.Text(frame, wrap="word", width=80, height=10)
    text_area2.grid(row=3, column=0, padx=5, pady=5)

    label3 = tk.Label(frame, text="Suggested Update:")
    label3.grid(row=4, column=0, padx=5, pady=5, sticky="nw")
    text_area3 = tk.Text(frame, wrap="word", width=80, height=10)
    text_area3.grid(row=5, column=0, padx=5, pady=5)

    slider_label = tk.Label(frame, text="Temperature:")
    slider_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
    slider = tk.Scale(frame, from_=0, to=1, resolution=0.05, orient=tk.HORIZONTAL)
    slider.grid(row=7, column=0, padx=5, pady=5, sticky="we")

    def on_button_click() -> None:
        btn.config(state=tk.DISABLED)
        text_area3.delete(1.0, tk.END)
        temperature: float = slider.get()
        fragment: str = text_area1.get(1.0, tk.END).rstrip()
        feedback: str = text_area2.get(1.0, tk.END).rstrip()

        def background_task():
            suggestion = apply_review_feedback(fragment, feedback, temperature)
            text_area3.insert(1.0, suggestion)
            btn.config(state=tk.NORMAL)

        Thread(target=background_task).start()

    btn = tk.Button(frame, text="Get Suggestion", command=on_button_click)
    btn.grid(row=8, column=0, padx=5, pady=10)

    window.mainloop()


if __name__ == "__main__":
    main()
