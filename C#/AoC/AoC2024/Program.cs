namespace AoC2024;

internal abstract class Program
{
    private static void Main(string[] args)
    {
        if (args.Length < 2)
        {
            Console.WriteLine("Usage: AoC2024 <day> <exercise>");
            return;
        }

        var day = args[0];
        var exercise = args[1];

        try
        {
            // Dynamically load and execute the specified exercise
            var className = $"AoC2024.dec{day}.Dec{exercise}";
            var type = Type.GetType(className);
            if (type == null)
            {
                Console.WriteLine($"Exercise not found: {className}");
                return;
            }

            var method = type.GetMethod("Run");
            method?.Invoke(null, null);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}