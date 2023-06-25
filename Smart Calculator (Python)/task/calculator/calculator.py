from dataclasses import dataclass
import re


@dataclass(repr=False, eq=False)
class Calculator:
    my_dict = {}
    ls: str

    def check_ls(self) -> None:
        pattern = re.compile(r'[+\-*/]')
        if '=' in self.ls or not pattern.search(self.ls):
            list_data = self.ls.split('=')
            list_data = [i.strip() for i in list_data]
            self.filter_string(list_data)
        else:
            string = self.ls
            self.expression_evaluation(string)

    @classmethod
    def filter_string(cls, list_data) -> print:
        if list_data[0].isalpha() and list_data[-1].isdigit() and len(list_data) <= 2:
            cls.my_dict[list_data[0]] = list_data[-1]
        elif list_data[0].isalpha() and list_data[-1] in cls.my_dict and len(list_data) == 2:
            cls.my_dict[list_data[0]] = cls.my_dict[list_data[-1]]
        elif list_data[0].isalpha() and list_data[-1] in cls.my_dict and len(list_data) < 2:
            print(cls.my_dict[list_data[0]])
        elif not list_data[0].isalpha():
            print('Invalid identifier')
        elif (not list_data[-1].isdigit() and len(list_data) == 2) or len(list_data) > 2:
            print('Invalid assignment')
        else:
            print('Unknown variable')

    @classmethod
    def expression_evaluation(cls, string) -> print:
        new_ls = ''
        for ch in string:
            if ch in cls.my_dict:
                new_ls += cls.my_dict[ch]
            else:
                new_ls += ch
        if new_ls[0] == '/' or new_ls[0] == '*':
            print('Unknown variable')
        elif '//' in new_ls:
            print('Invalid expression')
        else:
            try:
                print(int(eval(new_ls)))
            except (NameError, SyntaxError):
                print('Invalid expression')


def main():
    while True:
        ls = input()
        if '/help' in ls:
            print('The program calculates the sum of numbers')
        elif '/exit' in ls:
            print('Bye!')
            break
        elif len(ls):
            ans = Calculator(ls)
            ans.check_ls()


if __name__ == "__main__":
    main()
