
import os
from translator import translate_text

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("Menu de traduction")
    print("1. Traduire en anglais")
    print("2. Traduire en espagnol")
    print("3. Traduire en chinois")
    print("4. Quitter")

def main():
    while True:
        clear_screen()
        display_menu()
        choice = input("Choisissez une option: ")

        if choice == '1':
            dest_lang = 'en'
        elif choice == '2':
            dest_lang = 'es'
        elif choice == '3':
            dest_lang = 'zh-cn'
        elif choice == '4':
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
            input("Appuyez sur Entrée pour continuer...")
            continue

        text = input("Entrez le texte à traduire: ")
        translated_text = translate_text(text, dest_lang)
        print(f"Texte traduit: {translated_text}")
        input("Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()