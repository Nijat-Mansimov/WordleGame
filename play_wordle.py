from letter_state import LetterState
from wordle import Wordle
from colorama import Fore


def main():
    print("Hello Wordle")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("\nType your guess: ")

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Word must be {wordle.WORD_LENGTH} characters long!"
                  + Fore.RESET)
            continue
        wordle.attempt(x)
        display_results(wordle)
        result = wordle.guess(x)
        # print(*result, sep="\n")

    if wordle.is_solved:
        print("You've solved the puzzle.")

    else:
        print("You failed to solved the puzzle.")


def display_results(wordle: Wordle):
    print(f"You have {wordle.remaining_attempts} attempts remaining.")

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)
    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))

    draw_border_around(lines)


def convert_result_to_color(result: list[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE

        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)

    return " ".join(result_with_color)


def draw_border_around(lines: list[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    buttom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)
    for line in lines:
        print("│" + space + line + space + "│")
    print(buttom_border)


if __name__ == "__main__":
    main()
