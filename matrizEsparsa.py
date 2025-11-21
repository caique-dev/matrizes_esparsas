from LLRB import LLRB


class matrizEsparsa:
    def __init__(self):
        self.rows = LLRB() # árvore de linhas
        self.cols = LLRB() # árvore de colunas
        self.escalar = 1 # implementação lazy

    def _delete(self, i, j):
        row_tree = self.rows.get(i)
        if row_tree:
            row_tree.insert(j, None)

        col_tree = self.cols.get(j)
        if col_tree:
            col_tree.insert(i, None)
            
    def transpor(self):
        nova = matrizEsparsa()
        nova.rows = self.cols
        nova.cols = self.rows
        nova.escalar = self.escalar
        return nova

    def set(self, i, j, valor_inicial):
        valor_transformado = valor_inicial / self.escalar

        if valor_transformado == 0:
            self._delete(i, j)
            return

        # arvore de linhas
        row_tree = self.rows.get(i)
        if row_tree is None:
            row_tree = LLRB()
            self.rows.insert(i, row_tree)
        row_tree.insert(j, valor_transformado)

        # arvore de colunas
        col_tree = self.cols.get(j)
        if col_tree is None:
            col_tree = LLRB()
            self.cols.insert(j, col_tree)
        col_tree.insert(i, valor_transformado)

    def get(self, i, j):
        row_tree = self.rows.get(i)
        if row_tree is None:
            return 0

        value = row_tree.get(j)
        return value * self.escalar if value is not None else 0

    def soma(self, mB):
        resultado = matrizEsparsa()

        # Percorre todas as linhas da primeira matriz
        for i, row_tree in self.rows.inorder():
            for j, value in row_tree.inorder():
                resultado.set(i, j, value * self.escalar)

        # Percorre todas as linhas da segunda matriz
        for i, row_tree in mB.rows.inorder():
            for j, valor_b in row_tree.inorder():
                valor_atual = resultado.get(i, j)
                resultado.set(i, j, valor_atual + valor_b * mB.escalar)

        return resultado

    def multiplica_escalar(self, k):
        self.escalar *= k
        
    def multiplica_matrizes(self, mB):
        resultado = matrizEsparsa()

        resultado.escalar = self.escalar * mB.escalar

        # percorrendo cada linha i da matriz
        for i, row_tree_A in self.rows.inorder():

            # percorrendo cada elemento da linha
            for k, valor_A in row_tree_A.inorder():

                # verificando se a linha existe na outra matriz
                row_tree_B = mB.rows.get(k)
                if row_tree_B is None:
                    continue

                # percorrendo os elementos da linha
                for j, valor_B in row_tree_B.inorder():
                    valor_atual = resultado.get(i, j)
                    resultado.set(i, j, valor_atual + valor_A * valor_B * resultado.escalar)

        return resultado

    def print(self, max_rows=None, max_cols=None):
        """
        Imprime a matriz no terminal.
        max_rows e max_cols limitam o tamanho exibido.
        """

        # coleta índices existentes
        rows = [i for i, _ in self.rows.inorder()]
        cols = [j for j, _ in self.cols.inorder()]

        if not rows or not cols:
            print("[ matriz vazia ]")
            return

        min_row, max_row = min(rows), max(rows)
        min_col, max_col = min(cols), max(cols)

        if max_rows:
            max_row = min(max_row, min_row + max_rows - 1)
        if max_cols:
            max_col = min(max_col, min_col + max_cols - 1)

        # impressão
        for i in range(min_row, max_row + 1):
            linha = []
            for j in range(min_col, max_col + 1):
                valor = self.get(i, j)
                linha.append(f"{valor:6.2f}" if valor != 0 else "   .  ")
            print(" ".join(linha))
