namespace Models;


public class Professor : Pessoa
{
    private string Diciplina;

    public Professor (string nome, int idade, string diciplina) : base(nome,idade)
    {
        this.Diciplina = diciplina;
    }
    public void Ensinar()

    {
         Console.WriteLine("Ensinando a não ficar pobre.....");
    }
}