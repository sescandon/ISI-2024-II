using Práctica_2___Problema_de_las_jarras;

public class StateSpaceCalculator
{
    private HashSet<string> visitedStates;
    private Jar jar3L;
    private Jar jar5L;

    public StateSpaceCalculator()
    {
        visitedStates = new HashSet<string>();
        jar3L = new Jar(3);
        jar5L = new Jar(5);
    }

    private string GetStateKey(Jar jar1, Jar jar2)
    {
        return $"{jar1.getCurrentVolume()},{jar2.getCurrentVolume()}";
    }

    public HashSet<string> CalculateStateSpace()
    {
        ExploreStates(jar3L, jar5L);
        return visitedStates;
    }

    private void ExploreStates(Jar jar1, Jar jar2)
    {
        string currentState = GetStateKey(jar1, jar2);

        if (visitedStates.Contains(currentState))
        {
            return;
        }

        visitedStates.Add(currentState);

        Jar jar1Back = new Jar(jar1);
        Jar jar2Back = new Jar(jar2);

        jar1.fill();
        ExploreStates(jar1, jar2);
        jar1 = new Jar(jar1Back);

        jar2.fill();
        ExploreStates(jar1, jar2);
        jar2 = new Jar(jar2Back);

        jar1.empty();
        ExploreStates(jar1, jar2);
        jar1 = new Jar(jar1Back);

        jar2.empty();
        ExploreStates(jar1, jar2);
        jar2 = new Jar(jar2Back);


        jar1.fill(jar2);
        ExploreStates(jar1, jar2);
        jar1 = new Jar(jar1Back);
        jar2 = new Jar(jar2Back);

        jar2.fill(jar1);
        ExploreStates(jar1, jar2);
        jar1 = new Jar(jar1Back);
        jar2 = new Jar(jar2Back);
    }
}