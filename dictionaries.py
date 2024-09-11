"""
leetspeak_dic: This is a dictionary containing a mapping of characters to their "leet speak" equivalents. Each character in the dictionary (a through z) is mapped to a list of possible leet substitutions. These substitutions include both numbers and special characters. Leet speak is commonly used in online communities to obfuscate text or create a "hacker-style" look

suffixes: This is a list of common suffixes that users often append to passwords. It includes numeric sequences (123, 456), repeated characters (!!!, ###), special characters (@, $), common keyboard patterns (qwerty, asd), and current or recent years (2020, 2023). These suffixes are often predictable and used by people to meet password complexity requirements while remaining easy to remember.
"""


leetspeak_dict = {
    1: {
        "a": ["4", "@"],
        "b": ["I3", "13", "8", "|3"],
        "c": ["[", "<", "(", "{"],
        "d": ["|)", "|]"],
        "e": ["3", "&", "€"],
        "f": ["|=", "ph"],
        "g": ["6", "9", "&", "(_+"],
        "h": ["#", "|-|", "]-[", "}{"],
        "i": ["1", "!", "|", "eye"],
        "j": ["_|", "_]", "]"],
        "k": ["|<", "|{"],
        "l": ["1", "|", "£", "|_"],
        "m": ["/\\/\\", "|\\/|", "^^", "em"],
        "n": ["/\\/", "|\\|", "//"],
        "o": ["0", "()", "[]", "<>"],
        "p": ["|*", "|o", "|º"],
        "q": ["O_", "9", "(_,)", "0,"],
        "r": ["|2", "|?", "12", "®"],
        "s": ["5", "$", "§"],
        "t": ["7", "+", "†"],
        "u": ["|_|", "(_)", "v"],
        "v": ["\\/", "|/"],
        "w": ["\\/\\/", "vv", "\\^/"],
        "x": ["><", "}{", "×", "}{}"],
        "y": ["'/", "¥", "j"],
        "z": ["2", "7_", ">_"]
    }
}

suffixes = [
    "",
    "123", "123123", "1234", "12345", "123456", "123456789",
    "hihi", "haha", "hehe", "huhu", "kaka", "keke", "kuku",
    "456", "456456",
    "789", "789789",
    "111", "222", "333", "444", "555", "666", "777", "888", "999",
    "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999",
    "zzz","xxx","ccc","aaa","sss","ddd","qqq","www","eee",
    "xyz", "xyz123",
    "zxc", "zxczxc", "cxz", "cxzcxz",
    "asd", "asdasd", "dsa", "dsadas",
    "abc", "abcd",
    "qwe", "qweqwe", "ewq", "ewqeqw", "qwerty",
    "2020", "2021", "2022", "2023", "2024", "2025",
    "!", "!!", "!!!",
    "@", "@@", "@@@",
    "#", "##", "###",
    "`", "``", "```",
    "`12", "`123", "21`", "321`",
    ".", "..", "...",
    ",", ",,", ",,,",
    "$", "$$", "$$$",
    "?", "??", "???",
    "~!@#", "!@#", "@#$", "~!@#$", "#@!", "@!~", "#@!~"
]
