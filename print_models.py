def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing current design : " + current_design.title())

        completed_models.append(current_design)


def show_comleted_models(completed_models):

    for completed_model in completed_models:
        print("You have completed the design " + completed_model.title()
              + ".")

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahetron']
comleted_models = []

print_models(unprinted_designs, comleted_models)
show_comleted_models(comleted_models)

print(unprinted_designs)


