import CLI
import Config


class Main:
    @staticmethod
    def main():
        print("Hello")
        cli = CLI.CLI()
        cli.parser()


# TODO:
if __name__ == '__main__':
    Main.main()