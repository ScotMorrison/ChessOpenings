using System.Data;
namespace ChessOpeningsApp;

public class Program
{
    static void Main(string[] args)
    {

    }
    
    public static Colour IdentifyTeam(string[] matchObject, string playerName)
    {
        var teamLine = matchObject.Where(line => line.Contains(playerName));

        return teamLine.First().Contains("White") ? Colour.WHITE : Colour.BLACK;
    }
}

public enum Colour { WHITE, BLACK }
public enum MatchResult { WIN, LOSS, DRAW }

public class Match
{
    public readonly string Result;
    public readonly string PlayerWhite;
    public readonly string PlayerBlack;
    public readonly string Moves;
    public Match(string[] matchStrings)
    {
        Result = InitialiseMemberFromStrings(matchStrings, "Result");
        PlayerWhite = InitialiseMemberFromStrings(matchStrings, "White");
        PlayerBlack = InitialiseMemberFromStrings(matchStrings, "Black");
    }
    private string InitialiseMemberFromStrings(string[] input, string identifier)
    {
        return input.Where(line => line.Contains(identifier)).First().Split('\"')[1];
    }
}