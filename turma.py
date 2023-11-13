class Turma:
  def __init__(self):
    self.turma = [];
    self.menorNota = float('inf') 
    self.maiorNota = float('-inf') 

  def cadastrarAlunos(self, alunos):
    for aluno in alunos:
      if aluno.nota < 0:
        raise ValueError('A nota não pode ser menor que 0')
      if aluno.nota > 10:
        raise ValueError('A nota não pode ser maior que 10')
      self.turma.append(aluno)
      if aluno.nota < self.menorNota:
        self.menorNota = aluno.nota
      if aluno.nota > self.maiorNota:
        self.maiorNota = aluno.nota               

  def mostrarAlunos(self):  
    print('Quantidade de alunos:', len(self.turma));
    for x in self.turma:      
      print(x.mostrarAluno());
