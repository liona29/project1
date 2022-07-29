class big_char(object):
    def __init__(self):
        self.A = [
            "             "
            , "      /\       "
            , "     /  \      "
            , "    /    \     "
            , "   /______\    "
            , "  /        \   "
            , " /          \  "
            , "/            \ "]
        self.R = [
            "        "
            , " ____   "
            , "|    \  "
            , "|     | "
            , "|____/  "
            #     ,"|  \    "
            , "|   \   "
            , "|    \  "]
        self.I = [
            "        "
            , "_______ "
            , "   |    "
            , "   |    "
            #      ,"   |    "
            , "   |    "
            , "   |    "
            , "------- "]
        self.B = [
             "        "
            ," ____   "
            ,"|    \  "
            ,"|____/  "
            ,"|    \  "
            ,"|     | "
            ,"|____/  "]
        self.C = [
             "         "
            ,"  _____  "
            ,"/      \ "
            ,"|        "
            ,"|        "
            ,"|        "
            ,"\______/ "
        ]
        self.D = [
             "         "
            ," ____    "
            ,"|    \   "
            ,"|     \  "
            ,"|      | "
            ,"|     /  "
            ,"|____/   "
        ]
        self.E = [
             "        "
            ,"_______ "
            ,"|       "
            ,"|       "
            ,"|------ "
            ,"|       "
            ,"|______ "
        ]
        self.F = [
             "        "
            ,"_______ "
            ,"|       "
            ,"|       "
            ,"|------ "
            ,"|       "
            ,"|       "
        ]
        self.G = [
             "         "
            ," ______  "
            ,"/      \ "
            ,"|  ___   "
            ,"|     \  "
            ,"|      | "
            ,"\_____/  "
        ]
        self.H = [
            "        "
            , "|      | "
            , "|      | "
            , "|______| "
            , "|      | "
            , "|      | "
            , "|      | "
        ]
        self.J = [
            "        "
            , "    ___ "
            , "      | "
            , "      | "
            , "      | "
            , "      | "
            , "\____/  "
        ]
        self.K = [
            "        "
            , "|    /  "
            , "|   /   "
            , "|__/    "
            , "|  \    "
            , "|   \   "
            , "|    \  "
        ]
        self.L = [
            "          "
            , "|       "
            , "|       "
            , "|       "
            , "|       "
            , "|       "
            , "|______ "
        ]
        self.M = [
            "                 "
            , "|\          /| "
            , "| \        / | "
            , "|  \      /  | "
            , "|   \    /   | "
            , "|    \  /    | "
            , "|     \/     | "
        ]
        self.N = [
              "         "
            , "|\     | "
            , "| \    | "
            , "|  \   | "
            , "|   \  | "
            , "|    \ | "
            , "|     \| "
        ]
        self.O = [
              "          "
            , "  _____   "
            , " /     \  "
            , "|       | "
            , "|       | "
            , "|       | "
            , " \_____/  "
        ]
        self.P = [
              "         "
            , "______   "
            , "|     \  "
            , "|      | "
            , "|_____/  "
            , "|        "
            , "|        "
            ]
        self.Q = [
            "          "
            , "  _____   "
            , " /     \  "
            , "|       | "
            , "|       | "
            , "|      \| "
            , " \_____/\ "
            ]
        self.S= [
            "        "
            , "  ____   "
            , "/      \ "
            , "\____    "
            , "      \  "
            , "       | "
            , "\_____/  "
        ]
        self.T = [
            "        "
            , "_________ "
            , "    |     "
            , "    |     "
            , "    |     "
            , "    |     "
            , "    |     "
        ]
        self.U = [
            "          "
            , "|       | "
            , "|       | "
            , "|       | "
            , "|       | "
            , "|       | "
            , " \_____/  "
        ]
        self.V = [
            "          "
            , "\          / "
            , " \        /  "
            , "  \      /   "
            , "   \    /    "
            , "    \  /     "
            , "     \/      "
        ]
        self.W = [
            "          "
            , "\          /\          / "
            , " \        /  \        /  "
            , "  \      /    \      /   "
            , "   \    /      \    /    "
            , "    \  /        \  /     "
            , "     \/          \/      "
        ]
        self.X = [
            "          "
            , "\    / "
            , " \  /  "
            , "  \/   "
            , "  /\   "
            , " /  \  "
            , "/    \ "
        ]
        self.Y = [
            "          "
            , "\       / "
            , " \     /  "
            , "  \   /   "
            , "   \ /    "
            , "    |     "
            , "    |     "
        ]
        self.Z = [
            "          "
            , "_______ "
            , "      / "
            , "     /  "
            , "   /    "
            , " /      "
            , "/______ "
        ]
        self.space = [
            "         "
            , "        "
            , "        "
            , "        "
            , "        "
            , "        "
            , "        "
        ]
        self.charsbig = {"A": self.A
            , "R": self.R
            , "I": self.I
            , "B": self.B
            , "C": self.C
            , "D": self.D
            , "E": self.E
            , "F": self.F
            , "G": self.G
            , "H": self.H
            , "J": self.J
            , "K": self.K
            , "L": self.L
            , "M": self.M
            , "N": self.N
            , "O": self.O
            , "P": self.P
            , "Q": self.Q
            , "S": self.S
            , "T": self.T
            , "U": self.U
            , "V": self.V
            , "W": self.W
            , "X": self.X
            , "Y": self.Y
            , "Z": self.Z
            , " ": self.space
                         }

    def char_big_str(self, str):
        newstr = ""
        for i in range(7):
            for ch in str.upper():
                if ch in(" ABCDEFGHIJKLMNOPQRSTUVWXYZ") :
                    newstr += self.charsbig[ch][i]
            newstr += "<br>"
        return newstr

def biger(str):
        c = big_char()
        ans = c.char_big_str(str)
        return ans

