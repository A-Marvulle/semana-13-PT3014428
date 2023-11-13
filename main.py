import aluno as a;
import turma as t;

alunos = []
alunos.append(a.Aluno('Fabiano', 'Teixeira', 10));
alunos.append(a.Aluno('Fabio', 'Teixeira', 8));
alunos.append(a.Aluno('Melissa', 'Teixeira', 6));
alunos.append(a.Aluno('Fabiano', 'Teixeira', 7));

turmaObject = t.Turma();
turmaObject.cadastrarAlunos(alunos);

turmaObject.mostrarAlunos();
print('*'*30)
print('Aluno com menor nota:', turmaObject.menorNota)
print('Aluno com maior nota:', turmaObject.maiorNota)
