from __future__ import annotations

from datetime import datetime
from pathlib import Path


NOTES_FILE = Path(__file__).with_name("notes.txt")


def cmd_help() -> None:
    print("/help - список команд")
    print("/time - текущее время")
    print("/sum a b [c ...] - сумма чисел")
    print("/note text - сохранить заметку")
    print("/exit - выход")


def cmd_time() -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now)


def cmd_sum(args: list[str]) -> None:
    if not args:
        print("Использование: /sum 2 5 [7 ...]")
        return

    numbers: list[float] = []
    for a in args:
        try:
            numbers.append(float(a))
        except ValueError:
            print(f"Ошибка: '{a}' не число")
            return

    print(sum(numbers))


def cmd_note(args: list[str]) -> None:
    if not args:
        print("Использование: /note ваш текст")
        return

    text = " ".join(args).strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)
    with NOTES_FILE.open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")

    print("Заметка сохранена.")


def main() -> None:
    print("Assistant CLI started. Type /help")

    while True:
        raw = input("> ").strip()
        if not raw:
            continue

        parts = raw.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "/exit":
            print("Bye!")
            break
        elif cmd == "/help":
            cmd_help()
        elif cmd == "/time":
            cmd_time()
        elif cmd == "/sum":
            cmd_sum(args)
        elif cmd == "/note":
            cmd_note(args)
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
