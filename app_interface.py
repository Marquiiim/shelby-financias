import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from datetime import datetime

class ShelbyFinancias:
    def __init__(self, root):
        self.root = root
        self.root.title("SHELBY FINANCIAS S.A")
        self.root.geometry("400x350")  # TAMANHO REDUZIDO DA JANELA
        
        # CENTRALIZA A JANELA NA TELA
        self._center_window()
        
        # APLICA O TEMA MODERNO 'MINTY' DO TTKBOOTSTRAP
        self.style = Style(theme='minty')
        
        # CRIA O FRAME PRINCIPAL COM PADDING REDUZIDO
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # TÍTULO PRINCIPAL DA INTERFACE
        self.title_label = ttk.Label(
            self.main_frame, 
            text="ADICIONAR INDIVÍDUO", 
            font=('Helvetica', 14, 'bold')
        )
        self.title_label.pack(pady=(0, 15))  # ESPAÇAMENTO REDUZIDO ABAIXO DO TÍTULO
        
        # FRAME DOS INPUTS COM BORDA VISÍVEL PARA AGRUPAMENTO
        self.input_frame = ttk.LabelFrame(self.main_frame, text=" Dados do Indivíduo ", padding=10)
        self.input_frame.pack(fill=tk.X, pady=5)
        
        # CONFIGURAÇÕES DE ESPAÇAMENTO COMPACTO
        padx_compact = 5
        pady_compact = 3
        
        # CAMPO NOME - LABEL E ENTRY
        ttk.Label(self.input_frame, text="Nome:").grid(
            row=0, column=0, padx=padx_compact, pady=pady_compact, sticky=tk.W)
        
        self.name_entry = ttk.Entry(self.input_frame)
        self.name_entry.grid(
            row=0, column=1, padx=padx_compact, pady=pady_compact, sticky=tk.EW)
        
        # CAMPO VALOR - LABEL E ENTRY
        ttk.Label(self.input_frame, text="Valor:").grid(
            row=1, column=0, padx=padx_compact, pady=pady_compact, sticky=tk.W)
        
        self.value_entry = ttk.Entry(self.input_frame)
        self.value_entry.grid(
            row=1, column=1, padx=padx_compact, pady=pady_compact, sticky=tk.EW)
        
        # CAMPO VALOR - LABEL E ENTRY
        ttk.Label(self.input_frame, text="Endereço:").grid(
            row=2, column=0, padx=padx_compact, pady=pady_compact, sticky=tk.W)
        
        self.address_entry = ttk.Entry(self.input_frame)
        self.address_entry.grid(
            row=2, column=1, padx=padx_compact, pady=pady_compact, sticky=tk.EW)
        
        # CAMPO DATA - LABEL E ENTRY (PRÉ-PREENCHIDO COM DATA ATUAL)
        ttk.Label(self.input_frame, text="Data:").grid(
            row=3, column=0, padx=padx_compact, pady=pady_compact, sticky=tk.W)
        
        self.date_entry = ttk.Entry(self.input_frame)
        self.date_entry.insert(0, datetime.now().strftime('%d/%m/%Y'))
        self.date_entry.grid(
            row=3, column=1, padx=padx_compact, pady=pady_compact, sticky=tk.EW)
        
        # CONFIGURA A EXPANSÃO DA COLUNA DOS CAMPOS DE ENTRADA
        self.input_frame.columnconfigure(1, weight=1)
        
        # BOTÃO PRINCIPAL DE AÇÃO - ESTILO SUCCESS (VERDE)
        self.add_button = ttk.Button(
            self.main_frame, 
            text="ADICIONAR", 
            style='success.TButton',
            command=self.add_item
        )
        self.add_button.pack(pady=10, ipadx=5, ipady=3)  # TAMANHO MAIS COMPACTO
        
        # LABEL DE STATUS PARA FEEDBACK AO USUÁRIO
        self.status_label = ttk.Label(
            self.main_frame, 
            text="", 
            font=('Helvetica', 8)
        )
        self.status_label.pack(pady=(5, 0))
        
    def _center_window(self):
        """MÉTODO PARA CENTRALIZAR A JANELA NA TELA"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def add_item(self):
        """MÉTODO EXECUTADO QUANDO O BOTÃO ADICIONAR É PRESSIONADO"""
        name = self.name_entry.get()
        value = self.value_entry.get()
        address = self.address_entry.get()
        date = self.date_entry.get()
        
        # VALIDAÇÃO DOS CAMPOS OBRIGATÓRIOS
        if not name or not value or not address:
            self.status_label.config(text="Preencha nome, valor e endereço!", style='danger.TLabel')
            return
            
        # VALIDAÇÃO DO FORMATO NUMÉRICO DO VALOR
        try:
            float(value)  # TENTA CONVERTER O VALOR PARA FLOAT
        except ValueError:
            self.status_label.config(text="Valor deve ser numérico!", style='danger.TLabel')
            return
            
        # AQUI VOCÊ DEVE IMPLEMENTAR SUA LÓGICA DE PROGRAMAÇÃO
        self.status_label.config(
            text=f"Item adicionado: {name} (R${value}) em {date}", 
            style='success.TLabel'
        )
        
        # LIMPA OS CAMPOS APÓS ADIÇÃO
        self.name_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)
        self.name_entry.focus_set()  # RETORNA O FOCO PARA O CAMPO NOME

if __name__ == "__main__":
    root = tk.Tk()
    app = ShelbyFinancias(root)
    root.mainloop()