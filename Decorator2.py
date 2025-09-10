
def admin_(func):
 def inner():
  role = input("Enter your role(admin/user:)")
  if role=="admin":
     func()
  else: 
    print("Denied!Admins only.")
 return inner


@admin_
def renew_data():
  print("Data renewed successfully!")
  

renew_data()