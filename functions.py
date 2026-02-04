def add(x, y):
        return x + y
def add(x, y):
      return x + y
def get_user_full_name(user_data):
      first_name = user_data.get("first_name", "")
      last_name = user_data.get("last_name", "")
      return f"{first_name} {last_name}".strip()
def divide(a, b):
      if b == 0:
            raise ValueError
      return a / b