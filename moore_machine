import tkinter as tk
from tkinter import messagebox, simpledialog


def generate_tables():
    try:
        numStates = int(state_entry.get())
        inputAlphabet = input_alphabet_entry.get()
        outputAlphabet = output_alphabet_entry.get()
        inputString = input_string_entry.get()

        stateNames = [f"q{i}" for i in range(numStates)]

        transitionTable = [[[None for _ in range(numStates)] for _ in range(len(inputAlphabet))] for _ in
                           range(numStates)]
        outputTable = [""] * numStates

        transition_window = tk.Toplevel(window)
        transition_window.title("Transition Table")
        transition_text = tk.Text(transition_window)
        transition_text.pack()

        for i in range(numStates):
            transition_text.insert(tk.END, f"Durum {stateNames[i]} icin gecisleri girin:\n")
            for j in range(len(inputAlphabet)):
                transition_text.insert(tk.END, f"  {inputAlphabet[j]} icin yeni durum: ")
                nextState = simpledialog.askstring("Gecis Durumu",
                                                   f"Durum {stateNames[i]}, {inputAlphabet[j]} girisi sonrasi yeni durum: ")

                if nextState in stateNames:
                    nextStateIndex = stateNames.index(nextState)
                    transitionTable[i][j][0] = nextStateIndex
                else:
                    messagebox.showerror("Hata", f"{nextState} gecerli bir durum degil!")

        for i in range(numStates):
            outputChar = simpledialog.askstring("Cikti", f"Durum {stateNames[i]} icin cikti (or. 0 veya 1): ")
            outputTable[i] = outputChar

        currentState = 0
        output_sequence = [outputTable[currentState]]
        state_sequence = [stateNames[currentState]]

        for char in inputString:
            inputIndex = inputAlphabet.index(char)
            currentState = transitionTable[currentState][inputIndex][0]
            state_sequence.append(stateNames[currentState])
            output_sequence.append(outputTable[currentState])

        transition_text.insert(tk.END, "\nTransition Table\n")
        transition_text.insert(tk.END, "Old State | After input {0} | After input {1}\n".format(inputAlphabet[0],
                                                                                                inputAlphabet[1]))
        transition_text.insert(tk.END, "-----------------------------------------\n")
        for i in range(numStates):
            transition_text.insert(tk.END,
                                   f"{stateNames[i]} | {stateNames[transitionTable[i][0][0]]} | {stateNames[transitionTable[i][1][0]]}\n")

        output_window = tk.Toplevel(window)
        output_window.title("Output Table")
        output_text = tk.Text(output_window)
        output_text.pack()
        output_text.insert(tk.END, "State | Character Printed\n")
        output_text.insert(tk.END, "------------------------\n")
        for i in range(numStates):
            output_text.insert(tk.END, f"{stateNames[i]} | {outputTable[i]}\n")

        result_window = tk.Toplevel(window)
        result_window.title("Results")
        result_text = tk.Text(result_window)
        result_text.pack()
        result_text.insert(tk.END, f"Input String: {inputString}\n")
        result_text.insert(tk.END, f"State Transition: {' '.join(state_sequence)}\n")
        result_text.insert(tk.END, f"Output Sequence: {' '.join(output_sequence)}\n")

    except ValueError:
        messagebox.showerror("Error", "Lutfen gecerli bir sayisal deger girin.")


window = tk.Tk()
window.title("Moore Makinesi")

state_label = tk.Label(window, text="Durum sayisini girin:")
state_label.pack()
state_entry = tk.Entry(window)
state_entry.pack()

input_alphabet_label = tk.Label(window, text="Semboller alfabesini girin (or. 'ab'):")
input_alphabet_label.pack()
input_alphabet_entry = tk.Entry(window)
input_alphabet_entry.pack()

output_alphabet_label = tk.Label(window, text="Olasi cikti sembolleri alfabesini girin (or. '01'):")
output_alphabet_label.pack()
output_alphabet_entry = tk.Entry(window)
output_alphabet_entry.pack()

input_string_label = tk.Label(window, text="Giris dizisini girin:")
input_string_label.pack()
input_string_entry = tk.Entry(window)
input_string_entry.pack()

generate_button = tk.Button(window, text="Tabloları Olustur", command=generate_tables)
generate_button.pack()

window.mainloop()
