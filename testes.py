import unittest;
from aluno import AlunoClass; 
from turma import TurmaClass;
from conexao import ConexaoClass;
import mongomock;


class alunoTest(unittest.TestCase):
  @mongomock.patch(servers=(('localhost.com', 27017),))
  def setUp(self):
    print('Teste', self._testMethodName, 'sendo executado...');
    self.aluno = AlunoClass('Fabio', 'Teixeira', 10);
    self.turma = TurmaClass();
    self.turma.cadastrarAlunos([self.aluno]);
    self.conexao = ConexaoClass.conexaoMongoDB(self, url = 'localhost.com', banco = 'faculdade')

   def test_salvarAluno(self):
    resposta = self.aluno.salvar(conexao = self.conexao, colecao = 'aluno');
    self.assertEqual(True, resposta, 'Aluno cadastrado incorretamente!');
    self.assertEqual(1, self.conexao['aluno'].count_documents({'nome': 'Fabio', 'sobrenome': 'Teixeira', 'nota': 10}), 'Aluno nao foi encontrado no banco!');

  def test_salvarTurma(self):   
    resposta = self.turma.salvar(conexao = self.conexao, colecao = 'turma');  
    self.assertEqual(True, resposta, 'Turma cadastrada incorretamente!');

if __name__ == "__main__":
  unittest.main()
