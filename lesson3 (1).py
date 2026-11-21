class User:
    def __init__(self , name):
        self.name = name
        self.password = None
        self.login = None
        self.is_active = None

    login_list = []
    password_list =[]

    def save_password(password):
        with open("password.txt","r") as pasw:
            if password in pasw.read():
                print("такой пароль уже есть")
        with open("password.txt","a") as pasw:
            pasw.write("\n" + str(password))
    
    def set_password(self, password):
        User.password_list.append(password)
        self.password = password
        User.save_password(password)

    def check_password(self, password):
        return self.password == password

    def check_login(login):
        if login not in User.login_list:
            return True
        else:
            return False

    def set_login(self, login):
        User.login_list.append(login)
        self.login = login
 
    def user_register(self , login, password):
        if User.check_login(login):
            self.set_login(login)
            self.set_password(password)
            print("Юзер успешно зарегистрирован!" , self.name , "Ваш логин: " , self.login)
        else:
            print("Пользователь с таким логином сушествует")

    def user_login( login, password):
        current_login = login
        current_password = password    
        while True:
            if current_login in User.login_list and current_password in User.password_list:
                print("Вы успешно вошли в систему!")
                break
            else:
                print("Вход воспрещён, повторите попытку ещё раз!")
                current_login = input("Введите логин: ")
                current_password = input("Введите пароль: ")
            

 
user1 = User(name="Sanya")
user2 = User(name="Vanya")

user1.user_register(input("Введите логин: "),input("Введите пароль: "))
user2.user_register(input("Введите логин: "),input("Введите пароль: "))
for i in range(1,6):
    user1.user_register("tutuy" + str(i), "pass" + str(i))
print(User.login_list)
print(User.password_list)
User.user_login(input("Введите логин: "),input("Введите пароль: ")) 


login_pass = {
    "tutuy1" : "pass1" ,
    "tutuy2" : "pass2" ,
    "tutuy3" : "pass3" ,
    "tutuy4" : "pass4" ,
    "tutuy5" : "pass5"
}
login_pass["tutuy5"] = "pass5"
print(login_pass.keys())

print(login_pass.values())
print(type(login_pass))
