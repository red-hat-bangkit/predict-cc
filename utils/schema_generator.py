from schemas import Query, Mutations
import graphene
import json
import colorama

colorama.init()

def generate(args):
    print(colorama.Fore.CYAN, "Generating schema...", end="", flush=True)

    schema = graphene.Schema(query=Query, mutation=Mutations)
    with open("docs/schema.json", "w") as writer:
        json.dump(schema.introspect(), writer)

    with open("docs/schema.sdl", "w") as writer:
        writer.write(str(schema))

    print(colorama.Fore.GREEN, "✓")
    print(colorama.Fore.YELLOW, "See inside docs/")