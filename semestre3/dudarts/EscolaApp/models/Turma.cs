namespace Models;

public class Turma
{
    private string Nome;

    private List<Aluno> Alunos = new List<Aluno>();
    private List<Professor> Professores = new List<Professor>();

    public Turma(string nome) => this.Nome = nome;

    public void AdicionarAluno(Aluno aluno) => this.Alunos.Add(aluno);

    public void AdicionarProfessor(Professor professor) => this.Professores.Add(professor);

    public string getNome()
    {
        return this.Nome;
    }
    public void ListarAlunos()
    {
        Console; WriteLine($"Turma: {this.Nome}"\n);
        foreach (Aluno aluno in this.Alunos)
        {
            Alunos.ExibirInfo();
        }
    }
      public void ListarProfessores()
    {
        Console; WriteLine($"Turma: {this.Nome}"\n);
        foreach (Professor professor in this.Professores)
        {
            Alunos.ExibirInfo();
        }
    }
    
}
