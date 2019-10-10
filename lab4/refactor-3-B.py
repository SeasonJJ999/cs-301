def fix(moves, should):
    if should:
        if moves:
            return "good"
        else:
            return "WD-40"
    else:
        if moves:
            return "duct tape"
        else:
            return "good"

print(fix(False, False))
