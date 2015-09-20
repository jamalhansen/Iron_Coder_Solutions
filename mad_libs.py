from string import Template

def main():
    print("First pick a story!")
    print("You need to type story1 or story2, like that.")
    choice = input("> ")
    if choice == "story1":
        print("In order, type an adjective, a noun, a pronoun, a verb")
        words = input("> ")
        vocab = words.split()
        create_story(choice, vocab)
    elif choice == "story2":
        print("In order, type a noun an adjective a verb an adjective a noun.")
        words = input("> ")
        vocab = words.split()
        create_story(choice, vocab)
    else:
        main()

def create_story(choice, words):
    story_temps = ["""So this will be a ${adj} story about ${noun}!
                ${pronoun}, ${verb} is absolutely amazing!""",
                """$noun1 will be doing $adj1 things. $verb is $adj2 for $noun2."""]
    if choice == "story1":
        for text in words:
            if text == words[0]:
                # The code '\033[31m' is the start sequence
                # and color code for the text.
                # '\033[0m' is the end sequence.
                adj = '\033[31m' + text + '\033[0m'
            elif text == words[1]:
                noun = '\033[31m' + text + '\033[0m'
            elif text == words[2]:
                pronoun = '\033[31m' + text + '\033[0m'
            elif text == words[3]:
                verb = '\033[31m' + text + '\033[0m'
        temp = story_temps[0]
        templ = Template(temp)
        print(templ.safe_substitute(adj=adj, noun=noun, pronoun=pronoun, verb=verb))
    elif choice == "story2":
        for text in words:
            if text == words[0]:
                n = '\033[31m' + text + '\033[0m'
            elif text == words[1]:
                a = '\033[31m' + text + '\033[0m'
            elif text == words[2]:
                v = '\033[31m' + text + '\033[0m'
            elif text == words[3]:
                a2 = '\033[31m' + text + '\033[0m'
            elif text == words[4]:
                n2 = '\033[31m' + text + '\033[0m'
        temp = story_temps[1]
        templ = Template(temp)
        print(templ.safe_substitute(noun1=n, adj1=a, verb=v, adj2=a2, noun2=n2))


if __name__ == '__main__':
    main()
