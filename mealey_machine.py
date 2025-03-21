import tkinter as tk
from tkinter import messagebox, simpledialog

class MealeyMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mealey Makinesi")
        self.root.geometry("600x600")

        self.num_states = 0
        self.input_alphabet = ""
        self.state_names = []
        self.transition_table = []
        self.input_string = ""

        self.create_widgets()

    def create_widgets(self):
        self.state_label = tk.Label(self.root, text="Durum Sayısı Girin:")
        self.state_label.pack()
        self.state_entry = tk.Entry(self.root)
        self.state_entry.pack()

        self.alphabet_label = tk.Label(self.root, text="Semboller Alfabesini Girin (örn. '01'):")
        self.alphabet_label.pack()
        self.alphabet_entry = tk.Entry(self.root)
        self.alphabet_entry.pack()

        self.transition_button = tk.Button(self.root, text="Geçiş Tablosunu Oluştur", command=self.create_transition_table)
        self.transition_button.pack()

        self.input_label = tk.Label(self.root, text="Giriş Dizisini Girin:")
        self.input_label.pack()
        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack()

        self.result_button = tk.Button(self.root, text="Sonuçları Göster", command=self.show_results)
        self.result_button.pack()

        self.results_text = tk.Text(self.root, height=10, width=70)
        self.results_text.pack()

    def create_transition_table(self):
        try:
            self.num_states = int(self.state_entry.get())
            self.input_alphabet = self.alphabet_entry.get()
            self.state_names = [f"q{i}" for i in range(self.num_states)]

            self.transition_table = [[None for _ in range(len(self.input_alphabet))] for _ in range(self.num_states)]

            for i in range(self.num_states):
                for j, symbol in enumerate(self.input_alphabet):
                    transition_input = simpledialog.askstring("Geçiş Bilgisi", f"Durum {self.state_names[i]}, '{symbol}' girisi sonrasi yeni durum (örn. q0) ve cikti (örn. 1):")
                    if transition_input:
                        new_state, output = transition_input.split()
                        new_state_index = self.state_names.index(new_state)
                        self.transition_table[i][j] = (new_state_index, output)

            messagebox.showinfo("Başarılı", "Geçiş tablosu oluşturuldu.")

        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")

    def show_results(self):
        try:
            self.input_string = self.input_entry.get()
            current_state = 0
            result = "State Transition and Output:\n"
            result += "Old State | New State | Output\n"
            result += "------------------------------\n"

            for symbol in self.input_string:
                input_index = self.input_alphabet.index(symbol)
                new_state, output = self.transition_table[current_state][input_index]
                result += f"    {self.state_names[current_state]}    |    {self.state_names[new_state]}    |    {output}\n"
                current_state = new_state

            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, result)

        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MealeyMachineApp(root)
    root.mainloop()
