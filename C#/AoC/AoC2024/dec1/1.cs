namespace AoC2024.dec1;

public class Dec1
{
    public static void Run()
    {
        // Read and parse input, skipping empty or invalid lines
        var lines = File.ReadAllLines("../../../dec1/input.txt")
            .Where(line => !string.IsNullOrWhiteSpace(line))
            .Select(line => line.Split().Where(part => int.TryParse(part, out _)).Select(int.Parse).ToArray())
            .Where(parts => parts.Length == 2)
            .ToArray();

        // Separate and sort values
        var leftList = lines.Select(x => x[0]).OrderBy(x => x).ToArray();
        var rightList = lines.Select(x => x[1]).OrderBy(x => x).ToArray();

        // Calculate and print total distance
        var totalDistance = leftList.Zip(rightList, (l, r) => Math.Abs(l - r)).Sum();
        Console.WriteLine(totalDistance);
    }
}