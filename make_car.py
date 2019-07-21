def make_car(manufature, model, **cars_info):
    cars_profile = {}
    cars_profile['manufacturer'] = manufature
    cars_profile['model'] = model
    for key, value in cars_info.items():
        cars_profile[key] = value
    return cars_profile

