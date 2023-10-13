# Create unit test using those cases:
# fixed_tests_True = (
#     ( "samurai", "ai"    ),
#     ( "ninja",   "ja"    ),
#     ( "sensei",  "i"     ),
#     ( "abc",     "abc"   ),
#     ( "abcabc",  "bc"    ),
#     ( "fails",   "ails"  ),
# )
# fixed_tests_False = (
#     ( "sumo",    "omo"   ),
#     ( "samurai", "ra"    ),
#     ( "abc",     "abcd"  ),
#     ( "ails",    "fails" ),
#     ( "this",    "fails" ),
#     ( "spam",    "eggs"  )
# from unittest                       

# class Exo1Test(unittest.TestCase):

#     def test_item_construction(self):
#         item = Item(10, 20)

#         self.assertEqual(20, item.weight)
from exo2 import solution 

def test_solution():
    fixed_tests_True = [
        ("samurai", "ai"),
        ("ninja", "ja"),
        ("sensei", "i"),
        ("abc", "abc"),
        ("abcabc", "bc"),
        ("fails", "ails"),
    ]

    fixed_tests_False = [
        ("sumo", "omo"),
        ("samurai", "ra"),
        ("abc", "abcd"),
        ("ails", "fails"),
        ("this", "fails"),
        ("spam", "eggs"),
]

    for ch1, ch2 in fixed_tests_True:
        assert solution(ch1, ch2) is True

    for ch1, ch2 in fixed_tests_False:
        assert solution(ch1, ch2) is False

test_solution()