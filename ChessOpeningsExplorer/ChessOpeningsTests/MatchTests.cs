
using ChessOpeningsApp;
using System.Drawing;

namespace ChessOpeningsTests;

public class MatchTests
{
    Match testMatch;
    string testPlayer;

    [SetUp]
    public void Setup()
    {
        testPlayer = "DrNykterstein";
        string[] matchStrings = new string[]
        {
            @"[Event ""Rated Blitz game""]",
            @"[Site ""https://lichess.org/K1j60I2N""]",
            @"[Date ""2022.04.16""",
            @"[White ""DrNykterstein""]",
            @"[Black ""slowandviolent""]",
            @"[Result ""0-1""]",
            @"[UTCDate ""2022.04.16""]",
            @"[UTCTime ""23:29:24""]",
            @"[WhiteElo ""3213""]",
            @"[BlackElo ""3068""]",
            @"[WhiteRatingDiff ""-15""]",
            @"[BlackRatingDiff ""+13""]",
            @"[WhiteTitle ""GM""]",
            @"[Variant ""Standard""]",
            @"[TimeControl ""180+2""]",
            @"[ECO ""D85""]",
            @"[Termination ""Normal""]",
            @"1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. Bd2 c5 6. Rc1 Nxc3 7. Bxc3 Bh6 8. e3 cxd4 9. Bb5+ Nc6 10. Qxd4 Qxd4 11. Bxd4 O-O 12. Bxc6 bxc6 13. h4 f6 14. h5 g5 15. Ne2 e5 16. Bc5 Rd8 17. Be7 Re8 18. Ba3 Be6 19. Rxc6 Rac8 20. Rxc8 Rxc8 21. Nc3 g4 22. O-O g3 23. Rd1 Kf7 24. Rd3 f5 25. e4 fxe4 26. Rxg3 Bf4 27. Nxe4 Rc1+ 28. Kh2 Bxa2 29. Ng5+ Kg8 30. Ne4+ Bxg3+ 31. Kxg3 Kf7 32. Ng5+ Kg7 33. f3 Bd5 34. Bd6 e4 35. fxe4 Bc6 36. Be5+ Kh6 37. Kg4 Bd7+ 38. Kg3 Rb1 39. Nf3 Kxh5 40. Bd4 a5 41. Kf4 a4 42. Ke5 Kg4 43. Kd6 Be8 44. e5 Kg3 45. e6 Kxg2 46. Ng5 Rd1 47. Ke5 h5 48. Bc3 h4 49. Kf6 h3 50. Nxh3 Kxh3 51. Ke7 Bb5 52. Kf8 Kg4 53. e7 Rf1+ 54. Kg7 Be8 0-1"
        };

        testMatch = new(matchStrings);

    }

    [Test]
    public void ConvertsStringArrayToMatchObject()
    {
        string expectedWhitePlayer = "DrNykterstein";
        string expectedBlackPlayer = "slowandviolent";
        string expectedMatchResult = "0-1";

        Assert.That(expectedBlackPlayer, Is.EqualTo(testMatch.PlayerBlack));
        Assert.That(expectedWhitePlayer, Is.EqualTo(testMatch.PlayerWhite));
        Assert.That(expectedMatchResult, Is.EqualTo(testMatch.Result));

    }
}