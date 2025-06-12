import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import USPUtils # Importa a biblioteca USPUtils

# Instalar: pip install ttkthemes
try:
    from ttkthemes import ThemedTk
except ImportError:
    messagebox.showerror("Erro de Instalação", "A biblioteca 'ttkthemes' não está instalada.\n"
                                             "Por favor, execute: pip install ttkthemes")
    exit()

class USPApp:
    def __init__(self, root):
        root.geometry('600x800')
        self.root = root
        self.root.title("USPUtils - O Executor do Mago!")

        # Configurações do tema "Matrix"
        self.root.set_theme("black") # Usando um tema escuro base do ttkthemes

        # Cores customizadas para o estilo Matrix
        self.bg_color = "#000000"  # Preto puro
        self.fg_color = "#00FF00"  # Verde brilhante
        self.entry_bg = "#0A0A0A"  # Verde escuro para campos de entrada
        self.entry_fg = "#00FF00"
        self.button_bg = "#003300" # Verde mais escuro para botões
        self.button_fg = "#00FF00"
        self.border_color = "#006600" # Borda verde para frames

        self.root.configure(bg=self.bg_color)
        self.root.option_add("*TNotebook*background", self.bg_color)
        self.root.option_add("*TNotebook*foreground", self.fg_color)
        self.root.option_add("*TNotebook.Tab*background", self.bg_color)
        self.root.option_add("*TNotebook.Tab*foreground", self.fg_color)
        self.root.option_add("*TNotebook.Tab*selectbackground", self.button_bg)
        self.root.option_add("*TNotebook.Tab*selectforeground", self.button_fg)

        # Configurar estilos para widgets específicos
        style = ttk.Style()
        style.configure("TLabel", background=self.bg_color, foreground=self.fg_color)
        style.configure("TButton", background=self.button_bg, foreground=self.button_fg,
                        font=('Consolas', 10, 'bold'), borderwidth=2, relief="solid", bordercolor=self.border_color)
        style.map("TButton", background=[('active', self.border_color)])

        style.configure("TEntry", fieldbackground=self.entry_bg, foreground=self.entry_fg,
                        insertbackground=self.entry_fg, borderwidth=2, relief="solid", bordercolor=self.border_color)

        style.configure("TFrame", background=self.bg_color)
        style.configure("TLabelframe", background=self.bg_color, foreground=self.fg_color, bordercolor=self.border_color)
        style.configure("TLabelframe.Label", background=self.bg_color, foreground=self.fg_color)

        # Style for ScrolledText (manual configuration as it's not a ttk widget)
        # We'll set these when creating the ScrolledText widget

        self.create_notebook()
        self.create_menu()

    def create_notebook(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True, fill="both")

        # Abas para cada categoria de função
        self.mac_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.mac_frame, text="MAC")
        self.create_mac_tab(self.mac_frame)

        self.matrizes_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.matrizes_frame, text="Matrizes")
        self.create_matrizes_tab(self.matrizes_frame)

        self.vetores_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.vetores_frame, text="Vetores")
        self.create_vetores_tab(self.vetores_frame)

        self.calculo_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.calculo_frame, text="Cálculo")
        self.create_calculo_tab(self.calculo_frame)

        self.geomatica_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.geomatica_frame, text="Geomática")
        self.create_geomatica_tab(self.geomatica_frame)

        self.quimica_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.quimica_frame, text="Química")
        self.create_quimica_tab(self.quimica_frame)

    def create_menu(self):
        menubar = tk.Menu(self.root, bg=self.bg_color, fg=self.fg_color,
                          activebackground=self.button_bg, activeforeground=self.button_fg)
        self.root.config(menu=menubar)

        help_menu = tk.Menu(menubar, tearoff=0, bg=self.bg_color, fg=self.fg_color,
                             activebackground=self.button_bg, activeforeground=self.button_fg)
        menubar.add_cascade(label="Ajuda", menu=help_menu)
        help_menu.add_command(label="Sobre", command=self.show_about)
        help_menu.add_command(label="Ajuda USPUtils (Console)", command=USPUtils.help) # Chama a função help da USPUtils
        help_menu.add_command(label="Mostrar Ajuda no App", command=self.show_usp_help_in_app)

    def show_about(self):
        messagebox.showinfo("Sobre", "USPUtils Calculator - Estilo Matrix\n"
                                     "Todas as funções da biblioteca USPUtils integradas.\n"
                                     "Desenvolvido para você, meu rei!")

    def show_usp_help_in_app(self):
        help_window = tk.Toplevel(self.root)
        help_window.title("Ajuda USPUtils")
        help_window.geometry("700x500")
        help_window.configure(bg=self.bg_color)

        help_text_widget = scrolledtext.ScrolledText(help_window, wrap=tk.WORD,
                                                     bg=self.entry_bg, fg=self.entry_fg,
                                                     insertbackground=self.entry_fg,
                                                     font=('Consolas', 10),
                                                     borderwidth=2, relief="solid", highlightbackground=self.border_color, highlightcolor=self.border_color)
        help_text_widget.pack(expand=True, fill="both", padx=10, pady=10)

        # Captura a saída da função help
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            USPUtils.help()
        s = f.getvalue()
        help_text_widget.insert(tk.END, s)
        help_text_widget.config(state=tk.DISABLED) # Torna o texto somente leitura

    # --- MAC Tab ---
    def create_mac_tab(self, parent_frame):
        # eh_palin
        palin_frame = ttk.LabelFrame(parent_frame, text="Palíndromo?")
        palin_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(palin_frame, text="Texto:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.palin_entry = ttk.Entry(palin_frame, width=50)
        self.palin_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Button(palin_frame, text="Verificar Palíndromo", command=self.mac_eh_palin).grid(row=1, column=0, columnspan=2, pady=5)
        self.palin_result_label = ttk.Label(palin_frame, text="Resultado: ")
        self.palin_result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # conta_vogais
        vogais_frame = ttk.LabelFrame(parent_frame, text="Contar Vogais")
        vogais_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(vogais_frame, text="Texto:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.vogais_entry = ttk.Entry(vogais_frame, width=50)
        self.vogais_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Button(vogais_frame, text="Contar Vogais", command=self.mac_conta_vogais).grid(row=1, column=0, columnspan=2, pady=5)
        self.vogais_result_label = ttk.Label(vogais_frame, text="Resultado: ")
        self.vogais_result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # inverter
        inverter_frame = ttk.LabelFrame(parent_frame, text="Inverter Texto")
        inverter_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(inverter_frame, text="Texto:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.inverter_entry = ttk.Entry(inverter_frame, width=50)
        self.inverter_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Button(inverter_frame, text="Inverter", command=self.mac_inverter).grid(row=1, column=0, columnspan=2, pady=5)
        self.inverter_result_label = ttk.Label(inverter_frame, text="Resultado: ")
        self.inverter_result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # numero_par
        par_frame = ttk.LabelFrame(parent_frame, text="Número Par?")
        par_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(par_frame, text="Número:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.par_entry = ttk.Entry(par_frame, width=20)
        self.par_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")
        ttk.Button(par_frame, text="Verificar Par", command=self.mac_numero_par).grid(row=1, column=0, columnspan=2, pady=5)
        self.par_result_label = ttk.Label(par_frame, text="Resultado: ")
        self.par_result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=2, sticky="w")

    def mac_eh_palin(self):
        text = self.palin_entry.get()
        result = USPUtils.eh_palin(text)
        self.palin_result_label.config(text=f"Resultado: {result}")

    def mac_conta_vogais(self):
        text = self.vogais_entry.get()
        result = USPUtils.conta_vogais(text)
        self.vogais_result_label.config(text=f"Resultado: {result}")

    def mac_inverter(self):
        text = self.inverter_entry.get()
        result = USPUtils.inverter(text)
        self.inverter_result_label.config(text=f"Resultado: {result}")

    def mac_numero_par(self):
        try:
            num = int(self.par_entry.get())
            result = USPUtils.numero_par(num)
            self.par_result_label.config(text=f"Resultado: {result}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número inteiro válido.")

    # --- Matrizes Tab ---
    def create_matrizes_tab(self, parent_frame):
        # mat_criar e mat_preencher (adaptado para GUI)
        criar_frame = ttk.LabelFrame(parent_frame, text="Criar Matriz")
        criar_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(criar_frame, text="Linhas:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.mat_criar_linhas = ttk.Entry(criar_frame, width=5)
        self.mat_criar_linhas.grid(row=0, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(criar_frame, text="Colunas:").grid(row=0, column=2, padx=5, pady=2, sticky="w")
        self.mat_criar_colunas = ttk.Entry(criar_frame, width=5)
        self.mat_criar_colunas.grid(row=0, column=3, padx=5, pady=2, sticky="w")
        ttk.Button(criar_frame, text="Criar Matriz Vazia", command=self.mat_criar_gui).grid(row=0, column=4, padx=5, pady=2)
        self.mat_criar_result = ttk.Label(criar_frame, text="Matriz Vazia: ")
        self.mat_criar_result.grid(row=1, column=0, columnspan=5, padx=5, pady=2, sticky="w")
        ttk.Label(criar_frame, text="Para preencher ou usar, digite a matriz (ex: [[1,2],[3,4]]):").grid(row=2, column=0, columnspan=5, padx=5, pady=2, sticky="w")
        self.mat_input_generic = ttk.Entry(criar_frame, width=80)
        self.mat_input_generic.grid(row=3, column=0, columnspan=5, padx=5, pady=2, sticky="ew")

        # mat_soma
        soma_frame = ttk.LabelFrame(parent_frame, text="Soma de Matrizes")
        soma_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(soma_frame, text="Matriz A:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.mat_soma_a = ttk.Entry(soma_frame, width=50)
        self.mat_soma_a.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Label(soma_frame, text="Matriz B:").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.mat_soma_b = ttk.Entry(soma_frame, width=50)
        self.mat_soma_b.grid(row=1, column=1, padx=5, pady=2, sticky="ew")
        ttk.Button(soma_frame, text="Somar", command=self.mat_soma_gui).grid(row=2, column=0, columnspan=2, pady=5)
        self.mat_soma_result = ttk.Label(soma_frame, text="Resultado: ")
        self.mat_soma_result.grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # mat_mult
        mult_frame = ttk.LabelFrame(parent_frame, text="Multiplicação de Matrizes / Escalar")
        mult_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(mult_frame, text="Matriz A:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.mat_mult_a = ttk.Entry(mult_frame, width=50)
        self.mat_mult_a.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Label(mult_frame, text="Matriz B ou Escalar:").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.mat_mult_b = ttk.Entry(mult_frame, width=50)
        self.mat_mult_b.grid(row=1, column=1, padx=5, pady=2, sticky="ew")
        ttk.Button(mult_frame, text="Multiplicar", command=self.mat_mult_gui).grid(row=2, column=0, columnspan=2, pady=5)
        self.mat_mult_result = ttk.Label(mult_frame, text="Resultado: ")
        self.mat_mult_result.grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # mat_det
        det_frame = ttk.LabelFrame(parent_frame, text="Determinante de Matriz")
        det_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(det_frame, text="Matriz:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.mat_det_m = ttk.Entry(det_frame, width=50)
        self.mat_det_m.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Button(det_frame, text="Calcular Determinante", command=self.mat_det_gui).grid(row=1, column=0, columnspan=2, pady=5)
        self.mat_det_result = ttk.Label(det_frame, text="Resultado: ")
        self.mat_det_result.grid(row=2, column=0, columnspan=2, padx=5, pady=2, sticky="w")

    def mat_criar_gui(self):
        try:
            linhas = int(self.mat_criar_linhas.get())
            colunas = int(self.mat_criar_colunas.get())
            matriz = USPUtils.mat_criar(linhas, colunas)
            self.mat_criar_result.config(text=f"Matriz {linhas}x{colunas} Vazia: {matriz}")
            # Dica para o usuário sobre como preencher/usar
            messagebox.showinfo("Criar Matriz", "Matriz vazia criada. Para preenchê-la ou usá-la em outras operações, digite os valores no formato Python (ex: [[1,2],[3,4]]) no campo genérico abaixo ou diretamente nos campos de operação.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar matriz: {e}")

    def mat_soma_gui(self):
        try:
            mat_a = eval(self.mat_soma_a.get())
            mat_b = eval(self.mat_soma_b.get())
            result = USPUtils.mat_soma(mat_a, mat_b)
            self.mat_soma_result.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao somar matrizes: {e}. Formato esperado: [[x,y],[z,w]]")

    def mat_mult_gui(self):
        try:
            mat_a = eval(self.mat_mult_a.get())
            b_val = self.mat_mult_b.get()
            if b_val.startswith("["): # Assume que é outra matriz
                mat_b = eval(b_val)
            else: # Assume que é um escalar
                mat_b = float(b_val) if '.' in b_val else int(b_val)

            result = USPUtils.mat_mult(mat_a, mat_b)
            self.mat_mult_result.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao multiplicar: {e}. Formato esperado para matriz: [[x,y],[z,w]]. Para escalar: número.")

    def mat_det_gui(self):
        try:
            mat = eval(self.mat_det_m.get())
            result = USPUtils.mat_det(mat)
            self.mat_det_result.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular determinante: {e}. Formato esperado: [[x,y],[z,w]] para matriz quadrada.")

    # --- Vetores Tab ---
    def create_vetores_tab(self, parent_frame):
        # esc_dot
        dot_frame = ttk.LabelFrame(parent_frame, text="Produto Escalar (Dot Product)")
        dot_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(dot_frame, text="Vetor A (ex: [1,2,3]):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.vet_dot_a = ttk.Entry(dot_frame, width=50)
        self.vet_dot_a.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Label(dot_frame, text="Vetor B (ex: [4,5,6]):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.vet_dot_b = ttk.Entry(dot_frame, width=50)
        self.vet_dot_b.grid(row=1, column=1, padx=5, pady=2, sticky="ew")
        ttk.Button(dot_frame, text="Calcular Produto Escalar", command=self.vet_dot_gui).grid(row=2, column=0, columnspan=2, pady=5)
        self.vet_dot_result = ttk.Label(dot_frame, text="Resultado: ")
        self.vet_dot_result.grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # vet_cross
        cross_frame = ttk.LabelFrame(parent_frame, text="Produto Vetorial (Cross Product)")
        cross_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(cross_frame, text="Vetor A (ex: [1,0,0]):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.vet_cross_a = ttk.Entry(cross_frame, width=50)
        self.vet_cross_a.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Label(cross_frame, text="Vetor B (ex: [0,1,0]):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.vet_cross_b = ttk.Entry(cross_frame, width=50)
        self.vet_cross_b.grid(row=1, column=1, padx=5, pady=2, sticky="ew")
        ttk.Button(cross_frame, text="Calcular Produto Vetorial", command=self.vet_cross_gui).grid(row=2, column=0, columnspan=2, pady=5)
        self.vet_cross_result = ttk.Label(cross_frame, text="Resultado: ")
        self.vet_cross_result.grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # vet_proj
        proj_frame = ttk.LabelFrame(parent_frame, text="Projeção Vetorial")
        proj_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(proj_frame, text="Vetor U (a ser projetado):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.vet_proj_u = ttk.Entry(proj_frame, width=50)
        self.vet_proj_u.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Label(proj_frame, text="Vetor V (base):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.vet_proj_v = ttk.Entry(proj_frame, width=50)
        self.vet_proj_v.grid(row=1, column=1, padx=5, pady=2, sticky="ew")
        ttk.Button(proj_frame, text="Calcular Projeção", command=self.vet_proj_gui).grid(row=2, column=0, columnspan=2, pady=5)
        self.vet_proj_result = ttk.Label(proj_frame, text="Resultado: ")
        self.vet_proj_result.grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # reta_vet
        reta_frame = ttk.LabelFrame(parent_frame, text="Reta por Dois Pontos")
        reta_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(reta_frame, text="Ponto 1 (ex: [0,0,0]):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.reta_p1 = ttk.Entry(reta_frame, width=50)
        self.reta_p1.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Label(reta_frame, text="Ponto 2 (ex: [1,2,3]):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.reta_p2 = ttk.Entry(reta_frame, width=50)
        self.reta_p2.grid(row=1, column=1, padx=5, pady=2, sticky="ew")
        ttk.Button(reta_frame, text="Calcular Reta", command=self.reta_vet_gui).grid(row=2, column=0, columnspan=2, pady=5)
        self.reta_vet_result = ttk.Label(reta_frame, text="Resultado: ")
        self.reta_vet_result.grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # plano_area
        plano_frame = ttk.LabelFrame(parent_frame, text="Área de Paralelogramo (vetores 3D)")
        plano_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(plano_frame, text="Vetor U (ex: [1,0,0]):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.plano_u = ttk.Entry(plano_frame, width=50)
        self.plano_u.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Label(plano_frame, text="Vetor V (ex: [0,1,0]):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.plano_v = ttk.Entry(plano_frame, width=50)
        self.plano_v.grid(row=1, column=1, padx=5, pady=2, sticky="ew")
        ttk.Button(plano_frame, text="Calcular Área", command=self.plano_area_gui).grid(row=2, column=0, columnspan=2, pady=5)
        self.plano_area_result = ttk.Label(plano_frame, text="Resultado: ")
        self.plano_area_result.grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

    def vet_dot_gui(self):
        try:
            a = eval(self.vet_dot_a.get())
            b = eval(self.vet_dot_b.get())
            result = USPUtils.esc_dot(a, b)
            self.vet_dot_result.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular produto escalar: {e}. Formato esperado: [x,y,z]")

    def vet_cross_gui(self):
        try:
            a = eval(self.vet_cross_a.get())
            b = eval(self.vet_cross_b.get())
            result = USPUtils.vet_cross(a, b)
            self.vet_cross_result.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular produto vetorial: {e}. Apenas vetores 3D. Formato esperado: [x,y,z]")

    def vet_proj_gui(self):
        try:
            u = eval(self.vet_proj_u.get())
            v = eval(self.vet_proj_v.get())
            result = USPUtils.vet_proj(u, v)
            self.vet_proj_result.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular projeção: {e}. Formato esperado: [x,y,z]")

    def reta_vet_gui(self):
        try:
            p1 = eval(self.reta_p1.get())
            p2 = eval(self.reta_p2.get())
            result = USPUtils.reta_vet(p1, p2)
            self.reta_vet_result.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular reta: {e}. Formato esperado: [x,y,z]")

    def plano_area_gui(self):
        try:
            u = eval(self.plano_u.get())
            v = eval(self.plano_v.get())
            result = USPUtils.plano_area(u, v)
            self.plano_area_result.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular área do plano: {e}. Apenas vetores 3D. Formato esperado: [x,y,z]")

    # --- Cálculo Tab ---
    def create_calculo_tab(self, parent_frame):
        # calc_limite
        limite_frame = ttk.LabelFrame(parent_frame, text="Cálculo de Limite")
        limite_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(limite_frame, text="Expressão (ex: x^2 + 3*x):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.limite_expr_entry = ttk.Entry(limite_frame, width=40)
        self.limite_expr_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Label(limite_frame, text="Variável (ex: x):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.limite_var_entry = ttk.Entry(limite_frame, width=10)
        self.limite_var_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
        self.limite_var_entry.insert(0, 'x')
        ttk.Label(limite_frame, text="Valor para onde a variável tende:").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.limite_valor_entry = ttk.Entry(limite_frame, width=10)
        self.limite_valor_entry.grid(row=2, column=1, padx=5, pady=2, sticky="w")
        self.limite_valor_entry.insert(0, '0')
        ttk.Button(limite_frame, text="Calcular Limite", command=self.calcular_limite).grid(row=3, column=0, columnspan=2, pady=5)
        self.limite_result_label = ttk.Label(limite_frame, text="Resultado: ")
        self.limite_result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # calc_deriv
        derivada_frame = ttk.LabelFrame(parent_frame, text="Cálculo de Derivada")
        derivada_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(derivada_frame, text="Expressão (ex: x^2 + 3*x):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.derivada_expr_entry = ttk.Entry(derivada_frame, width=40)
        self.derivada_expr_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Label(derivada_frame, text="Variável (ex: x):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.derivada_var_entry = ttk.Entry(derivada_frame, width=10)
        self.derivada_var_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
        self.derivada_var_entry.insert(0, 'x')
        ttk.Button(derivada_frame, text="Calcular Derivada", command=self.calcular_derivada).grid(row=2, column=0, columnspan=2, pady=5)
        self.derivada_result_label = ttk.Label(derivada_frame, text="Resultado: ")
        self.derivada_result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # calc_continua
        continua_frame = ttk.LabelFrame(parent_frame, text="Verificar Continuidade")
        continua_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(continua_frame, text="Expressão (ex: 1/x):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.continua_expr_entry = ttk.Entry(continua_frame, width=40)
        self.continua_expr_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Label(continua_frame, text="Variável (ex: x):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.continua_var_entry = ttk.Entry(continua_frame, width=10)
        self.continua_var_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
        self.continua_var_entry.insert(0, 'x')
        ttk.Button(continua_frame, text="Verificar Continuidade", command=self.verificar_continuidade).grid(row=2, column=0, columnspan=2, pady=5)
        self.continua_result_label = ttk.Label(continua_frame, text="Resultado: ")
        self.continua_result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # calc_integral
        integral_frame = ttk.LabelFrame(parent_frame, text="Cálculo de Integral")
        integral_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(integral_frame, text="Expressão (ex: x^2):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.integral_expr_entry = ttk.Entry(integral_frame, width=40)
        self.integral_expr_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Label(integral_frame, text="Variável (ex: x):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.integral_var_entry = ttk.Entry(integral_frame, width=10)
        self.integral_var_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
        self.integral_var_entry.insert(0, 'x')
        ttk.Label(integral_frame, text="Limite Inferior (opcional):").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.integral_a_entry = ttk.Entry(integral_frame, width=10)
        self.integral_a_entry.grid(row=2, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(integral_frame, text="Limite Superior (opcional):").grid(row=3, column=0, padx=5, pady=2, sticky="w")
        self.integral_b_entry = ttk.Entry(integral_frame, width=10)
        self.integral_b_entry.grid(row=3, column=1, padx=5, pady=2, sticky="w")
        ttk.Button(integral_frame, text="Calcular Integral", command=self.calcular_integral).grid(row=4, column=0, columnspan=2, pady=5)
        self.integral_result_label = ttk.Label(integral_frame, text="Resultado: ")
        self.integral_result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=2, sticky="w")

    def calcular_limite(self):
        expr = self.limite_expr_entry.get()
        var = self.limite_var_entry.get()
        valor_str = self.limite_valor_entry.get()
        try:
            valor = float(valor_str)
            result = USPUtils.calc_limite(expr, var, valor)
            self.limite_result_label.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular limite: {e}")

    def calcular_derivada(self):
        expr = self.derivada_expr_entry.get()
        var = self.derivada_var_entry.get()
        try:
            result = USPUtils.calc_deriv(expr, var)
            self.derivada_result_label.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular derivada: {e}")

    def verificar_continuidade(self):
        expr = self.continua_expr_entry.get()
        var = self.continua_var_entry.get()
        try:
            result = USPUtils.calc_continua(expr, var)
            self.continua_result_label.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao verificar continuidade: {e}")

    def calcular_integral(self):
        expr = self.integral_expr_entry.get()
        var = self.integral_var_entry.get()
        a_str = self.integral_a_entry.get()
        b_str = self.integral_b_entry.get()
        try:
            a = float(a_str) if a_str else None
            b = float(b_str) if b_str else None
            result = USPUtils.calc_integral(expr, var, a, b)
            self.integral_result_label.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular integral: {e}")

    # --- Geomática Tab ---
    def create_geomatica_tab(self, parent_frame):
        # calc_rumo
        rumo_frame = ttk.LabelFrame(parent_frame, text="Cálculo de Rumo")
        rumo_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(rumo_frame, text="Delta Leste (ΔE):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.rumo_de_entry = ttk.Entry(rumo_frame, width=10)
        self.rumo_de_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(rumo_frame, text="Delta Norte (ΔN):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.rumo_dn_entry = ttk.Entry(rumo_frame, width=10)
        self.rumo_dn_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
        ttk.Button(rumo_frame, text="Calcular Rumo", command=self.geomatica_calc_rumo).grid(row=2, column=0, columnspan=2, pady=5)
        self.rumo_result_label = ttk.Label(rumo_frame, text="Resultado: ")
        self.rumo_result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # calc_azimute
        azimute_frame = ttk.LabelFrame(parent_frame, text="Cálculo de Azimute")
        azimute_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(azimute_frame, text="Norte Origem (n1):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.azimute_n1_entry = ttk.Entry(azimute_frame, width=10)
        self.azimute_n1_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(azimute_frame, text="Leste Origem (e1):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.azimute_e1_entry = ttk.Entry(azimute_frame, width=10)
        self.azimute_e1_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(azimute_frame, text="Norte Destino (n2):").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.azimute_n2_entry = ttk.Entry(azimute_frame, width=10)
        self.azimute_n2_entry.grid(row=2, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(azimute_frame, text="Leste Destino (e2):").grid(row=3, column=0, padx=5, pady=2, sticky="w")
        self.azimute_e2_entry = ttk.Entry(azimute_frame, width=10)
        self.azimute_e2_entry.grid(row=3, column=1, padx=5, pady=2, sticky="w")
        ttk.Button(azimute_frame, text="Calcular Azimute", command=self.geomatica_calc_azimute).grid(row=4, column=0, columnspan=2, pady=5)
        self.azimute_result_label = ttk.Label(azimute_frame, text="Resultado: ")
        self.azimute_result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # calc_distancia (renomeada em USPUtils para calc_distancia_geomat)
        distancia_frame = ttk.LabelFrame(parent_frame, text="Cálculo de Distância (N/E)")
        distancia_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(distancia_frame, text="Norte 1 (n1):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.dist_n1_entry = ttk.Entry(distancia_frame, width=10)
        self.dist_n1_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(distancia_frame, text="Leste 1 (e1):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.dist_e1_entry = ttk.Entry(distancia_frame, width=10)
        self.dist_e1_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(distancia_frame, text="Norte 2 (n2):").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.dist_n2_entry = ttk.Entry(distancia_frame, width=10)
        self.dist_n2_entry.grid(row=2, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(distancia_frame, text="Leste 2 (e2):").grid(row=3, column=0, padx=5, pady=2, sticky="w")
        self.dist_e2_entry = ttk.Entry(distancia_frame, width=10)
        self.dist_e2_entry.grid(row=3, column=1, padx=5, pady=2, sticky="w")
        ttk.Button(distancia_frame, text="Calcular Distância", command=self.geomatica_calc_distancia).grid(row=4, column=0, columnspan=2, pady=5)
        self.distancia_result_label = ttk.Label(distancia_frame, text="Resultado: ")
        self.distancia_result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # angulo_re
        angulo_re_frame = ttk.LabelFrame(parent_frame, text="Ângulo com Ré")
        angulo_re_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(angulo_re_frame, text="Azimute Ré (Az_re):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.az_re_entry = ttk.Entry(angulo_re_frame, width=10)
        self.az_re_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(angulo_re_frame, text="Azimute Avante (Az_vante):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.az_vante_entry = ttk.Entry(angulo_re_frame, width=10)
        self.az_vante_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
        ttk.Button(angulo_re_frame, text="Calcular Ângulo", command=self.geomatica_angulo_re).grid(row=2, column=0, columnspan=2, pady=5)
        self.angulo_re_result_label = ttk.Label(angulo_re_frame, text="Resultado: ")
        self.angulo_re_result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # dec2dms / dms2dec (agora DEC_pra_AMS / AMS_pra_DEC)
        dec_dms_frame = ttk.LabelFrame(parent_frame, text="Conversão Angulares")
        dec_dms_frame.pack(padx=10, pady=5, fill="x")

        ttk.Label(dec_dms_frame, text="Decimal para DMS (ex: 45.123):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.dec_to_dms_entry = ttk.Entry(dec_dms_frame, width=20)
        self.dec_to_dms_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")
        ttk.Button(dec_dms_frame, text="Converter", command=self.geomatica_dec_to_dms).grid(row=0, column=2, padx=5, pady=2)
        self.dec_to_dms_result_label = ttk.Label(dec_dms_frame, text="Resultado: ")
        self.dec_to_dms_result_label.grid(row=1, column=0, columnspan=3, padx=5, pady=2, sticky="w")

        ttk.Label(dec_dms_frame, text="DMS para Decimal (G, M, S):").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.dms_g_entry = ttk.Entry(dec_dms_frame, width=5)
        self.dms_g_entry.grid(row=2, column=1, padx=2, pady=2, sticky="w")
        self.dms_m_entry = ttk.Entry(dec_dms_frame, width=5)
        self.dms_m_entry.grid(row=2, column=2, padx=2, pady=2, sticky="w")
        self.dms_s_entry = ttk.Entry(dec_dms_frame, width=5)
        self.dms_s_entry.grid(row=2, column=3, padx=2, pady=2, sticky="w")
        ttk.Button(dec_dms_frame, text="Converter", command=self.geomatica_dms_to_dec).grid(row=2, column=4, padx=5, pady=2)
        self.dms_to_dec_result_label = ttk.Label(dec_dms_frame, text="Resultado: ")
        self.dms_to_dec_result_label.grid(row=3, column=0, columnspan=5, padx=5, pady=2, sticky="w")

        # calc_elementos_locacao
        locacao_frame = ttk.LabelFrame(parent_frame, text="Elementos de Locação")
        locacao_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(locacao_frame, text="Estação N:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.est_n_entry = ttk.Entry(locacao_frame, width=10)
        self.est_n_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(locacao_frame, text="Estação E:").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.est_e_entry = ttk.Entry(locacao_frame, width=10)
        self.est_e_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(locacao_frame, text="Ponto N:").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.ponto_n_entry = ttk.Entry(locacao_frame, width=10)
        self.ponto_n_entry.grid(row=2, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(locacao_frame, text="Ponto E:").grid(row=3, column=0, padx=5, pady=2, sticky="w")
        self.ponto_e_entry = ttk.Entry(locacao_frame, width=10)
        self.ponto_e_entry.grid(row=3, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(locacao_frame, text="Referência N:").grid(row=4, column=0, padx=5, pady=2, sticky="w")
        self.ref_n_entry = ttk.Entry(locacao_frame, width=10)
        self.ref_n_entry.grid(row=4, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(locacao_frame, text="Referência E:").grid(row=5, column=0, padx=5, pady=2, sticky="w")
        self.ref_e_entry = ttk.Entry(locacao_frame, width=10)
        self.ref_e_entry.grid(row=5, column=1, padx=5, pady=2, sticky="w")
        ttk.Button(locacao_frame, text="Calcular Elementos", command=self.geomatica_calc_elementos_locacao).grid(row=6, column=0, columnspan=2, pady=5)
        self.locacao_result_label = ttk.Label(locacao_frame, text="Resultado: ")
        self.locacao_result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=2, sticky="w")

    def geomatica_calc_rumo(self):
        try:
            de = float(self.rumo_de_entry.get())
            dn = float(self.rumo_dn_entry.get())
            result = USPUtils.calc_rumo(de, dn)
            self.rumo_result_label.config(text=f"Resultado Rumo: {result:.4f}°")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular rumo: {e}")

    def geomatica_calc_azimute(self):
        try:
            n1 = float(self.azimute_n1_entry.get())
            e1 = float(self.azimute_e1_entry.get())
            n2 = float(self.azimute_n2_entry.get())
            e2 = float(self.azimute_e2_entry.get())
            result = USPUtils.calc_azimute(n1, e1, n2, e2)
            self.azimute_result_label.config(text=f"Resultado Azimute: {result:.4f}°")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular azimute: {e}")

    def geomatica_calc_distancia(self):
        try:
            n1 = float(self.dist_n1_entry.get())
            e1 = float(self.dist_e1_entry.get())
            n2 = float(self.dist_n2_entry.get())
            e2 = float(self.dist_e2_entry.get())
            result = USPUtils.calc_distancia_geomat(n1, e1, n2, e2)
            self.distancia_result_label.config(text=f"Resultado Distância: {result:.4f}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular distância: {e}")

    def geomatica_angulo_re(self):
        try:
            az_re = float(self.az_re_entry.get())
            az_vante = float(self.az_vante_entry.get())
            result = USPUtils.angulo_re(az_re, az_vante)
            self.angulo_re_result_label.config(text=f"Resultado Ângulo com Ré: {result:.4f}°")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular ângulo com ré: {e}")

    def geomatica_dec_to_dms(self):
        try:
            angle = float(self.dec_to_dms_entry.get())
            g, m, s = USPUtils.DEC_pra_AMS(angle)
            self.dec_to_dms_result_label.config(text=f"Resultado: {g}° {m}' {s:.2f}\"")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na conversão: {e}")

    def geomatica_dms_to_dec(self):
        try:
            g = float(self.dms_g_entry.get())
            m = float(self.dms_m_entry.get())
            s = float(self.dms_s_entry.get())
            result = USPUtils.AMS_pra_DEC(g, m, s)
            self.dms_to_dec_result_label.config(text=f"Resultado: {result:.6f} °")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na conversão: {e}")

    def geomatica_calc_elementos_locacao(self):
        try:
            est_n = float(self.est_n_entry.get())
            est_e = float(self.est_e_entry.get())
            ponto_n = float(self.ponto_n_entry.get())
            ponto_e = float(self.ponto_e_entry.get())
            ref_n = float(self.ref_n_entry.get())
            ref_e = float(self.ref_e_entry.get())
            az_lanc, ang_re, dist = USPUtils.calc_elementos_locacao(est_n, est_e, ponto_n, ponto_e, ref_n, ref_e)
            self.locacao_result_label.config(text=f"Azimute Lançamento: {az_lanc[0]}° {az_lanc[1]}' {az_lanc[2]:.2f}\"\n"
                                                 f"Ângulo com Ré: {ang_re[0]}° {ang_re[1]}' {ang_re[2]:.2f}\"\n"
                                                 f"Distância: {dist:.4f}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular elementos de locação: {e}")

    # --- Química dos Materiais Tab ---
    def create_quimica_tab(self, parent_frame):
        # nernst
        nernst_frame = ttk.LabelFrame(parent_frame, text="Equação de Nernst")
        nernst_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(nernst_frame, text="Potencial Padrão E0 (V):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.nernst_e0_entry = ttk.Entry(nernst_frame, width=10)
        self.nernst_e0_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(nernst_frame, text="Nº Elétrons (n):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.nernst_n_entry = ttk.Entry(nernst_frame, width=10)
        self.nernst_n_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(nernst_frame, text="Quociente da Reação (Q):").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.nernst_q_entry = ttk.Entry(nernst_frame, width=10)
        self.nernst_q_entry.grid(row=2, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(nernst_frame, text="Temperatura T (K, padrão 298.15):").grid(row=3, column=0, padx=5, pady=2, sticky="w")
        self.nernst_t_entry = ttk.Entry(nernst_frame, width=10)
        self.nernst_t_entry.grid(row=3, column=1, padx=5, pady=2, sticky="w")
        self.nernst_t_entry.insert(0, '298.15')
        ttk.Button(nernst_frame, text="Calcular Potencial", command=self.quimica_nernst).grid(row=4, column=0, columnspan=2, pady=5)
        self.nernst_result_label = ttk.Label(nernst_frame, text="Resultado: ")
        self.nernst_result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # gibbs
        gibbs_frame = ttk.LabelFrame(parent_frame, text="Energia Livre de Gibbs (ΔG)")
        gibbs_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(gibbs_frame, text="Potencial da Célula E (V):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.gibbs_e_entry = ttk.Entry(gibbs_frame, width=10)
        self.gibbs_e_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(gibbs_frame, text="Nº Elétrons (n):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.gibbs_n_entry = ttk.Entry(gibbs_frame, width=10)
        self.gibbs_n_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
        ttk.Button(gibbs_frame, text="Calcular ΔG", command=self.quimica_gibbs).grid(row=2, column=0, columnspan=2, pady=5)
        self.gibbs_result_label = ttk.Label(gibbs_frame, text="Resultado: ")
        self.gibbs_result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # gibbs_to_k
        gibbs_k_frame = ttk.LabelFrame(parent_frame, text="Constante de Equilíbrio (K)")
        gibbs_k_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(gibbs_k_frame, text="Potencial Padrão E (V):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.gibbs_k_e_entry = ttk.Entry(gibbs_k_frame, width=10)
        self.gibbs_k_e_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(gibbs_k_frame, text="Nº Elétrons (n):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.gibbs_k_n_entry = ttk.Entry(gibbs_k_frame, width=10)
        self.gibbs_k_n_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
        ttk.Label(gibbs_k_frame, text="Temperatura T (K, padrão 298.15):").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.gibbs_k_t_entry = ttk.Entry(gibbs_k_frame, width=10)
        self.gibbs_k_t_entry.grid(row=2, column=1, padx=5, pady=2, sticky="w")
        self.gibbs_k_t_entry.insert(0, '298.15')
        ttk.Button(gibbs_k_frame, text="Calcular K", command=self.quimica_gibbs_to_k).grid(row=3, column=0, columnspan=2, pady=5)
        self.gibbs_k_result_label = ttk.Label(gibbs_k_frame, text="Resultado: ")
        self.gibbs_k_result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=2, sticky="w")

    def quimica_nernst(self):
        try:
            e0 = float(self.nernst_e0_entry.get())
            n = float(self.nernst_n_entry.get())
            q = float(self.nernst_q_entry.get())
            t_str = self.nernst_t_entry.get()
            t = float(t_str) if t_str else 298.15
            result = USPUtils.nernst(e0, n, q, t)
            self.nernst_result_label.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na equação de Nernst: {e}")

    def quimica_gibbs(self):
        try:
            e = float(self.gibbs_e_entry.get())
            n = float(self.gibbs_n_entry.get())
            result = USPUtils.gibbs(e, n)
            self.gibbs_result_label.config(text=f"Resultado ΔG: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro no cálculo de ΔG: {e}")

    def quimica_gibbs_to_k(self):
        try:
            e = float(self.gibbs_k_e_entry.get())
            n = float(self.gibbs_k_n_entry.get())
            t_str = self.gibbs_k_t_entry.get()
            t = float(t_str) if t_str else 298.15
            result = USPUtils.gibbs_to_k(e, n, t)
            self.gibbs_k_result_label.config(text=f"Resultado K: {result}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro no cálculo de K: {e}")


if __name__ == "__main__":
    root = ThemedTk() # Usando ThemedTk para aplicar temas
    app = USPApp(root)
    root.mainloop()